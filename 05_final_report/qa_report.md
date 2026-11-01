# Kiểm tra và sửa bài thu hoạch TTSP1 của Hồ Quang Huy

## Kết luận và phạm vi

Đã kiểm tra commit đầu vào `36ea69e1217ea207f5bedca3b0eac9ecf076dfe1` và sửa trực tiếp bản Word cùng các phần Markdown nguồn. Commit này đã có trên `origin/main`; cập nhật máy bằng fast-forward, không force-push hoặc xóa lịch sử.

Bản đã sửa đáp ứng các yêu cầu nội dung và hình thức đã kiểm tra từ FORM, bìa, tài liệu Hình thức và hồ sơ người dùng: **35 trang vật lý A4 khi dàn trang bằng Microsoft Word**, tính cả bìa và trang nhận xét. Sản phẩm nộp là `BAI_THU_HOACH_TTSP1_HO_QUANG_HUY.docx`. PDF cùng tên là bản đối chiếu bố cục xuất từ chính Word. Phần nhận xét, ngày ký, điểm và chữ ký dành cho nhà trường/người có thẩm quyền giữ trống theo mẫu; kết quả QA không thay đánh giá của GVHD.

Phạm vi nội dung vẫn là tuần đầu **26/10–01/11/2026**, không phải tổng kết cả đợt. Mốc hạn 02/11, 17/11, 18/11, 21/11 được trình bày theo lịch kế hoạch, không ký lùi ngày. Hồ sơ có đủ thông tin cốt lõi đã được người dùng xác nhận, đúng lớp **Tin3A** và lớp thực tập **12/2**.

## Các lỗi trong commit đầu vào và cách sửa

| Vấn đề | Sửa trong bản hiện tại |
| --- | --- |
| Dùng kết quả lớp 12/2 năm 2025–2026 làm nền nhận xét lớp 12/2 hiện tại | Phân biệt rõ hai khóa học sinh; không gán sĩ số hoặc xếp loại năm trước cho lớp hiện tại |
| Nhận định tỷ lệ Tốt cao nhất là lớp 12/5 | Tính lại: lớp 12/3 có 19/27 = 70,37%, cao nhất bảng; bổ sung tổng theo khối 2/17, 29/149, 73/136 |
| Suy giảm 8 học sinh là chuyển trường/chuyển hướng; suy tương quan học tập–rèn luyện ở từng cá nhân | Bỏ các kết luận nhân quả/cá nhân chưa có dữ liệu; nêu giới hạn bảng tổng hợp |
| Đồng nhất 7h–7h10 với hỗ trợ 15 phút đầu giờ | Ghi đúng 10 phút theo văn bản và tách hoạt động 15 phút theo lời người dùng |
| Coi khung 10 tiết là số tiết mọi học sinh học mỗi ngày | Ghi đây là khung giờ; thời lượng từng lớp phải theo thời khóa biểu cụ thể |
| Ghi sinh viên Tin học sẽ dự hai môn vì nhóm ghép Tin–Công nghệ | Sửa: dự chuyên môn môn Tin học theo phân công; không nhầm với cơ cấu 4+3 của ngành Công nghệ |
| Tự suy việc quay video, phản hồi/buổi họp và lý do giao nhiệm vụ | Trả về “thực hiện video”, vai trò hỗ trợ và những sự kiện đã xác nhận; bỏ suy diễn quy trình chưa có ghi chép |
| Dẫn tài liệu hình thức bằng [S07] và gán khung 5512 cho [S09] | Sửa về [S03]; bổ sung [S10] riêng cho khung KHBD, tách yêu cầu số/AI trong tài liệu địa phương |
| Một số bảng/chú thích cỡ 12, tiêu đề danh mục cỡ 14 và giãn đoạn khác 0 | Nội dung sau bìa, kể cả bảng/chú thích/mục lục: TNR 13, đen, Multiple 1.2, Before/After 0 pt; bìa giữ thiết kế mẫu |
| Bảng học tập/rèn luyện 10 cột quá dày | Tách hai bảng 5 và 6 cột, kiểm lại tổng 302 và các mức, không giảm font |
| Bản ghi bảng bị ngắt qua trang; dòng mục lục dài sát số trang | Không tách từng hàng dữ liệu; lặp hàng tiêu đề; chừa chỗ cho số trang mục lục, nới cột ngày tháng |
| Script kiểm tra dùng đường dẫn cố định /home/... và không trả exit code lỗi | Chuyển sang đường dẫn tương đối repo, trả mã thoát; thêm kiểm tra trên tài liệu thật |

