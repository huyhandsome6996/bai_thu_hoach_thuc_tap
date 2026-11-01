# Blueprint bài thu hoạch TTSP1 tại THPT Thuận Hóa

Đợt thực tập 26/10–21/11/2026; chốt tìm hiểu tuần 1 ngày 01/11; hạn bài thực tế giáo dục 02/11/2026. Hồ sơ **Hồ Quang Huy, MSSV 24S1020030, lớp Tin3A, ngành Sư phạm Tin học, lớp thực tập chủ nhiệm 12/2**. Đã có bài Word theo FORM, kiểm tra và sửa từ commit `36ea69e`; bản xuất Microsoft Word có **35 trang A4**.

## Bản đã kiểm tra

- [Bài thu hoạch Word](05_final_report/BAI_THU_HOACH_TTSP1_HO_QUANG_HUY.docx).
- [Kết quả kiểm tra và sửa](05_final_report/qa_report.md), [kiểm tra tài liệu dạng JSON](05_final_report/qa_checks.json).
- PDF cùng tên trong `05_final_report/` là bản đối chiếu dàn trang xuất từ Word. Phần nhận xét/chữ ký để trống theo mẫu.
- Chạy kiểm tra bản nộp bằng Python của runtime có python-docx/pypdf: `python 04_scripts/qa_submission.py`. Tái dựng DOCX: `build_docx_huy.py`, sau đó cập nhật mục lục và xuất PDF bằng `render_word_review.ps1` trên Windows có Microsoft Word; render và xem lại sau mỗi sửa đổi. Script QA không thay kiểm tra hình ảnh.

## Bắt đầu từ đây

Coding Agent phải đọc [quy tắc toàn repository](AGENTS.md) và [mốc thời gian bài viết](00_meta/report_context.json) trước khi triển khai. Đây là bài sau tuần thực tập đầu tiên, không phải tổng kết cả đợt.

Đọc thêm [hoạt động tuần đầu đã xác nhận](00_meta/confirmed_week1_activities.md). Người dùng chưa dự giờ chuyên môn hoặc chủ nhiệm; không tính hỗ trợ 15 phút đầu giờ thành một tiết dự giờ.

1. Đọc [kết quả QA](00_meta/qa_findings.md) để biết các sai khác và giới hạn nguồn.
2. Điền [khảo sát](00_meta/missing_info_survey.md),cập nhật [hồ sơ](00_meta/student_profile.json);tra46SVở [bảng chuẩn hóa](02_extracted_knowledge/06_danh_sach_46_sinh_vien_ttsp1.md).
3. Xem [chiến lược35trang](03_report_blueprint/pagination_strategy.md) và [dàn ýH4](03_report_blueprint/master_outline_detailed.md).
4. Bàn giao [Master Prompt](03_report_blueprint/prompt_for_coding_agent.md) cho Coding Agent.

## Phân vùng

- `00_meta/`:hồ sơ,khảo sát,roster,hash gốc,QA và kết quả kiểm tra.
- `01_raw_data/`:9tệpOffice nguyên byte;không sửa nguồn.
- `02_extracted_knowledge/`:7tệpMarkdown chuyên đề,có số liệu,bảng tra,mã nguồn và phần nguồn đầy đủ.
- `03_report_blueprint/`:kế hoạch từng trang,dàn ý chi tiết,prompt triển khai.
- `04_scripts/`:công cụ tái lập;`extracted_sources/`lưuJSON/Markdown,bản chuyểnDOCX vàảnh nhúng.
- `05_final_report/sections/`:dành cho bản viết ở bước tiếp theo;không đặt văn bản giả làm bài chính thức.

## Tái lập

PowerShell trênWindows cóWord: `./04_scripts/convert_legacy_docs.ps1` để tạo bản sao chuyển đổi2tệpDOCnếu cần. Tiếp theo chạy lần lượt:

```text
python 04_scripts/parse_all_docs.py
python 04_scripts/build_knowledge.py
python 04_scripts/build_blueprint.py
python 04_scripts/validate_repository.py
```

Các scriptPython dùng thư viện chuẩn,không cần cài gói;scriptblueprint không ghi đè hồ sơ đã tồn tại. Scripttrích xuất không tự chuyểnDOC,mà dùng bảnDOCXtrung gian đã có. Các scriptbuild sẽ tạo lại tệp tri thức/blueprint tương ứng,không dùng sau khi đã chỉnh tay các tệp đó nếu chưa lưu thay đổi. Master Prompt được biên soạn riêng và không bị scriptbuild ghi đè.

Yêu cầu hiện tại là **30–35 trang Word, bám đúng thứ tự FORM gốc**, mục tiêu 35 trang. Không còn phương án khoảng 40 trang hoặc cấu trúc chính C/D/E/F. Chỉ xác nhận số trang thực tế sau khi tạo Word, cập nhật mục lục và render kiểm tra. Script `build_blueprint.py` tự áp dụng cập nhật cá nhân hóa và blueprint theo FORM từ `update_personalized_handoff.py`.
