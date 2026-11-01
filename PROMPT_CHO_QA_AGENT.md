# PROMPT DÀNH CHO QA AGENT: PHÂN HOẠCH REPO DỰ ÁN & THIẾT KẾ BLUEPRINT BÀI THU HOẠCH THỰC TẬP SƯ PHẠM 1 (TTSP1)
*(Mục tiêu: Chuẩn bị tri thức, cấu trúc và prompt đặc tả để Coding Agent viết bài thu hoạch thực tập chi tiết từ 30 – 35 trang)*

---

## 1. BỐI CẢNH VÀ VẤN ĐỀ (CONTEXT & PROBLEM STATEMENT)

### 1.1. Bối cảnh đợt thực tập
- **Cơ sở đào tạo:** Trường Đại học Sư phạm, Đại học Huế.
- **Đơn vị thực tập tiếp nhận:** Trường THPT Thuận Hóa (Trường thực hành trực thuộc Trường ĐH Sư phạm Huế, địa chỉ tại 34 Lê Lợi, TP. Huế).
- **Kỳ thực tập:** Thực tập Sư phạm 1 (TTSP1) – Năm học 2026 – 2027.
- **Thời gian diễn ra đợt thực tập:** Từ ngày **26/10/2026 đến ngày 21/11/2026** (kéo dài 4 tuần).
- **Thời điểm hiện tại:** Sinh viên vừa hoàn thành trọn vẹn tuần đầu tiên (từ 26/10/2026 đến 01/11/2026) gồm: dự lễ chào cờ, nghe báo cáo tình hình nhà trường từ BGH, nghe báo cáo hoạt động Đoàn TNCS Hồ Chí Minh, tiếp xúc GVHD chuyên môn, GVHD chủ nhiệm, ra mắt lớp thực tập, tìm hiểu hồ sơ sổ sách và dự những tiết học đầu tiên.
- **Hạn nộp khẩn cấp:** Theo đúng Kế hoạch số .../KH-THPT ngày 21/10/2026 của Trường THPT Thuận Hóa, **hạn cuối cùng nộp Bài tìm hiểu thực tế giáo dục TTSP1 là ngày mai (Thứ Hai, ngày 02/11/2026)** để Trưởng đoàn tập hợp nộp cho Ban chỉ đạo nhà trường.

### 1.2. Vấn đề hiện tại
1. Toàn bộ dữ liệu thu thập được trong tuần qua đang ở dạng các file rời rạc tải từ nhóm Zalo (`.docx`, `.doc`, `.xlsx`), nằm lộn xộn tại thư mục gốc của repository.
2. Yêu cầu của bài thu hoạch rất lớn: **Độ dài ít nhất từ 30 đến 35 trang A4**, nội dung phải cực kỳ chi tiết, phong phú, chuẩn mực sư phạm, phản ánh chính xác số liệu thực tế của trường THPT Thuận Hóa và bám sát khung văn bản quy phạm của ĐH Sư phạm Huế (QĐ 2760/QĐ-ĐHSP) và Bộ GD&ĐT (CV 5512/BGDĐT-GDTrH kèm phụ lục IV tích hợp năng lực số và năng lực AI).
3. Thiếu một cơ chế phân hoạch repository rõ ràng, thiếu hệ thống tri thức (Knowledge Base) dạng `.md` để một **Coding Agent / Writer Agent** có thể đọc hiểu toàn bộ ngữ cảnh, dữ liệu và triển khai viết bài mà không bị quá tải ngữ cảnh (context overflow), không bị viết lan man cụt ý, hoặc bịa đặt sai lệch số liệu.
4. Một số thông tin cá nhân của sinh viên (Họ tên, Khoa/Ngành, Lớp, GVHD chuyên môn, GVHD chủ nhiệm, lớp tiếp nhận) cần được khớp nối từ danh sách 46 sinh viên thực tập có sẵn trong văn bản và được người dùng xác nhận.

---

## 2. NGUYÊN TẮC VÀ VAI TRÒ CỦA QA AGENT (ROLE & PRINCIPLES)