## Đối chiếu FORM

Thứ tự trong Word: bìa nguồn → lời cảm ơn → mục lục/danh mục → A. Tóm lược về bản thân → B.I. Hoạt động đã thực hiện → B.II. Kết quả tìm hiểu (đủ 1–6, 2.1–2.8, 3.1–3.4, 5.1–5.2, 6.1–6.5) → B.III. Công tác TTSP1 (đủ ba mục) → IV. Tổng kết → V. Nhận xét của BGH. FORM nguồn in trùng hai mục IV; bản nộp sửa số mục cuối thành V, không thay tên hoặc vị trí nội dung. Không thêm C/D/E/F ngoài FORM.

Trong mục 6.5 giữ các nhóm biện pháp a, b, c, d, e, g, h, i theo FORM. Nội dung hồ sơ học sinh, nhiệm vụ giáo viên, hoạt động giáo dục và đánh giá/xếp loại được bố trí trong các mục B tương ứng để bao phủ tiêu chí Phụ lục 8. Không gọi các hồ sơ dự kiến tìm hiểu là hồ sơ đã trực tiếp khảo sát.

## Kiểm tra có thể tái lập

- `validate_repository.py`: **33 kiểm tra toàn vẹn đạt**, đối chiếu **56 SUM cache**, trích 8 ảnh; tệp Office gốc giữ nguyên SHA-256.
- `qa_submission.py`: **35/35 kiểm tra tài liệu đạt**; kết quả chi tiết ở `qa_checks.json`. Kiểm tra thông tin cá nhân, giờ gặp GVHD, 0+0 tiết dự giờ, thứ tự FORM, font/cỡ/màu, giãn đoạn, khổ giấy/lề, tổng hai bảng kết quả, footer, phạm vi bảng và số trang PDF.
- `qa_content_check.py`: kiểm tra bổ sung các cụm sai/thiếu và thể thức cơ bản; dùng đường dẫn repo hiện tại, trả exit code có ý nghĩa.
- Microsoft Word: cập nhật trường SEQ, mục lục và danh mục bảng, dàn trang lại, cập nhật số trang rồi lưu DOCX và xuất PDF. Số trang trực tiếp của Word và số trang PDF cùng bằng **35**.
- Render PDF thành ảnh bằng Poppler trong runtime; kiểm tra toàn bộ 35 trang: bìa, mục lục, bảng nối trang, chữ tiếng Việt, lề, số trang và trang ký. Không phát hiện chữ bị cắt, bảng vượt lề hoặc trang trắng bất thường. Ảnh QA nằm trong cache `04_scripts/qa_review/`, không đưa lên Git.

Renderer `render_docx.py` của kỹ năng đã được thử nhưng không chạy được do Windows không có LibreOffice/soffice.exe. Đã dùng **Microsoft Word COM chạy ẩn để xuất PDF**, sau đó raster bằng Poppler; không lấy bản PDF cũ của commit làm bằng chứng cho DOCX đã sửa. Các bước Word nằm trong `render_word_review.ps1`.

## Lưu ý trước khi nộp

- Bản Word và PDF là một cặp đã kiểm tra cùng phiên bản; không sửa DOCX rồi tiếp tục dùng PDF cũ.
- Ảnh/font, driver hoặc phiên bản Word trên máy khác có thể làm đổi phân trang. Nếu chỉnh sửa, đổi máy hoặc cập nhật trường lại, kiểm tra Print Preview; không coi con số 35 là bất biến.
- Chỉ có lời xác nhận về hoạt động hỗ trợ; không tự tạo ảnh/video đính kèm, tên trò chơi, ngày hoạt động hoặc kết quả chưa được cung cấp. Không tự nhận đã dự giờ.
- Chưa có nguồn cho tỷ lệ đỗ đại học, tốt nghiệp thực tế 2026 hoặc giấy công nhận kiểm định; bài không đưa các kết quả đó vào như thành tích đã xác nhận.
- Không có điểm/chữ ký/nhận xét giả. Người có thẩm quyền điền phần cuối khi thực hiện thủ tục nộp.
