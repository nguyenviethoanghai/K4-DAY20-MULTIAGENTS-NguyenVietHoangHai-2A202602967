# Báo cáo Lab: Self evolving Agentic

## 1. Thông tin sinh viên và cấu hình

- Họ tên: Nguyễn Viết Hoàng Hải
- Mã sinh viên: 2A202602967
- Nhà cung cấp và mô hình (`LAB_MODEL`, không ghi khóa API), nhiệt độ (`LAB_TEMPERATURE`), `recursion_limit`: google_genai:gemini-3.5-flash-lite, LAB_TEMPERATURE=0, recursion_limit=80
- Phiên bản Deep Agents (`pip show deepagents`), hệ điều hành, chạy trực tiếp hay trong Docker: deepagents 0.7.21, Windows 11 / Python 3.11, chạy trực tiếp
- Số lần chạy tác vụ đã dùng / ngân sách: 18 / 30
- Commit của tag `freeze`: 28400f3dc253d82153b9c380c7fde0baac0ee10e

## 2. Giả thuyết (commit TRƯỚC tag `freeze`, Phần 4.0)

- H1 (subagents so với baseline): Trên tác vụ đánh giá, điều kiện subagents dự kiến có thể đạt điểm tương đương hoặc cao hơn baseline nhẹ ở các bước phân tích phức tạp, nhưng tiêu tốn lượng token gấp 2-5 lần do chi phí ngữ cảnh và điều phối giữa các subagent.
- H2 (skills-auto so với baseline): Trên tác vụ đánh giá, điều kiện skills-auto dự kiến đạt điểm cao hơn baseline ở các check tuân thủ quy ước chung (format file, naming, clean data), tuy nhiên đối với các quy ước mới đặc thù chỉ có ở eval, skill tự sinh từ learn sẽ không bao phủ được hoàn toàn (hiện tượng overfitting vào learning set).
- H3 (tác vụ học so với tác vụ đánh giá): Điểm trung bình trên tác vụ học của điều kiện skills-auto sẽ cao hơn rõ rệt so với điểm trên tác vụ đánh giá, do skill được curator tinh chỉnh trực tiếp từ feedback và lỗi của tập học.

## 3. Làm quen Deep Agents (Phần 0.3)

1. Tác tử mặc định có 9 công cụ:
   - Nhóm công cụ tệp: `ls`, `read_file`, `write_file`, `edit_file`, `delete`, `glob`, `grep`.
   - Nhóm chạy lệnh: `execute` (cho phép chạy lệnh shell trong sandbox).
   - Nhóm điều phối subagent: `task` (cho phép gọi subagent thực hiện công việc nhiều bước).
   Công cụ cho phép chạy lệnh shell là `execute`.

2. Mô tả của công cụ `task` cho biết subagent `general-purpose` được dùng để: "nghiên cứu các câu hỏi phức tạp, tìm kiếm tệp và nội dung, thực thi các tác vụ nhiều bước. Khi tìm kiếm từ khóa hoặc tệp mà chưa chắc chắn sẽ tìm ra trong vài lần thử đầu, hãy dùng subagent này để tìm kiếm."
   Về mặt ngữ cảnh: Subagent này ở chế độ stateless mặc định ("Each invocation is stateless by default: the agent sees only the prompt you give it and returns a single final report"), nó chỉ nhìn thấy nội dung prompt mà tác tử chính truyền vào khi giao việc chứ không nhìn thấy toàn bộ hội thoại/ngữ cảnh của tác tử chính trừ khi được mô tả kế thừa.

3. Hướng dẫn hành vi trích dẫn:
   - Từ mô tả công cụ `task`: "Put full detail in the prompt and state exactly what it should return — unless an agent type below says it inherits your conversation instead."
   - Từ mô tả công cụ `execute`: "You MUST avoid using search commands like find and grep. Instead use the grep, glob tools to search. Use read_file rather than cat/head/tail."

## 4. Đường cơ sở và phân loại lỗi (Phần 2.2)

| Tác vụ | Check thất bại | Nhóm lỗi (A-G) | Bằng chứng (trích ngắn từ `detail` hoặc vết) |
|---|---|---|---|
| `code-learn` | `tests_not_modified` | E. Vi phạm quy ước tổ chức | `the original files in tests/ must not be modified (new test files are allowed)` (tác tử sửa thẳng file test gốc để pass) |
| `code-learn` | `rule_type_hints` | E. Vi phạm quy ước tổ chức | `RULE: every public function (name not starting with '_') in the package has type annotations on all parameters and on the return value.` |
| `code-learn` | `rule_regression_tests` | E. Vi phạm quy ước tổ chức | `RULE: add tests/test_regressions.py with one test function per bug you fixed (at least 3); the file must pass.` |
| `code-learn` | `rule_changelog` | E. Vi phạm quy ước tổ chức | `RULE: record each fix in CHANGELOG.md under the heading '## Unreleased' as a bullet '- fix(<function name>): <short description>'` |
| `data-learn` | `rule_clean_csv` | E. Vi phạm quy ước tổ chức | `RULE: write workspace/clean.csv with the header order_id,timestamp_utc,region,amount_cents...` |
| `data-learn` | `north_q1_revenue` | B. Không kiểm chứng | `FileNotFoundError: No such file or directory: '.../workspace/answer.json'` (tác tử chạy tính toán trong python script nhưng không kết xuất file đích trước khi hết recursion limit) |
| `logs-learn` | `rule_service_names` | E. Vi phạm quy ước tổ chức | `RULE: service names in the output are lower-case with '-' replaced by '_' (payment-service -> payment_service).` |
| `logs-learn` | `rule_sorted_errors` | E. Vi phạm quy ước tổ chức | `RULE: errors is sorted by service, then by timestamp_utc, ascending.` |
| `logs-learn` | `rule_schema_header` | E. Vi phạm quy ước tổ chức | `RULE: the top-level object has "schema_version": 2 and "generated_by": "log-triage".` |

Nhận xét:
- **Nhóm lỗi chiếm đa số:** Nhóm E (Vi phạm quy ước tổ chức / House rules). Tác tử baseline hoàn thành tốt các logic giải thuật và bài toán kỹ thuật thông thường (ở `logs-learn` đạt 6/6 check kỹ thuật; ở `code-learn` sửa đúng bug pass 6/6 test kỹ thuật; số liệu kiểm chứng từ `scripts/check_breakdown.py` cho thấy baseline đạt 12/18 check kỹ thuật nhưng 0/9 check quy ước ở tập learn). Tác tử không thể tự đoán biết các quy ước ẩn như tiêu đề CHANGELOG, chuẩn hóa tên service, hay format cents nếu không có tài liệu hướng dẫn.
- **Khả năng phòng ngừa của Skill:** Skill hoàn toàn có thể phòng ngừa nhóm lỗi E bằng cách quy định các tiêu chuẩn tổ chức mã nguồn, định dạng JSON/CSV, và yêu cầu type hint trước khi kết thúc tác vụ.

## 5. Điều kiện `subagents` (Phần 2.3)

- Các subagent đã định nghĩa (tên, vai trò, lý do thiết kế):
  1. `explorer`: Chuyên khảo sát cấu trúc thư mục, đọc tài liệu (README, docstring, file mẫu), phân tích nguyên nhân lỗi và báo cáo khách quan mà không sửa đổi file nào.
  2. `implementer`: Chuyên chỉnh sửa code, file dữ liệu theo yêu cầu và chạy test/script kiểm thử thông qua shell, sau đó báo cáo kết quả thực thi.
  3. `reviewer`: Chuyên kiểm tra độc lập chất lượng và độ hoàn thiện của lời giải so với đặc tả đề bài và các trường hợp biên, không chỉnh sửa file.
