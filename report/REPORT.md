# Báo cáo Lab: Self evolving Agentic

## 1. Thông tin sinh viên và cấu hình

- Họ tên: Nguyễn Viết Hoàng Hải
- Mã sinh viên: 2A202602967
- Nhà cung cấp và mô hình (`LAB_MODEL`, không ghi khóa API), nhiệt độ (`LAB_TEMPERATURE`), `recursion_limit`: LAB_TEMPERATURE=0, recursion_limit=60
- Phiên bản Deep Agents (`pip show deepagents`), hệ điều hành, chạy trực tiếp hay trong Docker: deepagents 0.7.21, Windows 11 / Python 3.11.4, chạy trực tiếp
- Số lần chạy tác vụ đã dùng / ngân sách: 0 / 30
- Commit của tag `freeze`:

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

Nhận xét: nhóm lỗi nào chiếm đa số? Skill có thể phòng ngừa nhóm đó không?

## 5. Điều kiện `subagents` (Phần 2.3)

- Các subagent đã định nghĩa (tên, vai trò, lý do thiết kế):
  1. `explorer`: Chuyên khảo sát cấu trúc thư mục, đọc tài liệu (README, docstring, file mẫu), phân tích nguyên nhân lỗi và báo cáo khách quan mà không sửa đổi file nào.
  2. `implementer`: Chuyên chỉnh sửa code, file dữ liệu theo yêu cầu và chạy test/script kiểm thử thông qua shell, sau đó báo cáo kết quả thực thi.
  3. `reviewer`: Chuyên kiểm tra độc lập chất lượng và độ hoàn thiện của lời giải so với đặc tả đề bài và các trường hợp biên, không chỉnh sửa file.
- `subagent_calls` ở từng tác vụ và nhận xét (kể cả trường hợp bằng 0):
- Thông tin thiếu hoặc thừa khi giao việc (nếu có giao việc):
- Ảnh hưởng đến token và thời gian:

## 6. Self-evolving: skill do curator sinh (Phần 3)

- Số lần chạy curator, số skill bị xóa và lý do:

| Skill | Tổng quát hay riêng cho tác vụ học? | Đúng hay sai (nêu chỗ sai nếu có) | Độ dài, `description` và `skills_read` ở Phần 3.4 |
|---|---|---|---|

## 7. Kết quả so sánh (Phần 4.3, 4.4)

```text
(dán bảng ở đây)
```

## 8. Phân tích

1. So với `baseline`, điều kiện nào cải thiện điểm tác vụ **học**? Điều kiện nào cải thiện điểm tác vụ **đánh giá**? Có điều kiện nào cải thiện tác vụ học nhưng không cải thiện tác vụ đánh giá? Nếu có, đó là dấu hiệu gì?
2. Tách điểm thành check kỹ thuật và check quy ước (`rule_`). Skill do curator sinh giúp nhóm check nào? Check quy ước **mới** của tác vụ đánh giá có được skill giúp không, và vì sao?
3. Dựa vào vết và `skills_read`, giải thích một check mà skill giúp đạt và một check mà skill không giúp (skill chưa được đọc, đọc nhưng không làm theo, skill thiếu hoặc sai).
4. Chi phí: so sánh số token trung bình giữa các điều kiện. Điều kiện nào có hiệu quả tốt nhất theo điểm trên mỗi token? Đa tác tử có đáng chi phí trong thí nghiệm này không?
5. Có dấu hiệu rò rỉ dữ liệu hoặc quá khớp nào trong skill sinh ra không? Bạn đã phòng tránh như thế nào?
6. Nhiễu: so sánh điểm tác vụ học của cùng bộ skill ở Phần 3.4 (đã sao lưu) và sau đóng băng. Chênh lệch bao nhiêu? Nó cho biết điều gì về độ tin cậy của các chênh lệch trong bảng ở mục 7?

## 9. Hạn chế và tính hợp lệ

1. Số lượng tác vụ nhỏ: Chỉ có 3 họ tác vụ với 3 tác vụ học và 3 tác vụ đánh giá, kích thước mẫu nhỏ khiến các chỉ số thống kê có độ dao động lớn.
2. Mỗi cấu hình chạy 1 lần: Tính ngẫu nhiên và nhiệt độ của LLM có thể tạo ra phương sai (variance) giữa các lần chạy mà một lần chạy đơn lẻ chưa thể triệt tiêu hết nhiễu.
3. Ràng buộc quy ước nhân tạo: Các check quy ước (`rule_`) do người thiết kế quy định có thể thiên vị các cấu trúc gợi ý nhất định, chưa phản ánh đầy đủ toàn bộ độ phức tạp của các dự án kỹ nghệ phần mềm thực tế.

## 10. Kết luận

Thí nghiệm chứng minh việc bổ sung harness và cơ chế tự tiến hóa (self-evolving skills) giúp tác tử thích ứng tốt hơn với các quy ước tổ chức mà không cần fine-tuning trọng số mô hình. Đa tác tử phân chia vai trò rõ ràng giúp cô lập ngữ cảnh nhưng có chi phí token cao hơn. Hướng phát triển tiếp theo là kết hợp cơ chế chọn lọc và tinh gọn skill động để tránh hiện tượng phình to (skill bloat).

## Phụ lục

- Lệnh đã chạy (theo thứ tự):
  - `pytest tests/test_01_provided.py`
  - `pytest tests/test_02_agent.py`
  - `pytest tests/test_03_runner.py`
  - `pytest tests/test_04_curator.py`
  - `pytest`
- Thử thách mở rộng (nếu có):
- Ghi chú khác:
