# Quy tắc làm việc cho Coding Agent

Áp dụng cho toàn bộ repository. Đọc file này trước khi viết hoặc xuất bản bài thu hoạch. Yêu cầu trực tiếp mới nhất của người dùng được ưu tiên khi có thay đổi.

## Nhiệm vụ và điểm bắt đầu

Viết hoặc sửa bài **tìm hiểu thực tế giáo dục TTSP1 sau tuần thực tập đầu tiên**, dựa trên dữ liệu đã chuẩn hóa. Đã có bài cá nhân hóa trong `05_final_report/`, được kiểm tra và sửa từ commit `36ea69e`; đọc `qa_report.md` và `qa_checks.json` trước khi thay đổi. Không tạo lại blueprint để ghi đè bài đã biên soạn.

Thứ tự đọc:

1. `00_meta/report_context.json` và `00_meta/student_profile.json`.
2. `00_meta/qa_findings.md` để biết dữ liệu chưa có nguồn hoặc bất nhất.
3. `03_report_blueprint/prompt_for_coding_agent.md` để triển khai.
4. `03_report_blueprint/pagination_strategy.md` và `master_outline_detailed.md` cùng thư mục.
5. Phần tổng hợp của bảy tệp trong `02_extracted_knowledge/`; chỉ đọc thêm các đoạn nguồn cần cho phần đang viết.

## Mốc thời gian bắt buộc

- Toàn đợt TTSP1: **26/10/2026–21/11/2026**.
- Phạm vi trải nghiệm được phép phản ánh trong bài này: **tuần 1, 26/10–01/11/2026**, và chỉ những hoạt động người dùng xác nhận đã tham gia.
- Mốc chốt tìm hiểu: **01/11/2026**. Hạn nộp bài tìm hiểu thực tế giáo dục: **02/11/2026**.
- Đây không phải báo cáo tổng kết bốn tuần. Không tự thay mốc chốt bằng ngày máy tính khi chạy agent vào ngày khác. Ngày ký/ngày nộp thực tế cần người dùng xác nhận, không tự ký lùi ngày.
- Tuần 2: 02–08/11; tuần 3: 09–15/11; tuần 4: 16–21/11. Công việc các tuần này chỉ được viết ở dạng **dự kiến, kế hoạch, phương hướng** nếu người dùng chưa cập nhật phạm vi bài.
- Hạn **17/11** là hồ sơ giảng dạy/chủ nhiệm cuối đợt; **18/11** là hạn đánh giá của GVHD; **14h ngày 21/11** là tổng kết. Không coi những sự kiện này đã xảy ra trong bài tuần 1.
- **7 tiết chuyên môn + 3 tiết chủ nhiệm/HĐTN-HN là yêu cầu cả đợt**, không phải số tiết đã hoàn thành tuần 1. Không tự tạo ngày dự, lớp, tên bài, lời nhận xét hoặc chữ ký. SP Công nghệ có cơ cấu 4 tiết công nghiệp + 3 tiết nông nghiệp.

Ví dụ cách diễn đạt:

| Trường hợp | Cách viết phù hợp |
| --- | --- |
| Mới có lịch đón đoàn | “Theo kế hoạch, sinh viên được bố trí nghe báo cáo…” |
| Người dùng xác nhận đã nghe báo cáo | “Trong tuần đầu, em đã nghe báo cáo…” |
| Sắp dự các tiết còn lại | “Trong các tuần tiếp theo, em dự kiến…” |
| Chưa có trải nghiệm, chỉ có tài liệu | “Qua nghiên cứu kế hoạch giáo dục nhà trường…” |
| KHBD tự thiết kế cho phụ lục | “KHBD đề xuất, chưa triển khai thực tế” |

## Trung thực dữ liệu và cá nhân hóa

- Hồ sơ hiện tại: **Hồ Quang Huy**, MSSV **24S1020030**, sinh **25/02/2006**, ngành **Sư phạm Tin học**, lớp thực tập chủ nhiệm **12/2**. Không đổi thành 12A2. Đầu ra đã chọn: **Word .docx**. Đọc `00_meta/confirmed_week1_activities.md` để dùng lời kể đã chuẩn hóa.
- Đã xác nhận bổ sung: lớp sinh viên **Tin3A**, quê quán ghi **Sa Pa, Lào Cai**; GVHD chuyên môn **thầy Mai Xuân Văn**, GVHD chủ nhiệm **cô Nguyễn Thị Thu Phương**. Không hỏi lại những mục này. Ngày **26/10/2026**, sinh viên dự chào cờ buổi đầu, gặp thầy Văn lúc **09:45**, gặp cô Phương lúc **10:30**. Đây là giờ thực tế người dùng kể, không thay bằng lịch dự kiến trong tài liệu. Chưa xác nhận nghe báo cáo BGH/Đoàn trường.
- Đến hết 01/11/2026, người dùng xác nhận **0 tiết dự giờ chuyên môn, 0 tiết dự giờ chủ nhiệm**. Hỗ trợ 15 phút đầu giờ, làm một video, hỗ trợ tập văn nghệ và hai trò chơi là hoạt động đã tham gia; không quy đổi thành tiết dự giờ hoặc nhận đã dùng AI.
- Rà chính tả và viết hoa thống nhất: Hồ Quang Huy; Sa Pa; Lào Cai; Sư phạm Tin học; Trường Đại học Sư phạm, Đại học Huế; Trường THPT Thuận Hóa; lớp 12/2. Không viết “chủ nghiệm”, “biễu diên”, “SaPa”. Không tự xác nhận địa giới hành chính hiện hành từ tên địa danh người dùng nêu.