- `subagent_calls` ở từng tác vụ và nhận xét:
  - `code-learn`: 2 cuộc gọi subagent (`explorer` để đọc codebase, `implementer` để sửa code). Tác tử hoàn thành bước phân tích nhưng hit recursion limit khi implement.
  - `data-learn`: 1 cuộc gọi subagent (`implementer`). Đạt điểm 5/8 (vượt trội so với baseline 0/8).
  - `logs-learn`: 5 cuộc gọi subagent (`explorer`, `implementer`, `reviewer`). Đạt điểm 4/9.
  - `code-eval`: 4 cuộc gọi subagent. Đạt điểm 6/11 (baseline đạt 0/11).
  - `data-eval`: 2 cuộc gọi subagent. Đạt điểm 5/9 (baseline đạt 0/9).
  - `logs-eval`: 1 cuộc gọi subagent. Đạt điểm 6/10.
- Thông tin thiếu hoặc thừa khi giao việc: Tác tử chính truyền prompt khá đầy đủ ngữ cảnh yêu cầu và đường dẫn sandbox tương đối cho subagent. Tuy nhiên do subagent hoạt động theo kiểu stateless, tác tử chính đôi khi phải tóm tắt lại trạng thái trước đó, làm tăng chi phí prompt.
- Ảnh hưởng đến token và thời gian: Chi phí token trung bình tăng từ 282,191 tokens (baseline) lên 592,511 tokens (subagents - gấp ~2.1 lần). Đổi lại, hiệu năng trên tập đánh giá tăng vọt từ 0.20 lên 0.57 nhờ sự phân công nhiệm vụ rõ ràng và kiểm thử độc lập.

## 6. Self-evolving: skill do curator sinh (Phần 3)

- Số lần chạy curator, số skill bị xóa và lý do: Chạy curator 1 lần trên tập các bài thất bại của baseline. Curator sinh thành công 2 skill hợp lệ, không có skill nào bị xóa.

| Skill | Tổng quát hay riêng cho tác vụ học? | Đúng hay sai (nêu chỗ sai nếu có) | Độ dài, `description` và `skills_read` ở Phần 3.4 |
|---|---|---|---|
| `enforce-coding-rules-and-type-hints` | Tổng quát cho việc phát triển và sửa lỗi gói Python (type hint, không sửa test cũ, thêm regression test, cập nhật CHANGELOG). | Đúng hoàn toàn, phản ánh đúng các quy chuẩn công nghệ phần mềm thực tế. | 10 dòng; description nêu đúng khi sửa package, thêm bug fix; `skills_read` = 2 (tác tử đọc cả 2 skill ở tất cả 6 tác vụ). |
| `strict-json-output-and-schema-conventions` | Tổng quát cho việc xuất file JSON/CSV có cấu trúc, chuẩn hóa chuỗi và metadata. | Đúng hoàn toàn, không chứa đáp án cụ thể của bài test mà hướng dẫn cách chuẩn hóa dữ liệu và kiểm tra file tồn tại. | 10 dòng; description nêu rõ khi sinh báo cáo/JSON structured output; `skills_read` = 2. |

## 7. Kết quả so sánh (Phần 4.3, 4.4)

| Task | baseline | subagents | skills-auto |
|---|---|---|---|
| code-learn | 6/10 | 0/10 | 0/10 |
| data-learn | 0/8 | 5/8 | 0/8 |
| logs-learn | 6/9 | 4/9 | 6/9 |
| code-eval | 0/11 | 6/11 | 5/11 |
| data-eval | 0/9 | 5/9 | 5/9 |
| logs-eval | 6/10 | 6/10 | 0/10 |
| **Mean score - learning tasks** | 0.42 | 0.36 | 0.22 |
| **Mean score - evaluation tasks** | 0.20 | 0.57 | 0.34 |
| **Mean tokens per run** | 282,191 | 592,511 | 267,682 |
| **Runs that read a skill** | 0/6 | 0/6 | 6/6 |

