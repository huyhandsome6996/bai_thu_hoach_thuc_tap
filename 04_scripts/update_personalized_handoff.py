"""Apply the user's confirmed week-one facts and current strict-FORM handoff.
Run after generic build_blueprint.py. Never overwrites raw Office documents.
Existing answers to currently missing questions are preserved.
"""
from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
def write(p,s): (R/p).write_text(s.strip()+'\n',encoding='utf-8')
p=R/'00_meta/student_profile.json'; profile=json.loads(p.read_text(encoding='utf-8'))
activities=[
 {'id':'W1-01','activity':'Hỗ trợ quản lý học sinh và ổn định nề nếp lớp 12/2 trong 15 phút đầu giờ.','date':None,'source':'Người dùng xác nhận','note':'Chưa xác nhận ngày cụ thể hoặc số buổi; không tính là tiết dự giờ chủ nhiệm.'},
 {'id':'W1-02','activity':'Thực hiện 01 video phục vụ tiết mục biểu diễn văn nghệ của học sinh.','date':None,'source':'Người dùng xác nhận','note':'Chưa có tên tiết mục, công cụ, tệp video hoặc đường dẫn minh chứng.'},
 {'id':'W1-03','activity':'Có mặt để cổ vũ, hỗ trợ học sinh trong quá trình tập luyện văn nghệ.','date':None,'source':'Người dùng xác nhận','note':'Không suy thành phụ trách biên đạo hoặc tổ chức toàn bộ chương trình.'},
 {'id':'W1-04','activity':'Hỗ trợ đoàn sinh viên thực tập chuẩn bị và tổ chức 02 trò chơi cho học sinh trong thời gian chờ Ban Giám khảo chấm các tiết mục biểu diễn văn nghệ.','date':None,'source':'Người dùng xác nhận','note':'Chưa có tên trò chơi, luật chơi, số người tham gia hoặc kết quả; không tự thêm.'}
]
profile.update({'status':'partially_confirmed','as_of':'2026-11-01','stt_chuyen_mon':10,'stt_chu_nhiem':30,'ho_ten':'Hồ Quang Huy','ngay_sinh':'2006-02-25','mssv':'24S1020030','nganh':'Sư phạm Tin học','truong_dao_tao':'Trường Đại học Sư phạm, Đại học Huế','noi_thuong_tru':'Sa Pa, Lào Cai','dia_danh_nguoi_dung_cung_cap':'Quê ở Lào Cai (SaPa) (Thường trú)','gvhd_chuyen_mon':'Mai Xuân Văn','gvhd_chu_nhiem':'Nguyễn Thị Thu Phương','mentor_source':'Tra theo họ tên và ngày sinh: TT T0056 (CM10), T0063 (CN30); CN khớp Excel E42, E122. Chờ xác nhận phân công thực tế nếu đã thay đổi.','lop_thuc_tap_chu_nhiem':'12/2','dinh_dang_dau_ra':'docx','confirmed_week1_activities':activities,'observed_lessons':[],'observed_lesson_counts':{'chuyen_mon':0,'chu_nhiem':0,'as_of':'2026-11-01','source':'Người dùng xác nhận chưa được dự giờ chuyên môn hoặc chủ nhiệm.'},'confirmation_note':'Đã nhận thông tin trực tiếp của Hồ Quang Huy. Giữ chính xác lớp 12/2. Chưa biết lớp sinh viên; Sa Pa, Lào Cai được người dùng nêu kèm thường trú, chưa đồng nhất tự động với quê quán trong hồ sơ. Ngày hoạt động, buổi báo cáo/chào cờ và bài KHBD chưa được xác nhận.'})
activities.extend([
 {'id':'W1-05','activity':'Dự lễ chào cờ trong buổi sáng đầu tiên đến trường thực tập.','date':'2026-10-26','time':None,'source':'Người dùng xác nhận','note':'Thứ Hai; chưa xác nhận giờ thực tế bắt đầu chào cờ.'},
 {'id':'W1-06','activity':'Gặp thầy Mai Xuân Văn, giáo viên hướng dẫn chuyên môn.','date':'2026-10-26','time':'09:45','source':'Người dùng xác nhận','note':'Giờ gặp thực tế theo lời người dùng; không thay bằng mốc 9h00 trong kế hoạch chung.'},
 {'id':'W1-07','activity':'Gặp cô Nguyễn Thị Thu Phương, giáo viên hướng dẫn chủ nhiệm lớp 12/2.','date':'2026-10-26','time':'10:30','source':'Người dùng xác nhận','note':'Không tính cuộc gặp GVHD là tiết dự giờ chủ nhiệm.'}
])
profile.update({'status':'core_profile_confirmed','lop_sinh_vien':'Tin3A','que_quan':'Sa Pa, Lào Cai','mentors_confirmed_by_user':True,'mentor_source':'TT T0056 (CM10), T0063 (CN30); chủ nhiệm khớp Excel E42, E122. Người dùng đã xác nhận đúng hai GVHD hiện tại.','confirmation_note':'Đã xác nhận hồ sơ cốt lõi, lớp Tin3A, quê quán ghi Sa Pa, Lào Cai, hai GVHD và lớp thực tập 12/2. Ngày 26/10/2026 dự chào cờ buổi đầu, gặp thầy Mai Xuân Văn lúc 09:45 và cô Nguyễn Thị Thu Phương lúc 10:30. Vẫn chưa dự giờ chuyên môn/chủ nhiệm. Chưa xác nhận tham gia báo cáo BGH/Đoàn trường hoặc ngày cụ thể của các hoạt động văn nghệ/trò chơi.'})
p.write_text(json.dumps(profile,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
c=R/'00_meta/report_context.json'; context=json.loads(c.read_text(encoding='utf-8'))
context.update({'requested_output':'docx','page_count_min':30,'page_count_max':35,'page_count_target':35,'form_policy':'Bám thứ tự FORM gốc A, B.I, B.II.1–6, B.III, tổng kết và nhận xét BGH; không dùng C/D/E/F làm phần chính.','required_observations_entire_placement':{'subject_lessons':7,'homeroom_or_experiential_lessons':3,'completed_counts':{'subject_lessons':0,'homeroom_or_experiential_lessons':0},'completed_counts_as_of':'2026-11-01'}})
c.write_text(json.dumps(context,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
write('00_meta/confirmed_week1_activities.md','''
# Hoạt động tuần đầu của Hồ Quang Huy

Phạm vi 26/10–01/11/2026. Nguồn: lời xác nhận trực tiếp của người dùng trong cuộc trao đổi. Nội dung sau đã biên tập chính tả và diễn đạt, không bổ sung sự kiện.

## Nội dung có thể đưa vào bài

Sáng thứ Hai, ngày 26/10/2026, trong buổi đầu tiên đến Trường THPT Thuận Hóa thực tập, em đã dự lễ chào cờ. Sau đó, em gặp thầy Mai Xuân Văn, giáo viên hướng dẫn chuyên môn, lúc 9 giờ 45 phút và gặp cô Nguyễn Thị Thu Phương, giáo viên hướng dẫn chủ nhiệm lớp 12/2, lúc 10 giờ 30 phút.

Trong tuần thực tập đầu tiên, em đã hỗ trợ quản lý học sinh và ổn định nề nếp lớp 12/2 trong 15 phút đầu giờ. Bên cạnh đó, em thực hiện một video phục vụ tiết mục biểu diễn văn nghệ của học sinh, đồng thời có mặt để cổ vũ và hỗ trợ các em trong quá trình tập luyện.

Đối với hoạt động tập thể, em đã hỗ trợ đoàn sinh viên thực tập chuẩn bị và tổ chức hai trò chơi dành cho học sinh trong thời gian chờ Ban Giám khảo chấm các tiết mục biểu diễn văn nghệ.

Tính đến hết tuần đầu tiên, em chưa được dự giờ chuyên môn hoặc dự giờ chủ nhiệm. Trong các tuần tiếp theo, em sẽ thực hiện nhiệm vụ dự giờ theo kế hoạch và sự phân công của giáo viên hướng dẫn.

## Quy tắc sử dụng

- Lớp thực tập chủ nhiệm ghi **12/2** trong bìa, nội dung, bảng biểu và hồ sơ; không đổi thành 12A2.
- Chưa xác nhận ngày cụ thể, số buổi đầu giờ, tên tiết mục, tên hai trò chơi, số học sinh, phản hồi hoặc kết quả hoạt động. Không chia những việc này thành nhật ký từng ngày theo suy đoán.
- Hoạt động 15 phút đầu giờ và hỗ trợ văn nghệ là tham gia công tác giáo dục, không phải tiết dự giờ chủ nhiệm/HĐTN-HN đã hoàn thành.
- Việc thực hiện video có thể dùng để liên hệ bước đầu với kỹ năng số của sinh viên ngành Sư phạm Tin học. Không nói đã dạy học sinh làm video, đã sử dụng AI hoặc đã đo được năng lực số của học sinh.
- Chưa có tệp video/ảnh trong hồ sơ này; lời xác nhận là nguồn của bản tường thuật, không gọi là đã có minh chứng ảnh/video đính kèm.
- Chào cờ và hai cuộc gặp GVHD ngày 26/10 đã được người dùng xác nhận. Giờ gặp thực tế là 09:45 và 10:30; giữ riêng với lịch dự kiến trong TT T0039. Không suy nội dung trao đổi cụ thể nếu người dùng chưa cung cấp.
- Chưa xác nhận tham gia các buổi nghe báo cáo BGH/Đoàn trường; lịch TTSP chỉ chứng minh việc được bố trí theo kế hoạch.

## Chính tả và cách ghi thống nhất

Hồ Quang Huy; MSSV 24S1020030; ngày sinh 25/02/2006; Sư phạm Tin học; Trường Đại học Sư phạm, Đại học Huế; Trường THPT Thuận Hóa; Sa Pa, Lào Cai; lớp 12/2; giáo viên hướng dẫn chuyên môn; giáo viên hướng dẫn chủ nhiệm; dự giờ chủ nhiệm; biểu diễn văn nghệ; nề nếp; Ban Giám khảo (khi chỉ ban cụ thể của chương trình).

Tên địa danh Sa Pa, Lào Cai được chuẩn hóa theo thông tin người dùng, không tự bổ sung địa chỉ hành chính cấp xã/phường hoặc coi đây là xác minh địa giới hiện hành.
''')
write('00_meta/missing_info_survey.md','''
# Thông tin đã xác nhận và câu hỏi còn lại

Đã có: Hồ Quang Huy; MSSV 24S1020030; sinh 25/02/2006; lớp sinh viên **Tin3A**; ngành Sư phạm Tin học, Trường Đại học Sư phạm, Đại học Huế; lớp thực tập chủ nhiệm **12/2**; quê quán ghi **Sa Pa, Lào Cai** theo xác nhận; đầu ra Word .docx. Người dùng đã xác nhận thầy Mai Xuân Văn và cô Nguyễn Thị Thu Phương là hai GVHD hiện tại. Chưa dự giờ chuyên môn/chủ nhiệm.

## Hồ sơ cốt lõi đã đủ để Coding Agent bắt đầu viết

Không hỏi lại lớp sinh viên, quê quán hoặc tên GVHD. Buổi sáng thứ Hai 26/10/2026: đã dự chào cờ; gặp thầy Mai Xuân Văn lúc 09:45; gặp cô Nguyễn Thị Thu Phương lúc 10:30. Người dùng chưa xác nhận nghe báo cáo BGH/Đoàn trường; có thể trình bày nội dung từ tài liệu mà không khẳng định đã dự các buổi báo cáo này.

## Bổ sung nếu có, không chặn việc viết phần chung

- Ngày hỗ trợ đầu giờ, tập/biểu diễn văn nghệ, tổ chức trò chơi; tên hai trò chơi, tên tiết mục; video/ảnh được phép đưa vào bài. Chưa biết thì tường thuật theo tuần, không dựng lịch theo ngày.
- Tên bài, khối lớp, bộ sách cho KHBD mẫu nếu muốn chuẩn bị phụ lục hồ sơ chuyên môn riêng. Bài tìm hiểu thực tế giáo dục theo FORM không bắt buộc tự thêm toàn bộ giáo án vào bản chính 30–35 trang.
- Sĩ số, cơ cấu lớp và loại hồ sơ thực sự được tiếp cận, nếu được GVHD cung cấp; không tự lấy sĩ số lớp niên độ trước.

Không hỏi lại các dữ liệu đã xác nhận. Ngày ký/ngày nộp thực tế chưa xác nhận; không tự ký lùi ngày.
''')

pages=[
('Trang bìa','Bìa nguồn; hồ sơ Huy','Đúng tên, MSSV, ngành, GVHD và lớp 12/2; không thêm bìa phụ/cam đoan để tăng trang.'),
('Lời cảm ơn','Người dùng; GVHD theo tài liệu','Diễn đạt trang trọng, chỉ cảm ơn việc có căn cứ, không kể đã dự giờ.'),
('Mục lục','Heading Word','TOC tự động theo FORM.'),
('Mục lục tiếp và danh mục','Bảng thực dùng','Chữ viết tắt và danh mục bảng, rút xuống một trang nếu mục lục ngắn.'),
('A. Tóm lược về bản thân','student_profile; roster','Hồ Quang Huy; Tin3A; quê quán Sa Pa, Lào Cai; ngành Tin học; đúng lớp thực tập 12/2 và hai GVHD.'),
('B.I. Hoạt động đầu giờ','confirmed_week1_activities','15 phút đầu giờ ở 12/2; vai trò hỗ trợ, chưa tính là tiết dự giờ.'),
('B.I. Văn nghệ, trò chơi và phương pháp tìm hiểu','Lời người dùng; 9 tài liệu','Một video, hỗ trợ tập luyện, hai trò chơi; các buổi báo cáo chỉ viết đã tham gia khi xác nhận.'),
('B.II.1. Giáo dục địa phương','KH; TK; KB01','Bối cảnh và liên hệ đại học; giới hạn dữ liệu toàn thành phố.'),
('B.II.2.1–2.2. Vị trí và tổng quan','KB01; KB03','Địa chỉ theo người dùng; bảng quy mô hai niên độ, không dựng lịch sử trường.'),
('B.II.2.3. Đội ngũ giáo viên','KB01; KB02; KB05','42 GV niên độ cũ và 56 CB-GV-NV năm mới, đúng mẫu số/phạm vi.'),
('B.II.2.4. Tổ, nhóm chuyên môn','KH P0030–32; KB05','Hai tổ, 11 nhóm; vai trò nhóm Tin học–Công nghệ công nghiệp.'),
('B.II.2.5. Cơ sở vật chất','TK P0112–13; KH P0033–35','Bảng cơ sở riêng/dùng chung, niên độ, không gán số máy chưa có.'),
('B.II.2.5. Khai thác thiết bị và học liệu','KB01; KB03','Phân tích điều kiện dạy Tin học, STEM và kỹ năng số từ tài liệu; đề xuất ghi rõ.'),
('B.II.2.6. Thời gian ra vào lớp','TT T0021–23','Đầy đủ lịch sáng/chiều, 45 phút/tiết; liên hệ tác phong đầu giờ.'),
('B.II.2.7.a. Thành tích tiêu biểu','TK P0073–89','HSG, IOE, KHKT tách cuộc thi/cấp; không đổi thành thành tích cá nhân.'),
('B.II.2.7.b. Kết quả học tập','TK P0091; T0093','Tổng 302 và bảng theo lớp/khối có tính toán ghi rõ; Tốt khác danh hiệu HSG.'),
('B.II.2.7.b. Kết quả rèn luyện','TK P0092; T0093–98','263/31/5/3; so với học tập, giải thích giới hạn suy luận.'),
('B.II.2.8. Thuận lợi, khó khăn','TK; KH P0036–46','Dữ kiện, ảnh hưởng đến tổ chức giáo dục và hàm ý đối với sinh viên.'),
('B.II.3.1–3.2. BGH và BCH Đoàn','KB01; KB04','Hiệu trưởng, Bí thư/hai Phó Bí thư; không bịa nhân sự.'),
('B.II.3.3. Tổ, nhóm và phân công','KB05','Phân công nhiệm vụ, nhóm Tin học; giữ phạm vi tổng tiết và cảnh báo.'),
('B.II.3.4. GVCN năm 2026–2027','KB05','Danh sách GVCN sáng và ghi chú chiều; cô Nguyễn Thị Thu Phương, lớp 12/2.'),
('B.II.4. Hoạt động giáo dục','TK P0027–70; KH','Dạy học, đánh giá, hồ sơ HS, STEM, hướng nghiệp; không kể như đã quan sát tiết dạy.'),
('B.II.5.1–5.2.a,b. Hoạt động Đoàn','KB04','8 chi đoàn, 107 ĐVHS +10 ĐVGV; giáo dục tư tưởng, học tập, giảng dạy.'),
('B.II.5.2.c,d. Phong trào và phát triển tổ chức','KB04; hoạt động Huy','Niên đại thành tích; văn nghệ, thể thao, phát triển Đoàn; liên hệ hỗ trợ hai trò chơi.'),
('B.II.6.1. Mục tiêu','KB03 P0047–57','Mục tiêu giáo dục, đầu ra, đội ngũ và quản trị; phân tích có nguồn.'),
('B.II.6.2. Kế hoạch dạy học','KB03 P0082–104; P0176','35 tuần, HKI18/HKII17; lựa chọn và buổi 2 đúng điều kiện.'),
('B.II.6.3. Kế hoạch tổ chức hoạt động','KH T0178','Mốc tháng 10–11 và nhiệm vụ cả năm, người phụ trách/sản phẩm.'),
('B.II.6.4. Các chỉ tiêu','KB03 P0058–81','Bảng đối chiếu nền cũ với mục tiêu mới, đúng dấu ≥/≤ và điểm phần trăm.'),
('B.II.6.5. Biện pháp thực hiện','KB03 Phần III','Đủ nề nếp, chương trình, PPDH, hỗ trợ/HSG, đánh giá, đội ngũ, CNTT/AI, môi trường thân thiện.'),
('B.III.1. Vai trò TTSP1','KB07; hoạt động tuần đầu','Nhận thức nghề từ quản lý đầu giờ, video, hỗ trợ tập thể; không tổng kết bốn tuần.'),
('B.III.2. Công tác hướng dẫn','TT T0039; P0025–46; người dùng','Ngày 26/10 đã chào cờ; gặp thầy Văn 09:45, cô Phương 10:30. Phân biệt lịch dự kiến và giờ gặp thực tế.'),
('B.III.3. Yêu cầu TTSP1','KB07 PL1–10','7+3 tiết là kế hoạch, hiện 0+0; nội quy, trình đề cương, ghi phiếu, rút kinh nghiệm và các hạn.'),
('B.IV. Tổng kết: bài học tuần đầu','Hoạt động Huy; dữ liệu trường','Bài học gắn sự kiện đã xác nhận; giới hạn chưa dự giờ và chưa có đủ hồ sơ lớp.'),
('B.IV. Tổng kết: phương hướng','TT; kế hoạch cá nhân','Ba tuần tới, sản phẩm và mốc hạn; liên hệ Sư phạm Tin học, số/AI là đề xuất; danh mục nguồn.'),
('B.V. Nhận xét của BGH nhà trường','FORM T0068','Giữ nội dung nhận xét, ngày ký, chữ ký và điểm trống cho người có thẩm quyền; không tạo trang trắng giả.')]
lines=['# Chiến lược phân trang theo FORM gốc cho Hồ Quang Huy','',
'''## Yêu cầu đang có hiệu lực

Theo xác nhận mới nhất: xuất **Word .docx, tổng 30–35 trang vật lý A4, mục tiêu 35 trang**, bám đúng thứ tự FORM gốc. Quy định này thay thế phương án C/D/E/F và phương án gộp khoảng 40 trang trước đây. Đếm cả bìa và trang nhận xét; chưa có quy định nguồn loại trừ các trang này, cần ghi rõ cách đếm trong QA.

Không thêm phần C/D/E/F như các phần chính; tìm hiểu chuyên môn, chủ nhiệm và rèn luyện được tích hợp đúng các mục B liên quan. KHBD đầy đủ, phiếu dự giờ mẫu và kế hoạch chủ nhiệm đầy đủ chỉ soạn thành tài liệu chuẩn bị riêng khi có yêu cầu; không phải minh chứng đã dự giờ tuần 1 và không bắt buộc chèn vào bài tìm hiểu thực tế giáo dục này. Không tự cho phép vượt 35 trang.

FORM có hai mục IV liên tiếp; dùng IV. Tổng kết và V. Nhận xét của BGH để sửa số thứ tự, giữ nguyên tên và vị trí nội dung. Nếu GVHD yêu cầu nguyên xi số mục, dùng lại số IV của nguồn, không tự đổi cấu trúc khác.

## Định mức và điều chỉnh

A4, lề trái 3 cm, ba lề còn lại 2 cm, TNR 13, Multiple 1.2, Before/After 0 pt. Khởi tạo khoảng 400–500 đơn vị tách bằng khoảng trắng ở trang văn xuôi, 250–350 ở trang có bảng; chỉ là ước tính. Dùng khoảng 10.500–13.000 đơn vị cho bản thảo kể cả nội dung bảng rồi đo bằng render, không lấy số từ thay số trang. Không tăng giãn dòng, thu nhỏ font, lặp đoạn hoặc chèn ngắt trang tùy tiện để đạt độ dài.

## Ngân sách từng trang
''','| Trang vật lý | Đề mục trong FORM | Nguồn | Nội dung và kiểm soát |','| --- | --- | --- | --- |']
lines += [f'| {i} | {a} | {b} | {d} |' for i,(a,b,d) in enumerate(pages,1)]
lines += ['', '''## Điều kiện nghiệm thu

1. Mục tiêu 35, chấp nhận 30–35 trang sau khi cập nhật TOC/danh mục và render lại. Chưa render thì không được báo bảo đảm số trang thực tế.
2. Bản >35 trang: gộp các đoạn trùng, rút phần lý luận chung, tóm tắt phân công ngoài phạm vi; không xóa nội dung bắt buộc FORM. Bản <30 trang: bổ sung phân tích theo lớp/khối từ bảng thật, đối chiếu chỉ tiêu, điều kiện dạy học, nhiệm vụ giáo viên, giới hạn và phương hướng có căn cứ.
3. Trang 35 nhận xét dành diện tích đúng mẫu để ký, không dùng làm trang trắng kéo dài. Nếu tổng bản chỉ 32–34 trang mà đã đủ nội dung và đúng form thì chấp nhận, không ép lên 35.
4. Không tự nhận đã dự giờ để viết dài: tuần 1 chuyên môn 0, chủ nhiệm 0; hoạt động hỗ trợ đầu giờ vẫn có thể phân tích về tổ chức lớp và trách nhiệm thực tập.
5. Lưu số trang vật lý, số trang hiển thị, cấu hình định dạng và kết quả kiểm tra mọi trang trong `05_final_report/qa_report.md`.
''']
write('03_report_blueprint/pagination_strategy.md','\n'.join(lines))

# Rebuild the H4 outline from the actual FORM's headings, preserving its order.
src=json.loads((R/'04_scripts/extracted_sources/FORM BÀI THU HOẠCH TÌM HIỂU THỰC TẾ GIÁO DỤC TTSP1.json').read_text(encoding='utf-8'))
out=['# Dàn ý chi tiết theo FORM gốc cho Hồ Quang Huy','',
'''Bản này thay thế cấu trúc mở rộng C/D/E/F trước đây. Nguồn chuẩn: FORM P0002–P0068; bìa theo tệp bìa; thể thức theo tệp Hình thức. Giữ A, B.I, B.II.1–6, B.III, tổng kết và nhận xét; sửa mục IV trùng cuối thành V khi không có chỉ dẫn khác của GVHD. Tham chiếu ngân sách từng trang trong pagination_strategy.md.

Hồ Quang Huy, MSSV 24S1020030, sinh 25/02/2006, lớp Tin3A, ngành Sư phạm Tin học, quê quán Sa Pa, Lào Cai, lớp thực tập chủ nhiệm 12/2. Hai GVHD đã được xác nhận. Đọc hồ sơ JSON và confirmed_week1_activities.md trước khi viết ngôi thứ nhất. Ngày 26/10 dự chào cờ, gặp thầy Văn 09:45 và cô Phương 10:30. Hiện chưa dự giờ chuyên môn hoặc chủ nhiệm.
''','## Trang bìa và lời cảm ơn','','Trang 1–2. Dùng đúng bìa nguồn; không thêm bìa phụ và cam đoan để kéo dài. Mục lục/danh mục trang 3–4 là phần hỗ trợ tra cứu.']
for b in src:
    if 'text' not in b: continue
    n=int(b['id'][1:]); t=b['text']
    if n<4 or n>67: continue
    if n==4: level='## '; note='Trang 5. Điền đúng các trường bên dưới từ hồ sơ; quê quán không tự đồng nhất với nơi thường trú.'
    elif 5<=n<=13: level='#### '; note='Dữ liệu từ student_profile.json; trường chưa xác nhận giữ chờ trong dự thảo, không tự suy.'
    elif n==14: level='## '; note='Phần chính của bài; tuần 1 và số liệu tài liệu được tách rõ.'
    elif n in (15,19,62,66,67):
        level='### '; note={15:'Trang 6–7. Dùng bốn nhóm hỗ trợ đã xác nhận và chào cờ/gặp GVHD ngày 26/10 (09:45 thầy Văn, 10:30 cô Phương); buổi báo cáo chưa xác nhận chỉ ghi theo tài liệu.',19:'Trang 8–29. Trình bày đủ sáu nhóm kết quả tìm hiểu theo đúng thứ tự dưới đây.',62:'Trang 30–32. Dùng KB07; 7+3 là yêu cầu cả đợt, hiện 0+0. Không dựng quan sát tiết dạy.',66:'Trang 33–34. Bài học sau tuần đầu và kế hoạch ba tuần còn lại; không viết như tổng kết cả đợt.',67:'Trang 35 hoặc trang cuối trong khoảng 30–35. Để BGH/GVHD nhận xét và ký; không tạo lời nhận xét giả.'}[n]
        if n==67:t='V. NHẬN XÉT CỦA BGH NHÀ TRƯỜNG'
    elif n==61: out+=['',t,'']; continue
    else:
        level='#### '
        note=('Nguồn KB01/KB02, đối chiếu KH và TK theo niên độ.' if 20<=n<=33 else
              'Nguồn KB01/KB04/KB05. GVCN 12/2 là cô Nguyễn Thị Thu Phương theo bảng; không dùng lớp 12A2.' if 34<=n<=38 else
              'Nguồn TK/KB03. Bao gồm nhiệm vụ giáo viên, hồ sơ và đánh giá học sinh để đủ tiêu chí PL8; chưa có quan sát thì nêu theo tài liệu.' if n==39 else
              'Nguồn KB04; thành tích quá khứ ghi đúng năm. Liên hệ hỗ trợ hai trò chơi nhưng không nhận phụ trách toàn chương trình.' if 40<=n<=46 else
              'Nguồn KB03; chỉ tiêu là dự kiến 2026–2027, không đổi thành kết quả. Có bảng so sánh, nguồn và phân tích ý nghĩa sư phạm.' if 47<=n<=60 else
              'Nguồn KB07 và hoạt động tuần 1 đã xác nhận; nội quy, trách nhiệm, quy trình đề cương–dự–rút kinh nghiệm, các hạn nộp.')
    out += [level+t,'',note,'']
out+=['## Điểm triển khai phải bao phủ','',
'''- B.II.2.7: bảng kết quả học tập/rèn luyện 302 học sinh, phân tích theo lớp hoặc khối từ T0093; danh hiệu và giải thi tách rõ.
- B.II.3–4: nhiệm vụ giáo viên, tổ nhóm, hồ sơ học sinh và cách đánh giá; không gọi các hồ sơ dự kiến là đã xem.
- B.II.6.5: đủ biện pháp theo FORM, gồm đổi mới PPDH, bồi dưỡng, đánh giá và CNTT; liên hệ ngành Tin học từ công việc làm video, không tự nhận đã dùng AI.
- B.III: bảng tiến độ 7+3 tiết ở dạng kế hoạch. Có thể mô tả chuẩn bị KHBD theo 5512 và năng lực số/AI, không cần thêm một phần C ngoài FORM.
- B.IV: bài học gắn hỗ trợ 15 phút đầu giờ, một video, cổ vũ tập luyện và hai trò chơi; nêu đúng giới hạn chưa dự giờ. Kế hoạch các tuần 2–4 dùng thì tương lai.
- Toàn bài: duyệt chính tả, dấu câu, tên riêng và viết hoa; mỗi bảng có tên, niên độ, mẫu số và mã nguồn. Không đưa toàn danh sách 46 sinh viên vào để tăng trang.
''']
write('03_report_blueprint/master_outline_detailed.md','\n'.join(out))
print('Updated confirmed profile, week-one facts and strict FORM 30–35-page blueprint.')