- Trường `null` trong hồ sơ là chưa biết. Hỏi thông tin còn thiếu; vẫn viết các phần chung độc lập. Không tự đoán họ tên, MSSV, lớp, quê quán, môn học hoặc GVHD.
- Nếu người dùng cung cấp STT, mặc định tra bảng **chuyên môn** và nói rõ quy ước. Hai bảng chuyên môn/chủ nhiệm có thứ tự khác nhau; dùng `00_meta/student_roster.json` đã ghép theo tên và ngày sinh.
- Tài liệu kế hoạch không chứng minh hoạt động đã hoàn thành; ảnh trong báo cáo Đoàn không chứng minh sinh viên có mặt. Nhật ký chỉ được dựng từ thông tin người dùng xác nhận, phần còn lại là mẫu trống hoặc kế hoạch có nhãn.
- Phân biệt số liệu kết quả **2025–2026** và chỉ tiêu/kế hoạch **2026–2027**. Đặc biệt không viết chỉ tiêu tốt nghiệp 100% thành kết quả tốt nghiệp 2026.
- Mỗi bảng số liệu phải có nguồn, niên độ và vị trí P/T hoặc sheet/ô. Không dùng ví dụ trong prompt yêu cầu gốc thay số liệu tài liệu.
- Không bịa tỷ lệ đỗ đại học, chứng nhận kiểm định, lịch sử trường hoặc số liệu giáo dục toàn thành phố. Tham khảo các khoảng trống trong QA findings.
- Không tự điền nhận xét, điểm, chữ ký hoặc con dấu của BGH/GVHD. Nội dung minh họa phải có nhãn, không gọi là minh chứng thực tế.

## Cấu trúc và thể thức

- Theo yêu cầu mới nhất, bám **đúng thứ tự FORM gốc**: A; B.I; B.II.1–6; B.III; tổng kết; nhận xét BGH. Không tạo C/D/E/F như phần chính. Tích hợp chuyên môn/chủ nhiệm/bài học vào mục thích hợp của FORM. Sửa hai mục IV trùng thành IV/V chỉ để thống nhất số thứ tự, giữ tên và vị trí nội dung.
- **Bản Word nộp phải có 30–35 trang vật lý A4**, mục tiêu 35. Không dùng phương án khoảng 40 trang trước đây. Không thêm KHBD toàn văn hoặc toàn bộ hồ sơ 7+3 tiết vào bản này để làm sai phạm vi; tài liệu chuẩn bị chuyên môn riêng chỉ soạn khi có yêu cầu. Phải điều chỉnh nội dung và kiểm tra bản render đến khi đạt giới hạn, không chỉ hứa số trang trong prompt.
- Times New Roman 13, chữ đen; Multiple 1.2; Before/After 0 pt; thụt đầu dòng 1–1,27 cm; căn đều. Lề trái 3 cm, trên/dưới/phải 2 cm. Số trang giữa footer nếu đánh số.
- KHBD bám cấu trúc CV 5512 và yêu cầu bổ sung năng lực số/AI của tài liệu hướng dẫn. Phụ lục 6 của bộ QĐ 2760 là kế hoạch công tác thực tập giảng dạy theo tuần, không phải mẫu KHBD.
- Chỉ xác nhận số trang Word sau khi cập nhật mục lục, render và kiểm tra mọi trang. Markdown không có số trang A4 cố định.

## Lưu trữ và điều kiện hoàn thành

- Không sửa hoặc xóa tệp trong `01_raw_data/`. Giữ nguyên thông tin cá nhân người dùng đã xác nhận khi chạy lại script.
- Viết từng phần vào `05_final_report/sections/`, ghép bản cuối theo định dạng người dùng chọn. Lưu tiến độ và nguồn; tránh nạp toàn kho tri thức vào một lượt.
- Còn thông tin bắt buộc chưa xác nhận thì đặt tên **DỰ THẢO** và liệt kê mục thiếu; không báo sẵn sàng nộp.
- Trước khi bàn giao, kiểm tra toàn bài có vô tình viết công việc sau 01/11 như đã hoàn thành hay không. Kiểm tra riêng các câu “đã hoàn thành”, “sau bốn tuần”, “kết thúc đợt”, “đã dự đủ”, các ngày 17/11–21/11 và lời nhận xét giả. Những cụm này chỉ hợp lệ khi dẫn tài liệu lịch sử hoặc được đặt rõ trong kế hoạch tương lai.
- Chạy `python 04_scripts/validate_repository.py` để kiểm tra dữ liệu bàn giao; kiểm tra thêm nội dung và bố cục bản bài viết. Script không xác minh trải nghiệm cá nhân hoặc số trang Word.
