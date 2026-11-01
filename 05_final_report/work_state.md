# work_state – trạng thái làm bài của coding agent

Cập nhật: 01/11/2026 (theo mốc report_context).

## Đã hoàn thành

- Đọc đủ 9 tệp chỉ định (AGENTS.md, 00_meta/*, 03_report_blueprint/*) và 7 tệp tri thức `02_extracted_knowledge/`; đối chiếu FORM gốc và bìa gốc trong `04_scripts/extracted_sources/`.
- Viết 10 tệp phần trong `05_final_report/sections/` theo đúng thứ tự FORM: bìa, lời cảm ơn, A, B.I, B.II (1–6 đầy đủ 2.1–2.8, 3.1–3.4, 4, 5.1–5.2a–d, 6.1–6.5a–i), B.III (1–3), B.IV (tổng kết + phương hướng + danh mục), B.V (mẫu nhận xét BGH để trống).
- Dựng Word bằng `04_scripts/build_docx_huy.py`; cập nhật mục lục + danh mục bảng bằng `04_scripts/update_toc_uno.py` (LibreOffice UNO).
- Render và soát ảnh 35 trang qua 5 vòng; sửa 6 lỗi hình thức/nội dung (ghi trong qa_report.md mục 2).
- QA nội dung tự động PASS; `validate_repository.py` PASS.

## Trạng thái bàn giao

- `BAI_THU_HOACH_TTSP1_HO_QUANG_HUY.docx` – bản nộp, 35 trang, đã kèm PDF đối chiếu.
- Không còn trường `BAI_THU_HOACH_TTSP1_DU_THẢO` vì dữ kiện cá nhân và hoạt động tuần 1 đã đủ theo hồ sơ xác nhận.

## Việc còn mở (không chặn bài nộp 02/11)

- Ngày ký/tháng nộp thực tế: BGH tự điền theo mẫu; không tự ghi ngày.
- Tên bài, ngày dự 7+3 tiết: cập nhật theo thông báo của GVHD trong các tuần 2–4.
- Các bất nhất số liệu nguồn chưa xác nhận (Vật lí 24/27, Địa lí 17/22, học vị Trần Văn Dũng, Hoàng Đức Vương): giữ nguyên cảnh báo trong bài, không tự sửa.