Bạn là **Lead QA Agent / Solution Architect** chuyên về Quản trị Dự án và Kỹ thuật Tài liệu Sư phạm. Nhiệm vụ của bạn trong phiên làm việc này là:
1. **Khảo sát & Khai phá dữ liệu:** Quét sạch toàn bộ các tệp tin trong thư mục gốc, giải mã/trích xuất nội dung từ các file Office (`.docx`, `.doc`, `.xlsx`).
2. **Tái cấu trúc (Refactor & Partition) Repository:** Tổ chức lại cây thư mục theo tiêu chuẩn chuyên nghiệp, tách biệt dữ liệu thô (raw), dữ liệu tri thức (.md), kiến trúc thiết kế (blueprint) và sản phẩm đầu ra (output).
3. **Biên soạn bộ Knowledge Base (.md):** Tổng hợp và số hóa toàn bộ dữ liệu thực tế từ các báo cáo thành các chuyên đề tri thức có cấu trúc logic, bảng biểu rõ ràng.
4. **Thiết kế Đề cương 30 – 35 trang (Pagination Strategy & Master Blueprint):** Xây dựng chiến lược phân bổ dung lượng chi tiết từng trang cho bài thu hoạch đảm bảo dung lượng 30 - 35 trang một cách tự nhiên, thực chất và khoa học.
5. **Tương tác thu thập thông tin khuyết thiếu (Interactive Survey):** Đối chiếu danh sách 46 sinh viên có sẵn trong file `1. Kế hoạch TTSP1 năm 2026-2027.docx` và bảng `Phân công giảng dạy HK1 năm học 2026- 2027.xlsx` để hỏi người dùng xác nhận thông tin cá nhân.
6. **Biên soạn Prompt bàn giao cho Coding Agent:** Viết sẵn file prompt chi tiết từng câu lệnh, từng bước hướng dẫn Coding Agent cách viết bài thu hoạch hoàn chỉnh (bằng Python sinh file Word `.docx` chuẩn định dạng kỹ thuật hoặc file Markdown siêu dài).

---

## 3. ĐẦU VÀO CỦA DỰ ÁN (INPUT SPECIFICATIONS)

QA Agent cần đọc, phân tích và liên kết thông tin từ 8 tệp tài liệu Zalo hiện có trong repository:

| STT | Tên tệp tin gốc | Loại tệp | Vai trò và nội dung khai thác trọng tâm |
| :--- | :--- | :--- | :--- |
| **1** | `FORM BÀI THU HOẠCH TÌM HIỂU THỰC TẾ GIÁO DỤC TTSP1.docx` | .docx | **Khung xương bắt buộc của bài thu hoạch:** Quy định chính xác các đề mục từ Trang bìa, Lời cảm ơn, Phần A (Tóm lược bản thân), Phần B (Hoạt động đã làm & Kết quả tìm hiểu: 1. Địa phương; 2. Đặc điểm trường; 3. Cơ cấu tổ chức; 4. Hoạt động GD; 5. Hoạt động Đoàn; 6. Kế hoạch GD 2026-2027), Phần C (Công tác TTSP1), Phần D (Tổng kết & Nhận xét BGH). |
| **2** | `Hình thức làm bài thu hoạch (1).docx` | .docx | **Quy chuẩn định dạng kỹ thuật & Lưu ý chuyên môn:** <br>- Font: Times New Roman, Size 13.<br>- Dãn dòng: Before 0pt, After 0pt, Line spacing Multiple 1.2.<br>- Thụt đầu dòng: First line 1.0 – 1.27 cm. Căn đều 2 bên (Justify).<br>- Khổ giấy A4, Căn lề: Trái 3cm, Trên 2cm, Dưới 2cm, Phải 2cm. Số trang ở giữa footer.<br>- Soạn KHBD: Bám sát CV 5512 + Phụ lục IV, bắt buộc tích hợp **Năng lực số** và **Năng lực AI**.<br>- Ghi phiếu dự giờ: Viết chi tiết hoạt động GV và HS; phần nhận xét đánh giá tích cực, mang tính xây dựng. |
| **3** | `Bìa bài thu hoạch trường.docx` | .docx | **Mẫu trang bìa chuẩn mực:** Cơ quan chủ quản (Trường ĐH Sư phạm - ĐH Huế, Trường THPT Thuận Hóa), tiêu đề, tên sinh viên, ngành thực tập, GVHD chuyên môn, GVHD chủ nhiệm, thời gian (26/10/2026 – 21/11/2026), địa danh (Huế, tháng 11 năm 2026). |
| **4** | `1. Kế hoạch TTSP1 năm 2026-2027.docx` | .docx | **Kế hoạch triển khai & Danh sách phân công 46 sinh viên:**<br>- Lịch trình tuần 1 (chào cờ, báo cáo BGH, báo cáo Đoàn, gặp GVHD), tuần 2-3 (dự giờ 7 tiết chuyên môn + 3 tiết chủ nhiệm HĐTN-HN), tuần 4 (tổng kết).<br>- Danh sách phân công chi tiết 46 SV với Ngày sinh, Ngành thực tập, GVHD Chuyên môn và GVHD Chủ nhiệm.<br>- Hạn chót nộp bài tìm hiểu thực tế giáo dục: **02/11/2026**. |
| **5** | `Báo cáo tổng kết năm học 2025 -2026.chốt.doc` | .doc (binary) | **Kho dữ liệu thực tế khổng lồ về trường THPT Thuận Hóa:**<br>- Vị trí, lịch sử, thuận lợi, khó khăn.<br>- Quy mô lớp học, cơ sở vật chất (phòng học, phòng thực hành Lý, Hóa, Sinh, Tin, thư viện).<br>- Đội ngũ cán bộ, giáo viên (trình độ Tiến sĩ, Thạc sĩ, Cử nhân).<br>- Thành tích năm học 2025-2026: Giải HSG cấp Tỉnh, cấp Quốc gia, bảng tỷ lệ học lực/hạnh kiểm các khối 10, 11, 12, tỷ lệ đậu tốt nghiệp 100%, tỷ lệ trúng tuyển ĐH, kiểm định chất lượng mức độ 2, chuẩn quốc gia mức 1. |
| **6** | `2.10.26. Kế hoạch giáo dục nhà trường 2026-2027.docx` | .docx | **Kế hoạch giáo dục năm học mới (QĐ 145/QĐ-THPT ngày 15/9/2026):**<br>- Mục tiêu giáo dục năm học 2026-2027.<br>- Kế hoạch thực hiện CT GDPT 2018 các khối lớp, chuyên đề học tập.<br>- Đổi mới phương pháp dạy học (dạy học tích cực, tích hợp, STEM).<br>- Đổi mới kiểm tra đánh giá theo định hướng phát triển năng lực.<br>- Kế hoạch ứng dụng CNTT, chuyển đổi số và công nghệ trí tuệ nhân tạo (AI).<br>- Phong trào xây dựng trường học thân thiện, học sinh tích cực. |
| **7** | `BAO_CAO_DOAN_TTSP1_THANG_10.docx` | .docx | **Báo cáo hoạt động Đoàn và phong trào thanh niên (ngày 26/10/2026):**<br>- Cơ cấu 08 chi đoàn (07 chi đoàn học sinh + 01 chi đoàn giáo viên).<br>- 107 đoàn viên học sinh, 10 đoàn viên giáo viên.<br>- Danh sách BCH Đoàn trường: Cô Trương Thị Thu Thảo (Bí thư), Thầy Nguyễn Hữu Nhanh Tiến & Cô Đoàn Thị Phương Dung (Phó Bí thư)...<br>- Các hoạt động giáo dục tư tưởng, đạo đức, nề nếp, phong trào văn nghệ, TDTT, "Học sinh 3 tốt", phát triển Đảng trong học sinh. |
| **8** | `Phân công giảng dạy HK1 năm học 2026- 2027.xlsx` | .xlsx | **Bảng phân công chuyên môn học kỳ 1 năm học 2026-2027:**<br>- Chi tiết danh sách toàn bộ giáo viên theo từng tổ/bộ môn: Toán (79 tiết), Vật lý (24 tiết), Hóa học (39 tiết), Sinh học, Tin học, Ngữ văn, Lịch sử, Địa lý, Ngoại ngữ, GDCD, GDTC, QPAN, Công nghệ.<br>- Phân công giáo viên phụ trách phòng học bộ môn, giáo viên chủ nhiệm từng lớp (10/1 đến 10/6, 11/1 đến 11/4, 12/1 đến 12/6). |
| **9** | `vt_phu_luc_kem_theo_qd_2760_qd-dhsp.doc` | .doc (binary) | **Văn bản pháp lý nền tảng của ĐH Sư phạm Huế:**<br>- Nội quy thực tập sư phạm (Phụ lục 1).<br>- Hướng dẫn dự giờ và rút kinh nghiệm (Phụ lục 2 & 3).<br>- Mẫu phiếu dự giờ chuyên môn (Phụ lục 4).<br>- Mẫu kế hoạch giảng dạy (Phụ lục 6) & Kế hoạch chủ nhiệm (Phụ lục 7).<br>- Phiếu đánh giá chấm điểm thực tập (Phụ lục 8, 9, 10, 11). |

---

## 4. QUY TRÌNH PHÂN HOẠCH REPOSITORY (REPO RESTRUCTURING PLAN)

QA Agent phải chủ động lập trình (sử dụng PowerShell hoặc Python có sẵn) để tạo cấu trúc thư mục mới và phân loại các tệp tin một cách ngăn nắp:

```text
bai_thu_hoach_thuc_tap/
│
├── 00_meta/                               # Quản lý hồ sơ sinh viên & Bảng câu hỏi tương tác
│   ├── student_profile.json               # Dữ liệu sinh viên cá nhân hóa (được cập nhật sau khảo sát)
│   └── missing_info_survey.md             # Bảng câu hỏi trắc nghiệm/điền thông tin gửi người dùng
│
├── 01_raw_data/                           # Lưu trữ nguyên vẹn các file Zalo gốc ban đầu
│   ├── 1. Kế hoạch TTSP1 năm 2026-2027.docx
│   ├── 2.10.26. Kế hoạch giáo dục nhà trường 2026-2027.docx
│   ├── BAO_CAO_DOAN_TTSP1_THANG_10.docx
│   ├── Báo cáo tổng kết năm học 2025 -2026.chốt.doc
│   ├── Bìa bài thu hoạch trường.docx
│   ├── FORM BÀI THU HOẠCH TÌM HIỂU THỰC TẾ GIÁO DỤC TTSP1.docx
│   ├── Hình thức làm bài thu hoạch (1).docx
│   ├── Phân công giảng dạy HK1 năm học 2026- 2027.xlsx
│   └── vt_phu_luc_kem_theo_qd_2760_qd-dhsp.doc
│
├── 02_extracted_knowledge/                # Toàn bộ dữ liệu đã được trích xuất thành Markdown sạch
│   ├── 01_thong_tin_nha_truong.md         # Vị trí, lịch sử, CSVC, phòng học bộ môn, thời gian ra vào lớp
│   ├── 02_so_lieu_tong_ket_2025_2026.md   # Dữ liệu thống kê HSG, tỷ lệ học lực, tỷ lệ tốt nghiệp, thi đua
│   ├── 03_ke_hoach_giao_duc_2026_2027.md  # Kế hoạch GD năm học mới, chỉ tiêu, đổi mới PPDH, CNTT & AI
│   ├── 04_hoat_dong_doan_thanh_nien.md    # Chi đoàn, đoàn viên, phong trào, danh sách BCH Đoàn trường
│   ├── 05_phan_cong_chuyen_mon_gv.md      # Chi tiết phân công dạy học, GVCN, tổ nhóm chuyên môn
│   ├── 06_danh_sach_46_sinh_vien_ttsp1.md # Bảng tra cứu 46 sinh viên, GVHD chuyên môn & chủ nhiệm
│   └── 07_quy_che_va_bieu_mau_dhsp.md     # Nội quy TTSP, tiêu chí chấm điểm, mẫu phiếu dự giờ, KHBD
│
├── 03_report_blueprint/                   # Bản thiết kế kiến trúc bài thu hoạch 30 - 35 trang
│   ├── pagination_strategy.md             # Chiến lược phân bổ dung lượng chi tiết từng trang (Trang 1 -> 35+)
│   ├── master_outline_detailed.md         # Khung đề cương sâu đến cấp H4, gắn liền từng mục với số liệu thực tế
│   └── prompt_for_coding_agent.md         # Master Prompt hoàn chỉnh để bàn giao cho Coding Agent viết bài
│
├── 04_scripts/                            # Công cụ tự động hóa trích xuất dữ liệu và biên soạn
│   ├── parse_all_docs.ps1 (hoặc .py)      # Script đọc và chuyển đổi tự động các file doc/docx/xlsx
│   └── generate_report_docx.py            # Script Python hỗ trợ sinh file Word hoàn chỉnh định dạng Times New Roman 13
│
└── 05_final_report/                       # Thư mục lưu trữ bài thu hoạch chính thức
    ├── sections/                          # Các chương mục dự thảo dạng Markdown
    └── BÀI_THU_HOẠCH_TTSP1_CHÍNH_THỨC.docx # Bản Word hoàn chỉnh nộp nhà trường
```

> **Lưu ý kỹ thuật cho QA Agent:**
> - Các file `.doc` (Word 97-2003) và `.xlsx` có thể trích xuất văn bản dễ dàng bằng PowerShell COM (`New-Object -ComObject Word.Application` / `Excel.Application`) hoặc thư viện tiêu chuẩn của Python.
> - Sau khi trích xuất, toàn bộ nội dung phải được cấu trúc thành các file `.md` trong thư mục `02_extracted_knowledge/` với bảng biểu Markdown chuẩn để Coding Agent đọc trong vài giây.

---

## 5. THIẾT KẾ ĐỀ CƯƠNG CHI TIẾT & CHIẾN LƯỢC PHÂN BỔ TRANG (PAGINATION STRATEGY: 30 – 35 TRANG)

Để đạt mục tiêu tối thiểu 30 - 35 trang chất lượng cao, sâu sắc, không trùng lặp, QA Agent phải thiết kế đề cương theo cấu trúc sau:

```text
========================================================================================
BẢN PHÂN BỔ DUNG LƯỢNG VÀ NỘI DUNG CHI TIẾT (TỔNG CỘNG: 35 TRANG A4)
========================================================================================

TRANG 1: TRANG BÌA CHÍNH (Đúng chuẩn file "Bìa bài thu hoạch trường.docx")
- Đơn vị chủ quản: Bộ GD&ĐT / ĐH Huế / ĐH Sư phạm Huế & THPT Thuận Hóa.
- Nhan đề: BÀI THU HOẠCH TÌM HIỂU THỰC TẾ GIÁO DỤC - THỰC TẬP SƯ PHẠM 1.
- Thông tin: Sinh viên thực hiện, Ngành, GVHD Chuyên môn, GVHD Chủ nhiệm, Thời gian (26/10 - 21/11/2026).

TRANG 2: TRANG BÌA PHỤ & LỜI CAM ĐOAN
- Bìa phụ trang trọng. Lời cam đoan tính trung thực của số liệu và kết quả tìm hiểu thực tế.

TRANG 3: LỜI CẢM ƠN (Trân trọng, sâu sắc)
- Cảm ơn BGH ĐH Sư phạm Huế, Ban chỉ đạo TTSP1.
- Cảm ơn BGH THPT Thuận Hóa, BCH Đoàn trường, các thầy cô GVHD chuyên môn, GVHD chủ nhiệm và tập thể học sinh.

TRANG 4 - 5: MỤC LỤC CHI TIẾT, DANH MỤC CHỮ VIẾT TẮT & DANH MỤC BẢNG BIỂU / SƠ ĐỒ
- Mục lục phân cấp từ H1 đến H4.
- Bảng chữ viết tắt: GD&ĐT, GDPT, BGH, GVHD, GVCN, TTSP, HĐTN-HN, CNTT, STEM, AI...
- Danh mục bảng biểu (Bảng kết quả học lực, Bảng giải HSG, Bảng phân công đội ngũ...).

TRANG 6 - 7: PHẦN A - TÓM LƯỢC VỀ BẢN THÂN VÀ ĐƠN VỊ THỰC TẬP
- Lý lịch trích ngang sinh viên thực tập (Họ tên, ngày sinh, quê quán, lớp, khoa, khóa đào tạo).
- Giới thiệu nhóm thực tập, ngành đào tạo, lớp thực tập chủ nhiệm và môn học đảm nhận.
- Nhận thức sơ bộ về sứ mệnh người giáo viên trong kỷ nguyên chuyển đổi số và chương trình GDPT 2018.

TRANG 8 - 9: PHẦN B.I - CÁC HOẠT ĐỘNG ĐÃ THỰC HIỆN TRONG TUẦN ĐẦU TIÊN (26/10 - 01/11/2026)
- Lịch trình hoạt động chi tiết ngày đầu tiên (26/10): Dự lễ chào cờ đầu tuần, nghe BGH báo cáo tổng quan, nghe Đoàn trường báo cáo công tác thanh niên, gặp gỡ các tổ chuyên môn và GVHD.
- Các hoạt động từ 27/10 đến 01/11: Tiếp xúc lớp chủ nhiệm, nghiên cứu hồ sơ nhà trường, nghiên cứu phân phối chương trình, dự các tiết học mẫu của GVHD, tìm hiểu tâm lý học sinh.
- Phương pháp thu thập thông tin: Nghe báo cáo, nghiên cứu tài liệu lưu trữ, phỏng vấn chuyên sâu, điều tra khảo sát thực địa.

TRANG 10 - 13: PHẦN B.II.1 & B.II.2 - TÌNH HÌNH GIÁO DỤC ĐỊA PHƯƠNG & ĐẶC ĐIỂM NHÀ TRƯỜNG
- Mục 1: Khái quát bức tranh giáo dục phổ thông tỉnh Thừa Thiên Huế và vị thế trường THPT Thuận Hóa (trực thuộc trường Sư phạm danh tiếng).
- Mục 2.1 - 2.6: Tổng quan vị trí 34 Lê Lợi, cơ sở vật chất (hệ thống nhà H, phòng học đa năng, phòng thí nghiệm Lý - Hóa - Sinh, phòng máy vi tính, thư viện, thời khóa biểu và quy định thời gian ra vào lớp).
- Mục 2.7: BẢNG BIỂU & PHÂN TÍCH THÀNH TÍCH NĂM HỌC 2025 - 2026:
  + Thành tích thi chọn HSG cấp Tỉnh (liệt kê danh sách các môn đạt giải).
  + Thống kê chất lượng học tập và rèn luyện (Tỷ lệ Xuất sắc, Giỏi, Khá; Tỷ lệ Hạnh kiểm Tốt; Tỷ lệ đỗ tốt nghiệp 100%, đỗ ĐH).
  + Kiểm định chất lượng giáo dục đạt Mức độ 2 và Chuẩn quốc gia Mức độ 1.
- Mục 2.8: Phân tích sâu sắc Thuận lợi (đội ngũ sư phạm chất lượng cao, gắn liền ĐH Sư phạm) và Khó khăn (áp lực đổi mới GDPT 2018, cơ sở vật chất cần tiếp tục nâng cấp).

TRANG 14 - 16: PHẦN B.II.3 & B.II.4 - CƠ CẤU TỔ CHỨC & CÁC HOẠT ĐỘNG GIÁO DỤC NHÀ TRƯỜNG
- Sơ đồ cơ cấu tổ chức bộ máy nhà trường: BGH (Hiệu trưởng, các Phó Hiệu trưởng), Hội đồng trường, Công đoàn, Đoàn Thanh niên.
- Đội ngũ cán bộ giáo viên: Tỷ lệ Thạc sĩ, Tiến sĩ vượt chuẩn; phong cách làm việc chuyên nghiệp, mẫu mực.
- Danh sách và phân công các tổ/nhóm chuyên môn: Toán, Vật lý, Hóa học, Sinh học, Tin học, Ngữ văn, Lịch sử, Địa lý, Ngoại ngữ, GDCD, TD-QPAN, Công nghệ.
- Đội ngũ GVCN năm học 2026 - 2027 và phương thức quản lý nề nếp học sinh.
- Các hoạt động giáo dục trọng điểm: Hoạt động dạy học chính khóa, bồi dưỡng HSG, phụ đạo học sinh, giáo dục STEM, hoạt động trải nghiệm hướng nghiệp (HĐTN-HN).

TRANG 17 - 18: PHẦN B.II.5 - HOẠT ĐỘNG ĐOÀN VÀ PHONG TRÀO THANH NIÊN NĂM HỌC 2026 - 2027
- Dữ liệu thực tế từ Báo cáo Đoàn tháng 10/2026: 08 chi đoàn (07 chi đoàn HS + 01 chi đoàn GV), 107 đoàn viên học sinh.
- Ban Chấp hành Đoàn trường: Cô Trương Thị Thu Thảo (Bí thư), Thầy Nguyễn Hữu Nhanh Tiến, Cô Đoàn Thị Phương Dung...
- Các mặt công tác:
  + Giáo dục chính trị tư tưởng, đạo đức, tác phong, truyền thống lịch sử.
  + Phong trào thi đua dạy tốt - học tốt, xây dựng "Trường học thân thiện, học sinh tích cực".
  + Phong trào "Học sinh 3 tốt", hoạt động văn hóa, văn nghệ, thể dục thể thao, tình nguyện vì cộng đồng.
  + Công tác bồi dưỡng phát triển Đoàn viên và phát hiện nhân tố ưu tú phát triển Đảng viên tuổi 18.

TRANG 19 - 22: PHẦN B.II.6 - KẾ HOẠCH GIÁO DỤC NHÀ TRƯỜNG NĂM HỌC 2026 - 2027 (QĐ 145/QĐ-THPT)
- Mục tiêu tổng quát và các chỉ tiêu giáo dục năm học 2026 - 2027.
- Kế hoạch dạy học theo định hướng phát triển phẩm chất, năng lực người học cho cả 3 khối 10, 11, 12 theo CT GDPT 2018.
- Các nhóm biện pháp thực hiện then chốt:
  a. Nề nếp dạy học và quản lý học sinh.
  b. Đổi mới phương pháp dạy học: Dạy học giải quyết vấn đề, dạy học dự án, giáo dục STEM/STEAM.
  c. Đổi mới hình thức kiểm tra đánh giá: Kết hợp đánh giá thường xuyên và định kỳ, ma trận đề, bảng đặc tả năng lực.
  d. Kế hoạch bồi dưỡng HSG, hỗ trợ học sinh học tập, ôn thi tốt nghiệp THPT.
  e. Ứng dụng CNTT, chuyển đổi số toàn diện và đưa công nghệ Trí tuệ nhân tạo (AI) vào quản lý, giảng dạy.
  g. Công tác bồi dưỡng chuyên môn nghiệp vụ của đội ngũ nhà giáo.

TRANG 23 - 25: PHẦN B.III - CÔNG TÁC THỰC TẬP SƯ PHẠM 1 TẠI TRƯỜNG THPT THUẬN HÓA
- Ý nghĩa, vị trí và tầm quan trọng sống còn của kỳ TTSP1 đối với việc hình thành năng lực sư phạm của sinh viên.
- Công tác tổ chức, đón tiếp và hướng dẫn chu đáo của Ban chỉ đạo thực tập trường THPT Thuận Hóa.
- Các quy định nghiêm ngặt đối với sinh viên TTSP1 theo Quyết định 2760/QĐ-ĐHSP: Quy chế trang phục, tác phong xưng hô chuẩn mực, thời gian lên lớp, bảo mật hồ sơ, đạo đức lối sống.
- Kế hoạch dự giờ và thực tập: 07 tiết dự giờ chuyên môn + 03 tiết dự giờ công tác chủ nhiệm / HĐTN-HN.

TRANG 26 - 28: PHẦN C - TÌM HIỂU THỰC TẾ CHUYÊN MÔN THEO NGÀNH ĐÀO TẠO
- Phân tích chương trình môn học thuộc ngành của sinh viên đang giảng dạy tại trường THPT Thuận Hóa.
- Nghiên cứu Công văn 5512/BGDĐT-GDTrH và Phụ lục IV: Cấu trúc 4 bước của một Kế hoạch bài dạy chuẩn (Mở đầu/Khởi động -> Hình thành kiến thức -> Luyện tập -> Vận dụng).
- TÍCH HỢP ĐẶC BIỆT: Giải pháp tích hợp **Năng lực số (Digital Competence)** và **Năng lực Trí tuệ nhân tạo (AI Literacy)** vào thiết kế hoạt động học tập (sử dụng công cụ số, phần mềm mô phỏng, tra cứu thông minh).
- Kế hoạch dự giờ 07 tiết chuyên môn: Danh sách các tiết dự giờ dự kiến theo phân công của GVHD bộ môn.

TRANG 29 - 30: PHẦN D - TÌM HIỂU THỰC TẾ CÔNG TÁC CHỦ NHIỆM LỚP
- Vai trò của người GVCN trong mô hình trường THPT trực thuộc trường đại học.
- Đặc điểm tâm sinh lý lứa tuổi học sinh lớp tiếp nhận thực tập (khối 10, 11 hoặc 12).
- Các loại sổ sách chủ nhiệm: Sổ theo dõi học sinh, sổ liên lạc điện tử, hồ sơ quản lý nề nếp chi đoàn.
- Phương pháp phối hợp 3 môi trường: Nhà trường - Gia đình - Xã hội trong giáo dục đạo đức học sinh.
- Kế hoạch dự giờ 03 tiết sinh hoạt lớp / HĐTN-HN vào sáng thứ Bảy hàng tuần.

TRANG 31 - 32: PHẦN E - BÀI HỌC KINH NGHIỆM SƯ PHẠM VÀ PHƯƠNG HƯỚNG RÈN LUYỆN
- Những bài học sâu sắc rút ra sau 1 tuần tiếp xúc thực tế môi trường sư phạm chuyên nghiệp.
- Bài học về tác phong chuẩn mực, kỹ năng giao tiếp với học sinh, đồng nghiệp và phụ huynh.
- Bài học về kỹ năng quan sát, xử lý tình huống sư phạm trên lớp.
- Bản kế hoạch hành động cá nhân chi tiết cho 3 tuần thực tập tiếp theo (tuần 2, 3, 4).

TRANG 33 - 35+: PHẦN F - CÁC PHỤ LỤC MINH CHỨNG THỰC TẾ (HỒ SƠ THỰC TẬP)
- Phụ lục 1: Nhật ký thực tập tuần 1 (Ghi chép chi tiết từ 26/10 đến 01/11/2026).
- Phụ lục 2: Một Kế hoạch bài dạy (KHBD/Giáo án) hoàn chỉnh soạn đúng CV 5512 tích hợp Năng lực số và AI theo chuyên ngành của sinh viên.
- Phụ lục 3: Mẫu phiếu dự giờ chuyên môn (Phụ lục 4 - QĐ 2760) đã được ghi chép tiến trình sư phạm mẫu mực.
- Phụ lục 4: Kế hoạch công tác chủ nhiệm mẫu (Phụ lục 7 - QĐ 2760).
- Trang ký duyệt: Nhận xét và đánh giá của BGH trường THPT Thuận Hóa và GVHD.
========================================================================================
```

