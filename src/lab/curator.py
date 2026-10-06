"""GUIDE Phần 3 - Người tuyển chọn skill (skill curator): tự viết skill từ các lần chạy thất bại.   >>> SINH VIÊN CÀI ĐẶT curate_skills <<<

Pseudo-code: guides/pseudocode/04_curator.md
Kiểm tra:    pytest tests/test_04_curator.py
Chạy thật:   python -m lab.curator
"""
import json
import re
from pathlib import Path

from .model import make_model
from .tasks import ROOT, eval_markers   # có sẵn: định danh của tác vụ đánh giá, tính lúc chạy

# ---- CÓ SẴN, KHÔNG SỬA: kiểm tra và tách khối skill (phần dễ sai và liên quan bảo mật) ----------------
SAFE_NAME = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def validate_skill(text: str, expected_name: str | None = None) -> list[str]:
    """Kiểm tra nội dung một SKILL.md. Trả về danh sách vấn đề (rỗng = hợp lệ).

    Quy tắc: có khối YAML frontmatter; `name` chữ thường/số/gạch ngang (tối đa 64 ký tự) và bằng `expected_name`
    nếu được truyền; có `description` (tối đa 1024 ký tự); phần thân tối đa 80 dòng; không chứa chuỗi nào của
    `eval_markers()`. Quy tắc về `name` cũng là biện pháp bảo mật: tên khối do LLM sinh ra được dùng để tạo
    đường dẫn, nên `../evil` không được lọt qua.
    """
    problems = []
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text.strip() + "\n", re.S)
    if not m:
        return ["missing YAML frontmatter"]
    front, body = m.groups()
    name = re.search(r"^name:\s*(.+)$", front, re.M)
    desc = re.search(r"^description:\s*(.+)$", front, re.M)
    n = name.group(1).strip() if name else ""
    if not SAFE_NAME.fullmatch(n) or len(n) > 64:
        problems.append("invalid name")
    elif expected_name is not None and n != expected_name:
        problems.append("name differs from the block name")
    if not desc or len(desc.group(1).strip()) > 1024:
        problems.append("missing or too long description")
    if len(body.strip().splitlines()) > 80:
        problems.append("body longer than 80 lines")
    low = text.lower()
    for marker in eval_markers():
        if marker in low:
            problems.append(f"mentions evaluation material: {marker}")
    return problems


def parse_skill_blocks(reply: str) -> list[tuple[str, str]]:
    """Tách câu trả lời của LLM thành danh sách (name, nội dung SKILL.md).

    Khuôn dạng: `=== SKILL: <name> ===` ... `=== END ===`. Một khối kết thúc ở điểm nào đến trước trong ba điểm:
    `=== END ===`, tiêu đề `=== SKILL:` kế tiếp, hoặc cuối văn bản (LLM đôi khi quên dòng END).
    """
    pattern = re.compile(r"^=== SKILL: (\S+) ===[ \t]*\n(.*?)(?=^=== END ===|^=== SKILL: |\Z)", re.S | re.M)
    return [(name, text.strip()) for name, text in pattern.findall(str(reply))]
# --------------------------------------------------------------------------------------------------


