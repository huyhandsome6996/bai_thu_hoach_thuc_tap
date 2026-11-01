# Kết quả QA và các điều kiện bàn giao

Ngày chốt: 01/11/2026. Phạm vi phiên này là khảo sát, tái cấu trúc, trích xuất và thiết kế; chưa viết bài thu hoạch chính thức hoặc tạo Word cuối.

**Cập nhật theo xác nhận của người dùng:** hồ sơ Hồ Quang Huy đã được điền; đầu ra Word .docx, đúng lớp 12/2; chưa dự giờ chuyên môn/chủ nhiệm (0+0). Bản chính phải đúng FORM gốc và có 30–35 trang; cấu trúc C/D/E/F và phương án khoảng 40 trang trước đây được thay thế. Đọc `confirmed_week1_activities.md` để dùng bốn nhóm hoạt động đã xác nhận.

## Nguồn và tính toàn vẹn

Đã di chuyển 9 tệp Office vào `01_raw_data/`; tên và byte gốc giữ nguyên, có SHA-256 trong `raw_manifest.json`. `PROMPT_CHO_QA_AGENT.md` giữ ở gốc làm yêu cầu gốc, không phải nguồn thực chứng. README được cập nhật để chỉ đường.

DOCX đọc bằng OOXML; XLSX đọc tất cả ô có dữ liệu, giữ địa chỉ ô, vùng gộp, giá trị cache và biểu thức. Hai tệp DOC cũ được Word mở read-only rồi SaveAs2 thành bản sao DOCX trong `04_scripts/extracted_sources/`; raw không đổi. Các mã P/T định vị theo thứ tự đoạn/bảng trong body XML, không phải số trang Word. Bản sao DOCX và Markdown trích xuất là trung gian, không phải bài nộp.

Bảy tệp tri thức chứa tổng hợp có cảnh báo và kho đoạn/bảng nguồn để tra lại. Bảng gộp phức tạp được giữ dạng ô C1… ở phần nguồn; bảng học tập/rèn luyện và danh sách 46SV đã chuẩn hóa riêng để dùng. Các ô gộp dọc GVHD trong danh sách SV được triển khai theo vMerge, ghép hai bảng bằng tên+ngày sinh. Excel giữ nguyên ô nguồn; nhóm công tác GV được nối đến dòng tên kế tiếp, không lấy68dòng công tác làm68GV.

Đã xem bảng ảnh tổng hợp8ảnh nhúng:6ảnh trong báo cáoĐoàn (đội bóng,văn nghệ,trao giải thể thao,ngày hội,cuộc thi biểu diễn,kết nạp Đoàn),2ảnh trong bìa (khung viền và logo). Đây là minh họa trong tài liệu gốc, không chứng minh người dùng tham gia hay xác nhận niên đại sự kiện. Chưa OCR/nhận dạng người hoặc suy thành tích từ ảnh. Ảnh gốc nhúng được tách vào cache, có `media_inventory.json`; khi cần tái tạo bìa dùng đúng ảnh gốc.

Phạm vi trích xuất văn bản là body và bảng Office; chưa kiểm tra bố cục từng trang của9nguồn, header/footer, bình luận, revision hoặc đối tượng nhúng ngoài body. Không gọi dữ liệu ảnh là bảng số đã số hóa. Kết quả chuyển DOC dùng nội dung Word đọc được; cần mở nguồn gốc nếu kiểm tra định dạng/chữ ký hoặc nội dung có tranh chấp.

## Phát hiện ảnh hưởng trực tiếp nội dung