---

## 6. KHUNG CÂU HỎI TƯƠNG TÁC BẮT BUỘC (INTERACTIVE QUESTIONNAIRE)

QA Agent **tuyệt đối không được phỏng đoán** thông tin cá nhân của người dùng. Hãy lập tức hiển thị bảng câu hỏi sau để người dùng cung cấp hoặc chọn nhanh:

```markdown
### 📋 BẢNG XÁC NHẬN THÔNG TIN CÁ NHÂN SINH VIÊN THỰC TẬP SƯ PHẠM 1

Để bài thu hoạch được hoàn thiện chính xác 100%, xin bạn vui lòng xác nhận hoặc điền nhanh các thông tin sau:

1. **Họ và tên của bạn là gì?**
   *(Mẹo: Bạn có thể chỉ cần đọc Số Thứ Tự từ 1 đến 46 trong danh sách sinh viên TTSP1 tại trường THPT Thuận Hóa, hệ thống sẽ tự động tra cứu toàn bộ thông tin đi kèm!)*
   - Ví dụ:
     * Nguyễn Trọng Lộc (STT 11 - Trưởng đoàn - SP Công nghệ - GVHD: Thầy Trần Ngọc Đức Toàn)
     * Lê Bội Trân (STT 38 - Phó đoàn - SP Ngữ văn - GVHD: Cô Đàm Thị Mai)
     * Nguyễn Thị Phương Thảo (STT 45 - Phó đoàn - SP Địa lý - GVHD: Cô Lê Nguyễn Tú Trinh)
     * Nguyễn Thảo Duyên (STT 1 - SP Toán học - GVHD: Thầy Trần Ngọc Đức Toàn)
     * Trần Minh Huy (STT 14 - SP Vật Lý - GVHD: Thầy Huỳnh Vũ Long)
     * Phan Thị Thuỳ Dung (STT 19 - SP Hóa học - GVHD: Cô Trương Thị Thu Thảo)
     * Nguyễn Diệu Linh (STT 22 - SP Sinh học - GVHD: Thầy Võ Bá Định)
     * Alăng Along (STT 7 - SP Tin học - GVHD: Thầy Nguyễn Nhất Tân)
     * Bùi Thị Hiền (STT 25 - GD Chính trị - GVHD: Cô Trương Thị Xuân Quỳnh)
     * Vũ Thị Hà (STT 29 - GD Pháp luật - GVHD: Cô Vũ Thị Hợp)
     * Trần Hồng Anh (STT 41 - SP Lịch sử - GVHD: Thầy Võ Thanh Bắc)
     * ...hoặc Họ và tên chính xác của bạn.

2. **Mã số sinh viên (MSSV) và Lớp sinh viên tại ĐH Sư phạm Huế:**
   - Ví dụ: MSSV: 23S1020xxx, Lớp: Sư phạm Tin học K66.

3. **Lớp thực tập chủ nhiệm bạn được phân công tại THPT Thuận Hóa:**
   - Ví dụ: Lớp 10/2, 10/4, 11/1, hay 12/2...?

4. **Chuyên môn bài dạy mẫu theo CV 5512:**
   - Bạn muốn chọn tên bài học nào trong chương trình SGK mới (Kết nối tri thức / Cánh diều / Chân trời sáng tạo) để đưa vào giáo án mẫu phụ lục? (Nếu chưa chọn, Agent sẽ tự động gợi ý một bài học chuẩn mực nhất theo môn của bạn).

5. **Định dạng sản phẩm đầu ra bạn mong muốn:**
   - Bạn muốn Agent tạo file Word (.docx) chuẩn thể thức căn lề 3-2-2-2, Times New Roman 13 hay file Markdown (.md), hay tạo song song cả hai?
```