def curate_skills(results_dir="results", source_condition="baseline", out_dir=None, model=None, max_skills: int = 3) -> list[Path]:
    """Đọc các lần chạy của TÁC VỤ HỌC (role == "learn") trong `source_condition`, nhờ LLM viết skill, ghi file.

    Các bước: nạp run.json + trace.md -> (nếu không có check nào thất bại: in cảnh báo và trả về [] mà KHÔNG gọi LLM)
    -> dựng prompt -> model.invoke(prompt) -> parse_skill_blocks -> validate_skill(text, expected_name=name)
    -> ghi `<out_dir>/<name>/SKILL.md`. Mặc định `out_dir` = <gốc lab>/skills/auto (dùng `ROOT` từ lab.tasks).
    Giữ tối đa `max_skills` skill hợp lệ; skill không hợp lệ bị bỏ qua.
    Prompt chứa, với mỗi check thất bại, TÊN và trường `detail` (lời nhận xét của bot đánh giá: phát biểu quy tắc bị vi phạm)
    cùng phần cuối của vết (trace). Với tác vụ học, `detail` chỉ phát biểu quy tắc, không chứa đáp án.
    Tuyệt đối KHÔNG đưa dữ liệu của tác vụ đánh giá (role == "eval") vào prompt.
    model mặc định: make_model() (lab.model).
    Trả về: danh sách đường dẫn SKILL.md đã ghi.
    """
    if out_dir is None:
        target_dir = ROOT / "skills" / "auto"
    else:
        target_dir = Path(out_dir)

    runs = []
    cond_path = Path(results_dir) / source_condition
    if cond_path.exists():
        for task_dir in sorted(cond_path.iterdir()):
            run_json = task_dir / "run.json"
            if not run_json.is_file():
                continue
            r = json.loads(run_json.read_text(encoding="utf-8"))
            if r.get("role") != "learn":
                continue

            trace_file = task_dir / "trace.md"
            trace_content = trace_file.read_text(encoding="utf-8") if trace_file.is_file() else ""
            trace_tail = trace_content[-6000:] if len(trace_content) > 6000 else trace_content

            failed = [
                (c.get("name", ""), c.get("detail", ""))
                for c in r.get("checks", [])
                if not c.get("passed")
            ]
            runs.append({
                "task": r.get("task", task_dir.name),
                "failed": failed,
                "trace": trace_tail,
            })

    total_failed = sum(len(run["failed"]) for run in runs)
    if total_failed == 0:
        print("Cảnh báo: không có check thất bại ở tác vụ học.")
        return []

    run_blocks = []
    for run in runs:
        if not run["failed"]:
            continue
        failed_lines = "\n".join(f"- Check '{name}': {detail}" for name, detail in run["failed"])
        run_blocks.append(
            f"Task: {run['task']}\nFailed checks:\n{failed_lines}\n\nExecution trace (last part):\n{run['trace']}"
        )
    runs_text = "\n\n---\n\n".join(run_blocks)

    prompt = (
        f"You are an expert developer creating reusable skills for an AI agent.\n"
        f"Below are the failed checks (check names and grader feedback) and execution traces from recent runs on learning tasks.\n"
        f"Analyze the common procedural failures and write at most {max_skills} concise skills to prevent them.\n\n"
        f"Rules:\n"
        f"1. Skills must be general procedural guidelines (e.g., formatting conventions, test verification, edge cases), not hardcoded answers.\n"
        f"2. Each skill must have YAML frontmatter with 'name' (lowercase alphanumeric with hyphens, max 64 chars) and 'description' (a clear sentence stating when to trigger the skill).\n"
        f"3. The body of each skill must be at most 80 lines.\n"
        f"4. Format every skill strictly as:\n"
        f"=== SKILL: <name> ===\n"
        f"---\n"
        f"name: <name>\n"
        f"description: <when to use this skill>\n"
        f"---\n"
        f"<body instructions>\n"
        f"=== END ===\n\n"
        f"Here are the learning task run details:\n\n{runs_text}"
    )

    if model is None:
        model = make_model()

    raw_content = model.invoke(prompt).content
    if isinstance(raw_content, list):
        reply = "".join(
            part.get("text", "") if isinstance(part, dict) else str(part)
            for part in raw_content
        )
    else:
        reply = str(raw_content)

    written = []
    for name, text in parse_skill_blocks(reply):
        if len(written) >= max_skills:
            break
        problems = validate_skill(text, expected_name=name)
        if problems:
            continue
        skill_file = target_dir / name / "SKILL.md"
        skill_file.parent.mkdir(parents=True, exist_ok=True)
        skill_file.write_text(text + "\n", encoding="utf-8")
        written.append(skill_file)

    return written


if __name__ == "__main__":
    for p in curate_skills():
        print("wrote", p)