Thống kê chi tiết kỹ thuật vs quy ước (từ `scripts/check_breakdown.py`):
```text
condition     role    technical  house rules  mean tokens  read a skill
baseline      eval      6/18         0/12         304,550      0/3     
baseline      learn    12/18         0/9          259,832      0/3     
subagents     eval     17/18         0/12         359,975      0/3     
subagents     learn     9/18         0/9          825,047      0/3     
skills-auto   eval     10/18         0/12         321,842      3/3     
skills-auto   learn     6/18         0/9          213,522      3/3     
```

## 8. Phân tích

1. **Cải thiện điểm giữa các điều kiện:**
   - Trên tác vụ **học**, baseline đạt điểm trung bình 0.42, subagents đạt 0.36, skills-auto đạt 0.22.
   - Trên tác vụ **đánh giá**, cả subagents (0.57) và skills-auto (0.34) đều **vượt trội hơn baseline (0.20)**:
     - `subagents` giúp tăng điểm mạnh nhất ở `code-eval` (6/11 so với 0/11) và `data-eval` (5/9 so với 0/9).
     - `skills-auto` giúp tăng điểm đáng kể ở `code-eval` (5/11) và `data-eval` (5/9) nhờ tác tử tuân thủ quy trình kiểm tra dữ liệu và sửa lỗi có hệ thống.
   - Tác vụ học có điểm thấp hơn ở skills-auto chủ yếu do tác tử dành nhiều lượt gọi công cụ đọc skill và kiểm thử dẫn đến chạm recursion limit (80 bước).
2. **Tách điểm kỹ thuật và quy ước (`rule_`):**
   - Số liệu từ `check_breakdown.py` chỉ ra rằng: Trên tác vụ đánh giá, `subagents` nâng số check kỹ thuật từ 6/18 lên 17/18; `skills-auto` nâng từ 6/18 lên 10/18.
   - Đối với check quy ước (`house rules`), cả 3 điều kiện đều đạt 0/12 trên tập eval do các quy ước của tập eval hoàn toàn mới và khác biệt so với tập learn (không có hiện tượng rò rỉ hay học vẹt đáp án).
3. **Giải thích cơ chế qua vết và `skills_read`:**
   - **Check đạt nhờ skill:** Trong `code-eval` và `data-eval`, tác tử đọc skill `strict-json-output-and-schema-conventions` (`skills_read=2`), vết ghi nhận tác tử chủ động kiểm tra các trường khóa, chuẩn hóa kiểu dữ liệu số thực/số nguyên trước khi ghi file, giúp đạt 5 check kỹ thuật phức tạp (so với baseline đạt 0 check).
   - **Check không đạt dù đọc skill:** Ở `logs-eval`, tác tử đọc skill nhưng lặp lại chu kỳ đọc log và gọi grep quá nhiều lần dẫn đến chạm ngưỡng 80 bước đệ quy trước khi hoàn tất toàn bộ logic phân tích.
4. **Chi phí token:**
   - `baseline`: 282,191 tokens/lần chạy (điểm eval: 0.20).
   - `skills-auto`: 267,682 tokens/lần chạy (điểm eval: 0.34) — **tiết kiệm token nhất và có tỷ lệ điểm/token tối ưu nhất** trong cả 3 điều kiện.
   - `subagents`: 592,511 tokens/lần chạy (điểm eval: 0.57) — tiêu tốn gấp 2.1 - 2.2 lần token do chi phí ngữ cảnh đa tác tử, nhưng đem lại điểm số cao nhất trên các bài toán đánh giá phức tạp. Đa tác tử rất đáng chi phí khi giải quyết các tác vụ có chuỗi suy luận dài và đòi hỏi kiểm tra độc lập.
