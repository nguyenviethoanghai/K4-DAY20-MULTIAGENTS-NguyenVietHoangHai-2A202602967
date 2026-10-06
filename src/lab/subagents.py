"""GUIDE Phần 1 - Định nghĩa subagent (tác tử con).   >>> SINH VIÊN CÀI ĐẶT <<<

Pseudo-code: guides/pseudocode/02_subagents.md
Kiểm tra:    pytest tests/test_02_agent.py
"""


def get_subagents() -> list[dict]:
    """Trả về danh sách subagent (ít nhất 2, tên khác nhau).

    Mỗi phần tử là một dict có các khóa bắt buộc:
      "name":          tên duy nhất (chữ thường, có thể có dấu gạch ngang)
      "description":   khi nào tác tử chính nên giao việc cho subagent này (viết như một hướng dẫn hành động)
      "system_prompt": chỉ dẫn cho subagent
    Gợi ý vai trò: explorer (đọc và báo cáo), implementer (thực hiện), reviewer (kiểm tra độc lập).
    """
    return [
        {
            "name": "explorer",
            "description": "Use to explore the workspace, inspect files (such as README, source code, data samples, logs), and report findings. Does not modify any files.",
            "system_prompt": "You are an exploratory subagent. Your role is to read and inspect existing files in workspace/ (such as documentation, code, data schemas, sample records). Report concise, factual summaries and root-cause analyses back to the main agent. Do NOT modify or delete any files.",
        },
        {
            "name": "implementer",
            "description": "Use to implement code fixes, write data transformation scripts, process logs, or run tests and report execution outputs.",
            "system_prompt": "You are an implementation subagent. Your role is to make precise edits to code or data files in workspace/ and execute tests or scripts using shell commands. Verify your work with test runs and return a summary of changes and test outcomes back to the main agent.",
        },
        {
            "name": "reviewer",
            "description": "Use after changes are made to independently verify solutions, check edge cases, format constraints, and ensure all requirements are met without making modifications.",
            "system_prompt": "You are a quality assurance and code review subagent. Your role is to independently verify that the modifications meet all requirements, edge cases, and output schemas specified in the task instructions. Do NOT modify any files; only inspect files and test outputs, then report any discrepancies or confirmation of correctness.",
        },
    ]