---

## 7. ĐẦU RA CỦA QA AGENT (EXPECTED OUTPUTS)

Sau khi chạy xong, QA Agent phải bàn giao:
1. **Cấu trúc Repository đã được tổ chức lại** đúng như sơ đồ phân hoạch mục 4, giữ nguyên trạng file gốc trong `01_raw_data/`.
2. **Bộ 7 file Markdown tri thức** trong thư mục `02_extracted_knowledge/` chứa toàn bộ số liệu thực chứng đã được làm sạch và bảng biểu chuẩn.
3. **File thiết kế `03_report_blueprint/pagination_strategy.md` & `master_outline_detailed.md`** chỉ rõ từng trang phải viết những gì để đạt mốc 35 trang.
4. **File `03_report_blueprint/prompt_for_coding_agent.md`** chứa toàn bộ hướng dẫn tối thượng để Coding Agent chỉ việc chạy và sinh ra bài thu hoạch hoàn hảo 35 trang.
5. **File `00_meta/student_profile.json`** được khởi tạo sẵn các trường dữ liệu và cập nhật ngay khi người dùng trả lời.

---

## 8. HƯỚNG DẪN KÍCH HOẠT (EXECUTION TRIGGER)

Hãy bắt đầu ngay bằng cách:
1. Đọc và phân tích cấu trúc tất cả các file hiện có trong thư mục hiện tại.
2. Thực hiện lệnh tái cấu trúc thư mục và chiết xuất dữ liệu.
3. Hiển thị **Bảng xác nhận thông tin cá nhân (Mục 6)** để hỏi tôi các thông tin cần thiết.
4. Đợi tôi xác nhận thông tin cá nhân, sau đó hoàn tất bộ file Blueprint và Knowledge Base để sẵn sàng cho Coding Agent viết bài!