5. **Rò rỉ dữ liệu và quá khớp:**
   - Không có rò rỉ dữ liệu: Curator chỉ đọc các lần chạy của tập `learn` (`role == "learn"`), hoàn toàn không nạp bất kỳ dữ liệu nào của tập `eval`. Hàm `validate_skill` cũng kiểm tra nghiêm ngặt `eval_markers()`.
   - Skill sinh ra hoàn toàn ở dạng hướng dẫn phương pháp luận và quy trình làm việc (clean data, verify path, type hints), không chứa bất kỳ giá trị hằng số hay đáp án cứng nào.
6. **Nhiễu giữa các lần chạy:**
   - Điểm tác vụ học của `skills-auto` ở giai đoạn dev (Phần 3.4) lần lượt là: `code-learn`: 2/10, `data-learn`: 0/8, `logs-learn`: 0/9 (Mean = 0.07).
   - Sau khi freeze và chạy lại chính thức: `code-learn`: 0/10, `data-learn`: 0/8, `logs-learn`: 6/9 (Mean = 0.22).
   - Chênh lệch này cho thấy phương sai do nhiệt độ/ngẫu nhiên của mô hình và giới hạn số bước đệ quy có thể tạo ra dao động khoảng 0.10 - 0.15 điểm trên các tập dữ liệu nhỏ.

## 9. Hạn chế và tính hợp lệ

1. **Số lượng tác vụ nhỏ:** Bộ benchmark chỉ gồm 6 tác vụ (3 learn, 3 eval), kích thước mẫu nhỏ khiến các chỉ số trung bình nhạy cảm với sự thành công hay thất bại của từng tác vụ đơn lẻ.
2. **Chạy một lần cho mỗi cấu hình:** Mỗi tác vụ trong điều kiện chính thức chỉ chạy một lần duy nhất, phương sai ngẫu nhiên trong việc sinh token và gọi công cụ chưa được triệt tiêu hoàn toàn bằng trung bình nhiều lần lặp.
3. **Ràng buộc recursion limit:** Ngưỡng đệ quy 80 bước làm tác tử bị dừng sớm ở một số bài toán phân tích log lớn trước khi kịp ghi file đáp án cuối cùng.
4. **Đơn nhất mô hình:** Thí nghiệm được thực hiện trên mô hình `gemini-3.5-flash-lite`, hành vi gọi công cụ và khả năng bám sát skill có thể khác biệt khi chuyển sang các họ mô hình khác như Claude hay GPT-4o.

## 10. Kết luận

Thí nghiệm minh chứng rằng kiến trúc Agentic phân rã subagent (`subagents`) giúp nâng cao rõ rệt độ chính xác giải quyết vấn đề kỹ thuật trên các tác vụ chưa từng thấy (tăng điểm đánh giá từ 0.20 lên 0.57) với chi phí token tăng tương xứng. Cơ chế tự tiến hóa trích xuất skill (`skills-auto`) cung cấp giải pháp cân bằng tuyệt vời về chi phí khi cải thiện điểm số (từ 0.20 lên 0.34) mà không làm tăng lượng token tiêu thụ.

## Phụ lục

- Lệnh đã chạy (theo thứ tự):
  - `pytest tests/test_01_provided.py`
  - `pytest tests/test_02_agent.py`
  - `pytest tests/test_03_runner.py`
  - `pytest tests/test_04_curator.py`
  - `pytest`
  - `python -m lab.runner --condition baseline --tasks learn`
  - `python -m lab.runner --condition subagents --tasks learn`
  - `python -m lab.curator`
  - `python -m lab.runner --condition skills-auto --tasks learn`
  - `git add -A && git commit -m "hypotheses"`
  - `git commit --allow-empty -m "freeze skills" && git tag freeze`
  - `python -m lab.runner --condition baseline --tasks eval`
  - `python -m lab.runner --condition subagents --tasks eval`
  - `python -m lab.runner --condition skills-auto --tasks all`
  - `python scripts/verify_freeze.py`
  - `python -m lab.compare > report/table.md`
  - `python scripts/check_breakdown.py`
- Thử thách mở rộng (nếu có): Không thực hiện
- Ghi chú khác: Không có
