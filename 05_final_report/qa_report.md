# QA report – bản nộp bài thu hoạch tìm hiểu thực tế giáo dục TTSP1

Ngày kiểm tra: 01/11/2026 (mốc quan sát tuần 1 được giữ theo `00_meta/report_context.json`, không dùng ngày máy của lần chạy sau). Người kiểm tra: coding agent dựng bài.

## 1. Sản phẩm bàn giao

| Tệp | Nội dung |
| --- | --- |
| `05_final_report/BAI_THU_HOACH_TTSP1_HO_QUANG_HUY.docx` | Bản nộp Word (định dạng yêu cầu), 35 trang vật lý A4 |
| `05_final_report/BAI_THU_HOACH_TTSP1_HO_QUANG_HUY.pdf` | Bản render kiểm tra hình thức (LibreOffice 25.2, cùng nguồn XML) |
| `05_final_report/sections/*.md` | 10 tệp phần viết riêng theo FORM, dùng để ghép bản Word |
| `05_final_report/source_map.md` | Ánh xạ [S01]–[S09] tới tệp gốc và quy ước dẫn nguồn |
| `04_scripts/build_docx_huy.py` | Script dựng .docx (python-docx, thể thức quy định) |
| `04_scripts/update_toc_uno.py` | Cập nhật mục lục/danh mục bảng bằng LibreOffice UNO |
| `04_scripts/qa_content_check.py` | Kiểm tra chuỗi cấm, dữ kiện bắt buộc, thông số lề |

## 2. Số trang thực đo

- Render PDF bằng LibreOffice: **35 trang A4** (pdfinfo: 595.304 × 841.89 pts), đúng mục tiêu 35, trong khoảng cho phép 30–35.
- Đếm gồm bìa (không đánh số) và trang nhận xét BGH; số trang hiển thị ở footer chính giữa từ trang 2 (lời cảm ơn) đến trang 35.
- Đã xem ảnh toàn bộ 35 trang (gộp 2×2) sau từng vòng chỉnh sửa; các lỗi phát hiện đều đã sửa và render lại:
  1. Thứ tự FORM sai (mục lục trước lời cảm ơn) → đã đưa về Bìa → Lời cảm ơn → Mục lục → A…V.
  2. Bảng "Danh mục tài liệu" còn ký tự `|` do thiếu nhãn bảng → đã thêm nhãn, thành Bảng 12.
  3. Cột GVCN Bảng 7 và cột Mã Bảng 12 quá hẹp (thiếu tblGrid) → đã khóa lưới cột, kiểm tra lại hiển thị.
  4. Bìa xuống dòng ở cột giá trị → dùng nhãn ngắn theo mẫu gốc ("GVHD Chuyên môn"), khóa lưới cột.
  5. Trang gần trống trước trang nhận xét → mở rộng phần dẫn nguồn trong B.IV.4 để trang 34 có nội dung thực.
  6. Thiếu MSSV → bổ sung dòng "Mã số sinh viên (MSSV)" vào Bảng 1.

## 3. Thể thức

| Yêu cầu | Thực hiện |
| --- | --- |
| A4; lề trái 3 cm; trên/dưới/phải 2 cm | Đặt ở section; qa kiểm tra PASS |
| Times New Roman 13, màu đen | Style Normal + mọi run đặt rFonts ascii/hAnsi/eastAsia/cs = TNR, màu 000000; bảng dùng 13 (≤5 cột) hoặc 12 (≥6 cột) |
| Giãn dòng Multiple 1.2; Before/After 0 pt | w:spacing line=288 lineRule=auto; before/after=0 cho văn bản |
| Căn đều hai bên; thụt đầu dòng 1 cm | Justify; first line 1,0 cm (nằm trong 1–1,27 cm); danh sách thụt lề trái |
| Số trang chính giữa footer | Trường PAGE căn giữa; bìa không đánh số (different first page) |
| Mục lục tự động | TOC \o "1-3" \h \z \u và TOC \c "Bảng"; đã cập nhật bằng LibreOffice UNO (2 chỉ mục) và đặt updateFields để Word tự làm mới khi mở |
| Bảng không tràn lề, lặp hàng tiêu đề | Tổng rộng bảng = 16 cm (chiều rộng khổ in), tblHeader cho hàng đầu, bảng dài được qua trang |

## 4. Kiểm tra nội dung tự động (qa_content_check.py)

- KẾT QUẢ: PASS. Không tìm thấy: `12A2`, "chủ nghiệm", "biễu", "SaPa", TODO, 【…】, XXX, ____, null, undefined, NaN, "sau bốn tuần", "kết thúc đợt thực tập", "đã dự đủ", "đã hoàn thành cả đợt".
- Dữ kiện bắt buộc có mặt: Hồ Quang Huy; MSSV 24S1020030; 25/02/2006; Tin3A; Sư phạm Tin học; Trường Đại học Sư phạm, Đại học Huế; Sa Pa, Lào Cai; Trường THPT Thuận Hóa; lớp 12/2; thầy Mai Xuân Văn; cô Nguyễn Thị Thu Phương; 26/10/2026; gặp thầy 9 giờ 45 phút, gặp cô 10 giờ 30 phút; "0 tiết chuyên môn và 0 tiết chủ nhiệm".
- Các mốc 17/11, 18/11, 21/11, 02/11 chỉ xuất hiện ở ngữ cảnh hạn nộp/kế hoạch/tổng kết của Ban chỉ đạo, không viết như việc đã xảy ra trong bài tuần 1.
- `python 04_scripts/validate_repository.py`: PASS (33 kiểm tra toàn vẹn, 56 SUM cache, 8 ảnh nhúng) – kiểm tra dữ liệu repository, không thay QA nội dung.

## 5. Phạm vi và giới hạn còn lại

- Bài phản ánh đúng tuần 1 (26/10–01/11/2026); các hoạt động video, tập văn nghệ, trò chơi ghi ở mức tuần theo xác nhận, không tự đặt ngày, tên trò chơi, số học sinh hay kết quả.
- Chưa dự giờ chuyên môn/chủ nhiệm: ghi rõ 0+0; bảng tiến độ 7+3 chỉ ở dạng kế hoạch.
- Chưa xác nhận tham dự báo cáo BGH/Đoàn trường: bài chỉ viết "theo kế hoạch được bố trí" và trình bày kết quả qua tài liệu.
- Các thông tin chưa có nguồn (tỷ lệ tốt nghiệp thực tế 2026, đỗ đại học, kiểm định, thống kê toàn thành phố, lịch sử trường, số máy tính) không đưa vào bài.
- Phần nhận xét, điểm, ngày ký, chữ ký của BGH/GVHD để trống có chủ đích (mẫu T0068); ngày ký thực tế do người có thẩm quyền điền khi nộp.
- Số trang đã render kiểm tra bằng LibreOffice; khi mở trong Microsoft Word, mục lục/danh mục bảng sẽ tự cập nhật theo bộ máy dàn trang của Word (updateFields), do đó số trang của các mục trong mục lục có thể lệch ±1 trang nhưng tổng số trang vật lý vẫn giữ ở quanh 35 do định dạng cố định.
