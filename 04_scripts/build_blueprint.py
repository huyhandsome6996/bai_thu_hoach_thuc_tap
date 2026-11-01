"""Create QA handoff; does not author a student's report or confirmed observations."""
from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
def write(p,s): (R/p).write_text(s.strip()+'\n',encoding='utf-8')
profile=R/'00_meta/student_profile.json'
if not profile.exists():
    profile.write_text(json.dumps({'status':'awaiting_user','as_of':'2026-11-01','stt_chuyen_mon':None,'stt_chu_nhiem':None,'ho_ten':None,'ngay_sinh':None,'que_quan':None,'mssv':None,'lop_sinh_vien':None,'khoa':None,'nganh':None,'gvhd_chuyen_mon':None,'gvhd_chu_nhiem':None,'lop_thuc_tap_chu_nhiem':None,'bai_day_mau':None,'khoi_lop_bai_day':None,'bo_sach':None,'dinh_dang_dau_ra':None,'confirmed_week1_activities':[],'observed_lessons':[],'confirmation_note':'Chưa nhận phản hồi; không coi danh sách rỗng là xác nhận không tham gia. STT mặc định theo bảng chuyên môn; ghép CN theo tên + ngày sinh.'},ensure_ascii=False,indent=2),encoding='utf-8')
write('00_meta/missing_info_survey.md','''
# Bảng xác nhận thông tin sinh viên

Chưa có thông tin cá nhân được xác nhận. Điền vào `student_profile.json` sau khi người dùng trả lời; null không có nghĩa là không tồn tại.

| STT | Câu hỏi cần trả lời | Ghi chú |
| --- | --- | --- |
| 1 | Họ tên sinh viên hoặc STT 1–46? | STT mặc định theo bảng **chuyên môn** trong file tri thức 06. Nếu dùng bảng chủ nhiệm hãy ghi rõ. |
| 2 | MSSV và lớp sinh viên tại ĐHSP Huế? | Ví dụ 23S1020xxx, Sư phạm Toán K66; không lấy ví dụ làm dữ liệu. |
| 3 | Lớp thực tập chủ nhiệm được phân công? | Cần cả buổi nếu trường phân công sáng/chiều. |
| 4 | Tên bài học làm KHBD mẫu tích hợp năng lực số và AI? | Nếu chưa chọn, đề xuất sau khi biết ngành; cần khối lớp và bộ SGK. |
| 5 | Định dạng đầu ra muốn nộp? | Word .docx, Markdown .md hoặc cả hai. |

Thông tin bổ sung để xuất bản cuối: ngày sinh năm đầy đủ, quê quán (mẫu yêu cầu); khoa nếu có dùng; hoạt động đã tham gia ngày 26/10–01/11, tiết đã dự (ngày/giờ/môn/bài/lớp/GV), hồ sơ thực sự đã xem, ghi chép/ảnh được phép dùng. Có thể hỏi theo đợt sau khi tra cứu 5 câu chính; không dựng nhật ký từ lịch kế hoạch.
''')
pages=[
('Bìa chính','Mẫu BIA; hồ sơ cá nhân','Bìa đúng cơ quan, tiêu đề, GVHD, thời gian; không thêm cơ quan không có trên bìa nguồn.',0),
('Bìa phụ và cam đoan','BIA; hồ sơ cá nhân','Bìa phụ rút gọn ở nửa trên; cam đoan trung thực tài liệu và phạm vi quan sát ở nửa dưới.',150),
('Lời cảm ơn','Thông tin GVHD đã xác nhận','Cảm ơn gắn việc được hướng dẫn; tránh kể các sự kiện chưa xác nhận.',250),
('Mục lục','Outline và Word TOC','Mục lục tự động mức 1–3; H4 nằm trong nội dung, không ép TOC 4 cấp nếu tràn.',0),
('Viết tắt và danh mục bảng','Các bảng thực dùng','Giải nghĩa GDPT, TTSP, GVHD, HĐTN-HN, CNTT, AI; danh mục bảng và nguồn.',120),
('A.1 Hồ sơ sinh viên','student_profile; KB06','Lý lịch theo mẫu: tên, ngày sinh, quê, trường, ngành, lớp, hai GVHD.',250),
('A.2 Định hướng nghề nghiệp','KB01; thông tin người học','Mục tiêu tìm hiểu môi trường phổ thông, tự đánh giá ban đầu; phân biệt kỳ vọng với kết quả.',450),
('B.I.1 Báo cáo ngày đầu','KB07 TT T0039','Bảng lịch 26/10 (7h; 8h; 8h30; 9h); cột tham gia/minh chứng do người dùng xác nhận.',350),
('B.I.2 Phương pháp tìm hiểu','9 nguồn và nhật ký thật','Mô tả đọc hồ sơ, nghe báo cáo, quan sát/trao đổi đã có; nêu giới hạn dữ liệu.',450),
('B.II.1 Giáo dục địa phương','KH căn cứ; TK liên kết ĐHSP','Phạm vi TP. Huế theo văn bản; quan hệ nhà trường–đại học–địa phương; không bịa thống kê toàn thành phố.',450),
('B.II.2.1–2.4 Vị trí và quy mô','KB01; KB03','Bảng quy mô hai năm có mốc đầu/cuối; đội ngũ và tổ nhóm; phân biệt mẫu số.',350),
('B.II.2.5–2.6 CSVC và giờ học','KB01','Bảng phòng học/phòng chức năng, điều kiện dùng chung; bảng khung giờ và ý nghĩa tổ chức.',300),
('B.II.2.7–2.8 Kết quả và điều kiện','KB02','Bảng tổng kết học tập/rèn luyện; bảng 7 giải HSG; thuận lợi/khó khăn dựa trên số liệu.',350),
('B.II.3 Cơ cấu tổ chức','KB01; KB04; KB05','HT, BCH Đoàn, hai tổ, nhóm môn; sơ đồ chỉ quan hệ đã có nguồn, thiếu tên thì ghi chưa có.',350),
('B.II.3.4 Phân công đội ngũ','KB05','Bảng 13 GVCN buổi sáng, ghi chú phân công chiều; trách nhiệm tổ/nhóm và phụ trách phòng bộ môn.',300),
('B.II.4 Hoạt động giáo dục','TK P0027–70; KH','Dạy học, đánh giá, STEM/Robotics, câu lạc bộ, hướng nghiệp; ví dụ có nguồn, không kể như đã chứng kiến.',450),
('B.II.5.1 Tổ chức Đoàn','KB04 P0005–18','8 chi đoàn, 107 HS+10 GV; BCH 10/BTV 3; thuận lợi và khó khăn.',350),
('B.II.5.2 Các mặt hoạt động','KB04','Phân tích bốn mảng, thành tích có niên đại; tách lịch sử và kế hoạch 2026–2027.',450),
('B.II.6.1 Mục tiêu và chỉ tiêu','KB03 P0047–81','Bảng chỉ tiêu so với nền 2025–2026; nói rõ mục tiêu chưa phải thành tích.',350),
('B.II.6.2 Kế hoạch dạy học','KB03 P0082–104; P0176','35 tuần 18+17; môn lựa chọn, buổi 2, tự nguyện và không quá tải; trách nhiệm thực hiện.',450),
('B.II.6.3–6.5 Biện pháp','KB03 P0105–148; P0158–73','PPDH, STEM, hỗ trợ theo nhóm, kiểm tra đánh giá, bồi dưỡng đội ngũ; sản phẩm kiểm tra.',450),
('B.II.6.5.h Chuyển đổi số và AI','KB03 P0149–57; T0178','LMS360, học bạ số, AI kiểm chứng; bảng việc–phụ trách–sản phẩm tháng 10/11.',350),
('B.III.1 Vai trò TTSP1','KB07 PL5, PL8','Liên hệ học phần với quan sát thực tế và phẩm chất nghề; không viết TTSP1 là thực dạy TTSP2.',450),
('B.III.2 Công tác hướng dẫn','KB07 TT P0025–46','BCĐ, tổ/nhóm, GVHD, trưởng đoàn; ba hạn 02/11, 17/11, 18/11 và tổng kết 21/11.',350),
('B.III.3 Nội quy và hồ sơ','KB07 PL1–10','Ma trận 7+3 tiết, quy trình đề cương–dự–rút kinh nghiệm–ký; trọng số tiêu chí.',350),
('C.1 Tìm hiểu môn học','Ngành đã xác nhận; KH; SGK chờ bổ sung','Yêu cầu cần đạt, tiến độ, SGK, hồ sơ bộ môn; chỉ dẫn chương trình có nguồn.',450),
('C.2 Thiết kế KHBD số và AI','KB07; bài học đã chọn','Ma trận mục tiêu–nhiệm vụ–sản phẩm–đánh giá; có phương án thiếu mạng/thiết bị.',350),
('C.3 Kế hoạch 7 tiết dự giờ','KB07 TT P0033–35','7 dòng CM01–07: dự kiến ngày, GV, bài/lớp, đề cương, phiếu, trạng thái; để trống lịch chưa có.',300),
('D.1 Công tác chủ nhiệm','Lớp đã xác nhận; KB07 PL3,7','Hồ sơ lớp thực sự tiếp cận, lứa tuổi chỉ là cơ sở lý luận; không bịa sĩ số/hoàn cảnh.',450),
('D.2 Phối hợp và 3 tiết HĐTN-HN','KB07 TT T0039; PL7,10','Bảng CN01–03; lịch dự kiến thứ Bảy 07/11,14/11,21/11 cần GVHD xác nhận; phối hợp gia đình–nhà trường–xã hội.',350),
('E.1 Bài học sau tuần 1','Quan sát cá nhân xác nhận; KB02/03','Mỗi bài học gắn dữ kiện, ý nghĩa và điều chỉnh hành vi; chưa có quan sát thì chỉ rút bài học từ tài liệu.',450),
('E.2 Kế hoạch ba tuần tiếp','KB07 mốc hạn','Tuần 2 02–08/11, tuần 3 09–15/11, tuần 4 16–21/11; việc, sản phẩm, người kiểm tra, hạn.',350),
('F.1 Nhật ký và nguồn tài liệu','Nhật ký thật; danh mục 9 nguồn','Bảng ngày/việc/minh chứng/trạng thái; danh mục tài liệu đủ tên, số/ngày nếu có, không điền khống.',250),
('F.2 Tóm tắt KHBD đề xuất','C.2; phụ lục KHBD đầy đủ riêng','Mục tiêu, học liệu, bốn hoạt động, thời gian, minh chứng số/AI; dẫn file KHBD đầy đủ, không gọi bản tóm tắt là toàn văn.',300),
('F.3–5 Biểu mẫu và nhận xét','KB07 PL4,7; FM T0068','Mẫu trích yếu phiếu dự giờ và kế hoạch chủ nhiệm, dẫn bản đầy đủ riêng; khu vực nhận xét/chữ ký để trống.',150),
]
rows='\n'.join(f'| {i} | {a} | {b} | {c} | {d or "Không áp định mức"} |' for i,(a,b,c,d) in enumerate(pages,1))
write('03_report_blueprint/pagination_strategy.md',f'''
# Chiến lược phân trang bài thu hoạch TTSP1

## Phạm vi và quy ước đếm

Mục tiêu **35 trang vật lý A4 cho bản chính**, tính cả bìa và phụ lục tóm tắt. Có 5 trang thủ tục, 27 trang A–E và 3 trang F. Trang vật lý trong bảng khác số hiển thị ở footer nếu bỏ số bìa; bảng QA phải ghi cả hai. Người dùng yêu cầu mở rộng C/D/E/F so với FORM; đó là cấu trúc mở rộng được chọn, không tuyên bố nguyên bản FORM có các phần này.

**Giới hạn thực tế:** ba trang 33–35 không đủ để chứa đồng thời nhật ký, KHBD đầy đủ, phiếu dự giờ, kế hoạch chủ nhiệm và chỗ ký thoáng ở cỡ 13. Vì vậy cấu hình 35 trang dùng phụ lục tóm tắt trong bản chính, còn **phụ lục đầy đủ thành tệp riêng**, không tính vào 35. Nếu phải gộp toàn văn: giữ trang 1–32, trang 33 nhật ký + nguồn, trang 34–37 KHBD đủ hoạt động/học liệu/đánh giá, trang 38 phiếu dự giờ, trang 39 kế hoạch chủ nhiệm, trang 40 nhận xét và ký. Đây là phương án 40 trang, vượt mục tiêu 30–35, chỉ dùng khi người dùng chấp nhận nộp 35+. Không cắt font/giãn dòng để che vượt trang. Chưa chọn định dạng đầu ra, Coding Agent cần ghi rõ cấu hình khi xuất.

## Định mức ban đầu

A4 21×29,7 cm, vùng nội dung 16×25,7 cm trước khoảng cách header/footer. TNR13, Multiple1.2 thường cho khoảng 40–46 dòng hữu dụng mỗi trang; tùy chữ và bảng, khởi tạo khoảng 400–500 đơn vị tách bằng khoảng trắng/trang văn xuôi, 250–350 ở trang nhiều bảng. Đây là ước tính kỹ thuật, không phải quy định số từ. Cột dưới là mục tiêu lời văn sơ bộ (tổng {sum(p[3] for p in pages):,} đơn vị, chưa tính nội dung bảng), phải hiệu chỉnh bằng render.

## Kế hoạch từng trang

| Trang vật lý | Nội dung | Nguồn cần đọc | Sản phẩm và điểm kiểm soát | Định mức lời văn sơ bộ |
| --- | --- | --- | --- | --- |
{rows}

## Cơ chế dàn trang và điều chỉnh

1. Viết theo cụm mục, lưu từng phần tại `05_final_report/sections/`; không page-break mỗi đoạn để cưỡng bức đủ trang.
2. Dùng ngắt trang ở bìa, thủ tục và đầu phần lớn. Bảng tự giãn hàng, lặp header, cột nằm trong 16 cm; không ép cả bảng dài vào một trang, không để một tiêu đề lẻ cuối trang.
3. Render bản đầu, cập nhật TOC/danh mục, render lại vì TOC làm đổi trang. Lập bảng trang thực tế so với mục tiêu và kiểm tra toàn bộ trang, nhất là 13,15,22,25,28,30,34–35.
4. Nếu quá 35 trang: bỏ lặp số liệu, chuyển danh sách 46 SV và toàn bảng phân công vào kho tham chiếu, chỉ giữ dữ liệu cần thiết trong báo cáo; phụ lục đầy đủ để riêng. Nếu thiếu 30 trang: bổ sung phân tích dữ kiện→ý nghĩa→biện pháp, ma trận minh chứng, giới hạn và đối chiếu chỉ tiêu; không nhân bản đoạn văn hoặc chèn trang trắng.
5. Ghi số trang thực đo và cấu hình vào biên bản QA; chưa render thì chỉ gọi đây là blueprint 35 trang, không cam kết file Word đã đạt 35.
''')

outline=[
('A. TÓM LƯỢC VỀ BẢN THÂN','6–7','student_profile + KB06',[
('A.1 Lý lịch và phân công',[('A.1.1 Thông tin cá nhân','Họ tên, ngày sinh, quê quán, MSSV, lớp, ngành; null phải chờ xác nhận.'),('A.1.2 Mối quan hệ hướng dẫn','Hai GVHD; lớp chủ nhiệm; bảng chuyên môn/CN khác STT.')]),
('A.2 Mục tiêu học tập nghề nghiệp',[('A.2.1 Nhận thức ban đầu','Gắn CTGDPT2018 với năng lực quan sát, soạn đề cương, tự học.'),('A.2.2 Cam kết rèn luyện','Đúng giờ, bảo mật, trung thực với hồ sơ và AI; thể hiện mục tiêu cá nhân.')])]),
('B.I HOẠT ĐỘNG ĐÃ THỰC HIỆN','8–9','KB07 TT T0039; xác nhận người dùng',[
('B.I.1 Nghe báo cáo',[('B.I.1.1 Ngày tiếp nhận 26/10','Lịch 7h/8h/8h30/9h là kế hoạch, chỉ đổi sang đã tham gia khi có xác nhận.'),('B.I.1.2 Thông tin thu nhận','Ghi người báo cáo, nội dung, tài liệu và câu hỏi nếu thực có.')]),
('B.I.2 Nghiên cứu và điều tra',[('B.I.2.1 Hồ sơ và tài liệu','Liệt kê 9 nguồn có thật, mục đích đọc, cách đối chiếu niên độ.'),('B.I.2.2 Quan sát và trao đổi','Ghi ngày, đối tượng, phạm vi được tiếp cận; chưa có thì nêu hạn chế, không dựng phỏng vấn.')])]),
('B.II.1 TÌNH HÌNH GIÁO DỤC ĐỊA PHƯƠNG','10','KH căn cứ và TK',[
('B.II.1.1 Phạm vi tìm hiểu',[('B.II.1.1.a Bối cảnh địa phương','Dùng TP. Huế theo tài liệu năm 2026; không dùng thống kê hoặc địa giới cũ khi chưa kiểm chứng.'),('B.II.1.1.b Vai trò nguồn lực đại học','Quan hệ ĐHSP–THPT, nguồn chuyên gia, thư viện, trải nghiệm di sản.')]),
('B.II.1.2 Giới hạn và hàm ý',[('B.II.1.2.a Những gì chưa có','Chưa có số trường, quy mô HS toàn thành phố, tỷ lệ phổ cập hay kinh phí.'),('B.II.1.2.b Liên hệ nghề nghiệp','Đề xuất khai thác học liệu địa phương và phối hợp, không khẳng định thành tích chưa chứng minh.')])]),
('B.II.2 ĐẶC ĐIỂM TÌNH HÌNH NHÀ TRƯỜNG','11–13','KB01; KB02; KB03',[
('B.II.2.1 Vị trí',[('B.II.2.1.a Địa chỉ và trực thuộc','Địa chỉ do người dùng cung cấp; trực thuộc theo đầu văn bản.'),('B.II.2.1.b Lịch sử','Chỉ viết nếu bổ sung nguồn năm thành lập; không suy ra từ năm hoạt động Đoàn.')]),
('B.II.2.2 Tổng quan',[('B.II.2.2.a Quy mô 2025–2026','310 đầu năm, 302 cuối năm, 12 lớp; không suy giảm 8 em đồng nghĩa bỏ học.'),('B.II.2.2.b Quy mô 2026–2027','13 lớp,346 HS; khối10 185/6,11 18/1,12 143/6.')]),
('B.II.2.3 Đội ngũ',[('B.II.2.3.a Niên độ cũ','42 GV:1 TS,22 ThS,19 CN; nếu tính tỷ lệ dùng đúng mẫu số42.'),('B.II.2.3.b Niên độ mới','56 người và cơ cấu KH; không gộp với thống kê cũ hoặc 68 dòng công tác Excel.')]),
('B.II.2.4 Tổ nhóm',[('B.II.2.4.a Hai tổ','KHTN,KHXH.'),('B.II.2.4.b Mười một nhóm','Liệt kê đúng KH P0032, nhóm ghép khác môn đơn lẻ.')]),
('B.II.2.5 Cơ sở vật chất',[('B.II.2.5.a Cơ sở riêng','12→13 phòng học theo niên độ;15 phòng chức năng năm mới.'),('B.II.2.5.b Dùng chung','Phòng thí nghiệm Sinh, thư viện, giảng đường và thiết bị ĐHSP; không tự gán số máy.')]),
('B.II.2.6 Thời gian',[('B.II.2.6.a Buổi sáng','Bảng TT T0021 đầy đủ.'),('B.II.2.6.b Buổi chiều','Bảng TT T0023;45phút/tiết; liên hệ quy định không vào trễ.')]),
('B.II.2.7 Kết quả giáo dục',[('B.II.2.7.a Thành tích','7 giải HSG thành phố,IOE tách riêng; nguồn TK P0073–89.'),('B.II.2.7.b Học tập và rèn luyện','Bảng tổng hợp302 HS; phân tích 104/161/37 và263/31/5/3;10HSXS,92HSG khác phân loại Tốt.')]),
('B.II.2.8 Thuận lợi khó khăn',[('B.II.2.8.a Thuận lợi','Nguồn lực ĐHSP, quan tâm phụ huynh và đội ngũ; có dẫn nguồn.'),('B.II.2.8.b Khó khăn','Đội ngũ cơ hữu mỏng, đầu vào không đều, năng lực số; đề xuất giải pháp có căn cứ.')])]),
('B.II.3 CƠ CẤU TỔ CHỨC','14–15','KB01; KB04; KB05',[
('B.II.3.1 Ban Giám hiệu',[('B.II.3.1.a Hiệu trưởng','Dương Đức Giáp; nguồn TK/TT.'),('B.II.3.1.b Bộ máy khác','Chưa có tên PHT/HĐT; không dựng nhân sự.')]),
('B.II.3.2 Ban Chấp hành Đoàn',[('B.II.3.2.a Nhân sự','Bí thư,hai phó,7ủy viên chưa nêu tên.'),('B.II.3.2.b Phối hợp','Vai trò giáo dục và hỗ trợ TTSP, không vẽ quan hệ cấp trên suy đoán.')]),
('B.II.3.3 Tổ nhóm và Công đoàn',[('B.II.3.3.a Phân công chuyên môn','Đối chiếu Excel, nêu nhiệm vụ TTCM/NTBM.'),('B.II.3.3.b Công đoàn','Đàm Thị Mai ghi Chủ tịch Công đoàn tại E67; không suy ra toàn BCH.')]),
('B.II.3.4 Chủ nhiệm',[('B.II.3.4.a Danh sách sáng','13 GVCN theo E và dòng HĐTN-HN; không dùng GVCN niên độ cũ.'),('B.II.3.4.b Ghi chú chiều','Phân biệt GVCN chiều và hỏi lại nếu liên quan lớp SV.')])]),
('B.II.4 HOẠT ĐỘNG GIÁO DỤC','16','KB02 TK P0027–70;KB03',[
('B.II.4.1 Dạy học và kiểm tra',[('B.II.4.1.a Dạy học tích cực','Vai trò GV tổ chức, HS thực hiện; ví dụ theo nguồn.'),('B.II.4.1.b Đánh giá','Quá trình/định kỳ, sản phẩm, phản hồi; không chép quy định pháp lý chưa kiểm tra.')]),
('B.II.4.2 STEM và trải nghiệm',[('B.II.4.2.a CLB','MOS-AI,STEM Robotics,ngoại ngữ,nghệ thuật,thể thao theo TK P0060.'),('B.II.4.2.b Hướng nghiệp','Di sản và tham quan có niên độ; không biến kế hoạch thành trải nghiệm cá nhân.')])]),
('B.II.5 HOẠT ĐỘNG ĐOÀN','17–18','KB04',[
('B.II.5.1 Tình hình chung',[('B.II.5.1.a Quy mô','8chi đoàn,107ĐVHS,10ĐVGV; BCH10,BTV3.'),('B.II.5.1.b Điều kiện','Sự hỗ trợ và hạn chế do số đoàn viên ít.')]),
('B.II.5.2 Các mặt hoạt động',[('B.II.5.2.a Tư tưởng đạo đức','Nề nếp,di tích,lịch sử; tách hoạt động truyền thống với tuần1.'),('B.II.5.2.b Học tập giảng dạy','HSG,bồi dưỡng,tự học,đổi mới CNTT.'),('B.II.5.2.c Văn hóa TDTT','Giải bóng đá lầnVI đang tổ chức; thành tích cũ ghi đúng năm.'),('B.II.5.2.d Phát triển tổ chức','Kết nạp Đoàn,giới thiệu học nhận thức Đảng; không tự khai số kết nạp Đảng.')])]),
('B.II.6 KẾ HOẠCH GIÁO DỤC 2026–2027','19–22','KB03',[
('B.II.6.1 Mục tiêu',[('B.II.6.1.a Định hướng','Chất lượng đầu ra, số/AI, an toàn, đội ngũ.'),('B.II.6.1.b Quản trị','06 rõ và trách nhiệm giải trình.')]),
('B.II.6.2 Kế hoạch dạy học',[('B.II.6.2.a Thời lượng','35tuần,18+17; môn lựa chọn theo nguyện vọng.'),('B.II.6.2.b Hai buổi','Không chuyển nội dung bắt buộc sang buổi2; tự chọn phù hợp điều kiện.')]),
('B.II.6.3 Tổ chức hoạt động',[('B.II.6.3.a Tháng10–11','TTSP,nề nếp,20/11,dữ liệu,kiểm tra; người phụ trách và sản phẩm từ T0178.'),('B.II.6.3.b Cả năm','Các mốc tháng khác chọn lọc theo trọng tâm, không sao toàn bảng.')]),
('B.II.6.4 Chỉ tiêu',[('B.II.6.4.a Học sinh','Tốt≥35%,Khá≥53%,Đạt≤12%;RL Tốt≥90%,Khá≥8%;TN100% là mục tiêu.'),('B.II.6.4.b Đội ngũ và dữ liệu','100% tiếp cận bồi dưỡng;100% chuẩn hóa dữ liệu;chuyên đề ít nhất1.')]),
('B.II.6.5 Biện pháp',[('B.II.6.5.a Nề nếp và chương trình','Quản lý tiến độ, hồ sơ, không cắt xén.'),('B.II.6.5.b Đổi mới PPDH','Vấn đề,dự án,STEM; mục tiêu và điều kiện tổ chức.'),('B.II.6.5.c Bồi dưỡng hỗ trợ','HSG,phụ đạo,ôn thi theo nhóm,phân tích dữ liệu.'),('B.II.6.5.d Kiểm tra đánh giá','Chuẩn hóa,ma trận,phản hồi tiến bộ.'),('B.II.6.5.e Phát triển đội ngũ','Tự học,sinh hoạt chuyên môn,KPI theo sản phẩm.'),('B.II.6.5.h CNTT và AI','LMS360,học bạ số,AI kiểm chứng,an toàn dữ liệu.'),('B.II.6.5.i Môi trường học đường','Nhân văn,an toàn,hỗ trợ tâm lý,phối hợp cha mẹ.')])]),
('B.III CÔNG TÁC TTSP1','23–25','KB07',[
('B.III.1 Vai trò',[('B.III.1.1 Học nghề từ thực tế','Quan sát và phản tư; không nhận đã đứng lớp nếu chưa dạy.'),('B.III.1.2 Kết nối học phần','Từ lý luận đến kế hoạch rèn luyện.')]),
('B.III.2 Tổ chức hướng dẫn',[('B.III.2.1 Trách nhiệm','BCĐ,tổ,GVHD,trưởng đoàn,SV.'),('B.III.2.2 Mốc hồ sơ','02/11 tìm hiểu;17/11 giảng dạy/CN;18/11 GVHD;21/11 tổng kết14h.')]),
('B.III.3 Yêu cầu',[('B.III.3.1 Nội quy','Trang phục,đúng giờ,quan hệ và tham gia họp.'),('B.III.3.2 Tiêu chí','PL8 20+20+60; PL9/10 30+70; đề cương,phiếu và rút kinh nghiệm.')])]),
('C. TÌM HIỂU THỰC TẾ CHUYÊN MÔN','26–28','KB03;KB05;KB07;ngành người dùng',[
('C.1 Chương trình và hồ sơ',[('C.1.1 Yêu cầu môn học','Chờ ngành,khối,SGK và kế hoạch tổ; không tự chọn bài đã dạy.'),('C.1.2 Hồ sơ chuyên môn','Kế hoạch giáo dục tổ/GV,KHBD,học liệu,công cụ đánh giá.')]),
('C.2 KHBD mẫu đề xuất',[('C.2.1 Liên kết mục tiêu','Mục tiêu–hoạt động–sản phẩm–đánh giá; dẫn khung5512 đã đối chiếu.'),('C.2.2 Năng lực số và AI','Hành vi: tìm nguồn,phân tích,kết luận độc lập,kiểm chứng AI;rubric và phương án không mạng.')]),
('C.3 Bảy tiết dự giờ',[('C.3.1 Ma trận tiến độ','CM01–07; chưa có ngày thì để chờ GVHD;SP Công nghệ4+3.'),('C.3.2 Quy trình mỗi tiết','Đề cương trước,ghi phiếu trong giờ,hội ý sau và ký xác nhận.')])]),
('D. TÌM HIỂU THỰC TẾ CÔNG TÁC CHỦ NHIỆM','29–30','profile;KB07 PL3,7,10',[
('D.1 Hồ sơ và đặc điểm lớp',[('D.1.1 Dữ liệu lớp','Sĩ số,nam/nữ,cán bộ lớp chỉ dùng bản được phép tiếp cận.'),('D.1.2 Tâm lý và nhu cầu','Phân biệt lý luận tuổi THPT với nhận xét về lớp thực tế.')]),
('D.2 Tổ chức giáo dục',[('D.2.1 Ba môi trường','Quy trình trao đổi GVHD/phụ huynh,không nhận đã trao đổi khi chưa có.'),('D.2.2 Ba tiết HĐTN-HN','CN01–03,thứBảy theo phân công;ngày dự kiến phải được GVHD xác nhận.')])]),
('E. BÀI HỌC VÀ PHƯƠNG HƯỚNG','31–32','Tài liệu;trải nghiệm đã xác nhận',[
('E.1 Bài học',[('E.1.1 Tác phong và quan sát','Dữ kiện→bài học→điều chỉnh;không sáo rỗng hoặc khen chung.'),('E.1.2 Chuyên môn và chủ nhiệm','Một hạn chế tự nhận có căn cứ,một cách khắc phục đo được.')]),
('E.2 Kế hoạch rèn luyện',[('E.2.1 Tuần2–3','02–15/11 hoàn thiện đề cương/dự giờ và nhận góp ý;theo lịchGVHD.'),('E.2.2 Tuần4','17/11 nộp,18/11 đánh giá,21/11 tổng kết;không viết thành kết quả đã đạt.')])]),
('F. PHỤ LỤC VÀ NHẬN XÉT','33–35 trong bản chính','KB07;minh chứng thật',[
('F.1 Nhật ký và nguồn',[('F.1.1 Nhật ký tuần1','Ngày,hoạt động,trạng thái,minh chứng;tách kế hoạch và hoàn thành.'),('F.1.2 Danh mục tài liệu','9 nguồn gốc và nguồn khung5512;không tự thêm mã văn bản bỏ trống.')]),
('F.2 KHBD và biểu mẫu',[('F.2.1 Bản tóm tắt trong báo cáo','Dẫn phụ lục toàn văn riêng theo pagination_strategy.'),('F.2.2 Phiếu và kế hoạch chủ nhiệm','Theo PL4,PL7;chỉ mô phỏng nếu thiếu quan sát;không điền giả xác nhận.')]),
('F.3 Nhận xét và ký',[('F.3.1 Ban Giám hiệu','Để trống nội dung đánh giá,điểm,chữ ký,con dấu.'),('F.3.2 Sinh viên','Thống nhất ngày nộp thật;không ký thay.')])])]
out=['# Dàn ý chi tiết bài thu hoạch TTSP1','',
'''## Cách đọc và tương thích mẫu

KB01…KB07 là 7 tệp theo số trong `02_extracted_knowledge/`. Mỗi nhánh có nguồn và trang đích. H1 là tên dàn ý, H2 là phần lớn, H3 là mục, H4 là tiểu mục. Khi viết phải giữ đầy đủ nội dung bắt buộc FORM A, B.I, B.II.1–6, B.III, tổng kết và nhận xét. FORM gốc in trùng hai mục IV; cấu trúc mở rộng người dùng chọn chuyển tổng kết sang E và nhận xét sang F. Các phần C/D là tìm hiểu sơ bộ và kế hoạch, không thay hai bài thu hoạch chuyên môn/chủ nhiệm cuối đợt.

Để bám PL8, ngoài các mục FORM phải làm rõ nhiệm vụ GV ở B.II.3/4, hồ sơ HS ở D.1, đánh giá/xếp loại ở B.II.2.7 và B.II.4; bài học ở E. Không coi danh mục hồ sơ dự kiến là hồ sơ đã được xem. Chi tiết luật/điều lệ mới chỉ dẫn theo tài liệu trường cung cấp, cần kiểm tra nguồn chính thức nếu diễn giải thêm.
''']
for title,pg,src,children in outline:
    out+=['## '+title,'',f'Trang đích: {pg}. Nguồn: {src}.','']
    for mid,leaves in children:
        out+=['### '+mid,'']
        for leaf,body in leaves: out+=['#### '+leaf,'',body,'']
out+=['## Bảng biểu phải có','',
'B01 quy mô hai năm; B02 CSVC riêng/dùng chung; B03 giờ học; B04 học tập và rèn luyện302 HS; B05 giảiHSG/IOE tách cấp; B06 tổ chức và13GVCN sáng; B07 cơ cấuĐoàn; B08 chỉ tiêu2026–2027; B09 việc chuyển đổi số tháng10/11; B10 hạn và thành phần hồ sơTTSP; B11 kế hoạch7tiết; B12 kế hoạch3tiết; B13 rèn luyện ba tuần. Đánh số lại theo thứ tự xuất hiện, mỗi bảng có chú thích niên độ, mẫu số và mã nguồn. Không đưa toàn danh sách HS/SV vào bài để kéo dài trang.']
write('03_report_blueprint/master_outline_detailed.md','\n'.join(out))
print('Wrote profile, survey, 35-page strategy and H4 outline')
# Apply the later user-confirmed strict FORM requirement and personal facts.
import runpy
runpy.run_path(str(R/'04_scripts/update_personalized_handoff.py'), run_name='__main__')