| Vấn đề | Kết luận từ tài liệu | Cách xử lý |
| --- | --- | --- |
| Hai STT của46SV | Bảng chuyên môn khác thứ tự bảng chủ nhiệm | STT không ghi hệ thì mặc định chuyên môn; tra theo tên+ngày sinh |
| Ví dụ Nguyễn Trọng Lộc trong prompt cũ | CM17,CN11;CM Hồ Đắc Thái Sơn+Nguyễn Thị Hiền,CN Trần Ngọc Đức Toàn | Không dùng STT11 như CM hoặc gán nhầm GVHD |
| Tốt nghiệp100% | Có trong chỉ tiêu năm mới, chưa có kết quả2026 | Không biến mục tiêu thành thành tích |
| ĐỗĐH,kiểm định2,chuẩn quốc gia1 | Chưa có số liệu/quyết định xác nhận trong nguồn | Ghi thiếu nguồn; không tự đưa vào bài |
| Quy mô lớp | 12lớp/302HS cuối2025–2026;13lớp/346HS đầu2026–2027 | Bảng so sánh phải có niên độ và mốc |
| Phân loại và danh hiệu | Học tậpTốt104,HSXS10,HSG92 | Không đồng nhất ba khái niệm |
| Đoàn | 107ĐVHS và10ĐVGV;8chi đoàn | Không gọi107là tổng đoàn viên;không coi8chi đoàn bằng13lớp |
| Excel Toán79 | Tổng gồm công tác kiêm nhiệm | Không gọi79là tiết đứng lớp riêng |
| Excel Vật lý24 | SUM đúng phạm vi29–36 nhưng bỏ dòng28có3tiết | Nêu phạm vi,cần xác nhận tổng bao quát27 |
| Excel Địa lí17 | SUM đúng phạm vi80–82 nhưng bỏ dòng83có5tiết | Nêu phạm vi,cần xác nhận tổng bao quát22 |
| Học vị GV khác giữa các dòng | Trần Văn Dũng và Hoàng Đức Vương có Cử nhân/Thạc sĩ ở hai nhóm | Giữ cảnh báo,không tự chọn học vị |
| Số văn bản giáo dục | ĐầuKH145/KH-THPT,kèmQĐ145/QĐ-THPT ngày15/9/2026 | Dẫn đúng loại văn bản và vị trí |
| QĐ2760 | Chỉ có tệp phụ lục,không có toàn văn quyết định | Không tự thêm ngày ký hoặc khẳng định hiệu lực |
| KHBD5512 vàAI | HT yêu cầu thêm năng lực số/AI | Không quy yêu cầuAI thành nguyên vănCV2020 |
| PL6 QĐ2760 | Kế hoạch công tác thực tập giảng dạy theo tuần | Không gọiPL6là giáo án5512 |
| Nội dung FORM | A,B.I–III,tổng kết,nhận xét;hai mụcIVtrùng | Bám đúng thứ tự nguồn; sửa số IV cuối thành V nếu GVHD không yêu cầu nguyên xi; không dùng C/D/E/F làm phần chính |
| Hạn nộp khác nhau | 02/11thực tếGD;17/11giảng dạy/CN;18/11GVHD;21/11tổng kết | Không yêu cầu hoàn thành7+3tiết trước02/11 |

## Chiến lược số trang

Blueprint hiện tại có từng trang 1–35 theo FORM gốc, chấp nhận bản render trong khoảng 30–35 trang, không tự vượt 35. Không bắt buộc chèn KHBD toàn văn và hồ sơ 7+3 tiết vào bài tìm hiểu thực tế giáo dục tuần 1. Mục cuối là nhận xét BGH theo mẫu. Chưa có Word render nên đây là mục tiêu thiết kế, không phải số trang đã nghiệm thu.

## Thông tin cá nhân còn chờ

Hồ sơ cốt lõi đã đủ: tên, MSSV, ngày sinh, ngành/trường, lớp sinh viên **Tin3A**, quê quán ghi **Sa Pa, Lào Cai**, lớp thực tập **12/2**, Word .docx và hai GVHD **Mai Xuân Văn / Nguyễn Thị Thu Phương** đều được người dùng xác nhận. Ngày **26/10/2026**, đã dự chào cờ buổi đầu, gặp thầy Văn **09:45**, gặp cô Phương **10:30**; giờ thực tế khác lịch dự kiến không phải lỗi dữ liệu. Bốn nhóm hỗ trợ đầu giờ/văn nghệ/trò chơi vẫn xác nhận ở mức tuần, chưa có ngày cụ thể. Chưa dự giờ chuyên môn/chủ nhiệm (0+0). Chưa xác nhận tham gia nghe báo cáo BGH/Đoàn trường; không cần chặn viết bài vì có thể dẫn nội dung từ tài liệu. Tên bài KHBD chỉ cần khi chuẩn bị tài liệu chuyên môn riêng. Không hỏi lại dữ liệu đã xác nhận.

## Kiểm tra có thể tái lập

Chạy `python 04_scripts/validate_repository.py`. Kết quả máy đọc ở `validation_results.json`:9hash gốc,9cặp trích xuất,46khóaSV/hai bộSTT,12lớp/302HS,tổng từng lớp và từng mức,10HSXS/92HSG,346HS/13lớp,7tệpKB,35dòng phân trang,H4outline,cácSUMcache đơn giản. Chỉ kiểm tra dữ liệu repository; không thay QA nội dung,pháp lý hiện hành hoặc phân trang bản nộp.
