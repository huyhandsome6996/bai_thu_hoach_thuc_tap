"""Build the seven knowledge files and normalized lookup data from extraction JSON."""
from pathlib import Path
import json, re, unicodedata, zipfile, xml.etree.ElementTree as ET
from parse_all_docs import render, W, text_of
R=Path(__file__).resolve().parents[1]; X=R/'04_scripts/extracted_sources'; K=R/'02_extracted_knowledge'
names={'TT':'1. Kế hoạch TTSP1 năm 2026-2027','KH':'2.10.26. Kế hoạch giáo dục nhà trường 2026-2027','TK':'Báo cáo tổng kết năm học 2025 -2026.chốt','DT':'BAO_CAO_DOAN_TTSP1_THANG_10','QD':'vt_phu_luc_kem_theo_qd_2760_qd-dhsp','XL':'Phân công giảng dạy HK1 năm học 2026- 2027','FM':'FORM BÀI THU HOẠCH TÌM HIỂU THỰC TẾ GIÁO DỤC TTSP1','HT':'Hình thức làm bài thu hoạch (1)','BIA':'Bìa bài thu hoạch trường'}
D={k:json.loads((X/(v+'.json')).read_text(encoding='utf-8')) for k,v in names.items()}
def table(headers,rows):
    esc=lambda x:str(x).replace('|','\\|').replace('\n','<br>')
    return '\n'.join(['| '+' | '.join(headers)+' |','| '+' | '.join('---' for _ in headers)+' |']+['| '+' | '.join(map(esc,r))+' |' for r in rows])
def source(k,blocks=None):
    ext='.xlsx' if k=='XL' else '.doc' if k in ('TK','QD') else '.docx'
    return f"## Dữ liệu nguồn {k}\n\nNguồn: `01_raw_data/{names[k]}{ext}`. Mã P/T là vị trí đoạn/bảng theo thứ tự XML, không phải số trang Word. Bảng C1… giữ cấu trúc ô nguồn; bảng chuẩn hóa phía trên dùng để viết bài.\n\n"+render(D[k] if blocks is None else blocks)
def save(file,title,summary,parts):
    (K/file).write_text('# '+title+'\n\nChốt dữ liệu ngày 01/11/2026. Phân biệt kết quả 2025–2026, kế hoạch 2026–2027 và trải nghiệm cá nhân chưa xác nhận.\n\n'+summary+'\n\n'+'\n\n'.join(parts),encoding='utf-8')
def select(k,lo,hi): return [b for b in D[k] if lo<=int(b['id'][1:])<=hi]
save('01_thong_tin_nha_truong.md','Thông tin nhà trường và điều kiện tổ chức giáo dục',
'''## Thông tin dùng nhanh

- Cơ sở tiếp nhận: Trường THPT Thuận Hóa, trực thuộc Trường Đại học Sư phạm, Đại học Huế (đầu văn bản KH, TK, TT).
- Địa chỉ 34 Lê Lợi, TP. Huế do người dùng cung cấp; chưa thấy xác nhận trong phần văn bản trích xuất. Không tự thêm năm thành lập, quyết định thành lập hoặc lịch sử.
- Hiệu trưởng Dương Đức Giáp (TT T0050; TK T0168). TK P0108 ghi 01 CBQL; chưa có căn cứ liệt kê Phó Hiệu trưởng hay Hội đồng trường hiện tại.
- Năm 2025–2026: đầu năm 12 lớp/310 HS, cuối năm 12 lớp/302 HS. Cơ hữu 10 người gồm BGH 1, GV 7, NV 2; TK P0025 nêu 35 GV thỉnh giảng, P0108 nêu 42 GV giảng dạy với 1 tiến sĩ, 22 thạc sĩ, 19 cử nhân. Không lấy 45 người làm mẫu số cho cơ cấu 42 GV.
- Năm 2026–2027: 13 lớp/346 HS (10: 6 lớp/185; 11: 1 lớp/18; 12: 6 lớp/143), 56 CB-GV-NV gồm HT 1, GV 52, NV văn phòng 2, giám thị 1 (KH P0020–27). Cộng cơ cấu môn tại P0026–27 ra 52 người; đây là số ghi theo môn, chưa phải kiểm đếm cá nhân duy nhất.
- Hai tổ KHTN, KHXH và 11 nhóm chuyên môn (KH P0030–32). Phòng học tăng từ 12 trong TK lên 13 trong KH. KH P0033 ghi 15 phòng chức năng nhưng các hạng mục liệt kê cộng được 15; không tính trùng cơ sở dùng chung của ĐHSP.
- Nguồn chung: thư viện, giảng đường I, phòng thí nghiệm, phòng máy của ĐHSP. Phòng thí nghiệm Sinh dùng chung; chưa có phòng chuyên môn Âm nhạc, Mỹ thuật (TK P0113).
- Tiết học 45 phút. Sáng ổn định 7h–7h10, tiết 1 7h10–7h55, tiết 2 8h–8h45, tiết 3 9h–9h45, tiết 4 9h50–10h35, tiết 5 10h40–11h25. Chiều tiết 6 13h10–13h55, 7 14h–14h45, 8 14h50–15h35, 9 15h40–16h25, 10 16h30–17h15 (TT T0021–23). Lịch đón đoàn 26/10 ghi 7h00 là mốc riêng.

## Phân tích có thể triển khai

Lợi thế nguồn lực đại học hỗ trợ STEM, thực hành và hướng nghiệp; cần phân biệt tài sản riêng với quyền sử dụng. Đội ngũ thỉnh giảng giúp mở rộng chuyên môn nhưng gây khó phối hợp lịch. Đây là diễn giải dựa trên TK và KH, không phải kết quả phỏng vấn.

## Khoảng trống

Thiếu lịch sử trường, sơ đồ phòng chi tiết, số máy tính, số đầu sách, tên đầy đủ các thành viên bộ máy và số liệu toàn ngành giáo dục địa phương. Không biến những khoảng trống này thành dữ kiện.''',
[source('TK',select('TK',1,25)+select('TK',105,115)),source('KH',select('KH',17,46)),source('TT',select('TT',19,24))])

tkrows=next(b['rows'] for b in D['TK'] if b['id']=='T0093')
classes=[r for r in tkrows if len(r)==13 and r[0].isdigit() and r[3]=='SL']
norm=[[r[1],r[2]]+[x or '0' for x in r[4:12]]+[r[12]] for r in classes]
summary='''## Kết quả tổng hợp đã kiểm tra

Nguồn TK P0091–94, T0093. Mẫu số cuối năm 302 HS. Học tập Tốt 104 (34,44%), Khá 161 (53,31%), Đạt 37 (12,25%), Chưa đạt 0. Rèn luyện Tốt 263 (87,09%), Khá 31 (10,26%), Đạt 5 (1,66%), Chưa đạt 3 (0,99%). Hai nhóm đều cộng đủ 302; tỷ lệ hai chữ số thập phân cộng 100%.

Không đồng nhất mức học tập Tốt với danh hiệu HSG/HSXS. P0094 ghi 10 HSXS (khối 12: 8, khối 11: 2), 92 HSG (khối 12: 64, khối 11: 26, khối 10: 2); T0096 có 10 tên, T0098 có 92 tên.

### Bảng học tập và rèn luyện theo lớp

Ô SL trống trong bảng này quy đổi 0 để đối chiếu tổng; bảng gốc bên dưới giữ ô trống. HT = học tập, RL = rèn luyện. Danh sách GVCN này thuộc 2025–2026.

'''+table(['Lớp','Sĩ số','HT Tốt','HT Khá','HT Đạt','HT CĐ','RL Tốt','RL Khá','RL Đạt','RL CĐ','GVCN'],norm)+'''

### Thành tích dùng để phân tích

- Thi HSG cấp Thành phố: Ngữ văn 1 KK; Lịch sử 1 Ba và 2 KK; Tiếng Anh 1 Nhì; GD KT-PL 2 Nhì. Tổng 7 giải, không đổi thành giải quốc gia (TK P0079–84).
- IOE: 1 Ba khối 12 toàn quốc, 1 Ba và 1 KK khối 12 toàn thành phố, 1 Nhất cấp trường (P0085–89).
- KHKT/Sáng tạo và mô hình sách: xem nguyên văn P0073–78, không gộp các cuộc thi khác nhau thành HSG văn hóa.

### Dữ liệu chưa được chứng minh

Không tìm thấy tỷ lệ tốt nghiệp thực tế năm 2026, tỷ lệ đỗ đại học, quyết định công nhận kiểm định mức 2/chuẩn quốc gia mức 1 trong báo cáo. 100% tốt nghiệp là CHỈ TIÊU của KH 2026–2027 (P0071). Báo cáo TK đề ngày 15/5/2026, trước kỳ thi tốt nghiệp; không suy ra kết quả kỳ thi. Kế hoạch tuyển sinh 250 chỉ tiêu/8 lớp là dự kiến trong TK P0152, khác quy mô thực tế KH P0020–23.
'''
save('02_so_lieu_tong_ket_2025_2026.md','Kết quả và số liệu năm học 2025–2026',summary,[source('TK',select('TK',26,104)+select('TK',116,168))])
save('03_ke_hoach_giao_duc_2026_2027.md','Kế hoạch giáo dục năm học 2026–2027',
'''## Văn bản và chỉ tiêu chính

Đầu văn bản ghi 145/KH-THPT ngày 15/9/2026; dòng ban hành kèm theo ghi 145/QĐ-THPT cùng ngày. Giữ cả hai cách dẫn theo vị trí, không tự sửa thành một mã. Các căn cứ pháp lý năm 2026 dưới đây là nội dung tài liệu do người dùng cung cấp; chưa xác minh hiệu lực độc lập.

| Nhóm | Chỉ tiêu, kế hoạch | Vị trí KH |
| --- | --- | --- |
| Thời lượng | 35 tuần thực học; HKI 18, HKII 17 | P0090, P0176 |
| Học tập | Tốt ≥35%; Khá ≥53%; Đạt ≤12%; Chưa đạt thấp nhất | P0069 |
| Rèn luyện | Tốt ≥90%; Khá ≥8%; Đạt/Chưa đạt thấp nhất | P0070 |
| Sĩ số | Duy trì từ 99% | P0068 |
| Tốt nghiệp | 100% lớp 12 đủ điều kiện dự thi; tốt nghiệp 100% | P0071 |
| Năng lực số và AI | 100% CB-GV được tiếp cận, bồi dưỡng; 100% HS được giáo dục kỹ năng số, an toàn mạng, tiếp cận AI phù hợp | P0062, P0074 |
| Dữ liệu và học bạ | 100% dữ liệu rà soát, chuẩn hóa; 100% học bạ số tạo từ dữ liệu gốc, duyệt/ký số/đồng bộ | P0063–64 |
| Chuyên môn | Mỗi tổ/nhóm ít nhất 1 chuyên đề/sản phẩm áp dụng thực tế | P0066 |
| Đổi mới | Ít nhất 1 mô hình/CLB đổi mới trọng điểm | P0078 |

## Cách dùng khi viết

Phân tích đầy đủ chín nhóm nhiệm vụ của Phần III trong nguồn. Tách mục tiêu, biện pháp, người phụ trách và sản phẩm theo tháng. So sánh kết quả 2025–2026 với mục tiêu mới chỉ khi cùng chỉ báo: học tập Tốt 34,44% → ≥35%, rèn luyện Tốt 87,09% → ≥90%; chênh lệch là điểm phần trăm, không phải tỷ lệ tăng trưởng.

KH P0153–55 nêu LMS360, học liệu số, dạy học kết hợp, AI có kiểm chứng và trách nhiệm của giáo viên. Đây là kế hoạch triển khai, chưa chứng minh mọi lớp đã thực hiện. Tích hợp AI trong bài mẫu là thiết kế đề xuất, không phải tiết đã dạy.''',
[source('KH')])
save('04_hoat_dong_doan_thanh_nien.md','Hoạt động Đoàn và phong trào thanh niên',
'''## Tổ chức và mốc thời gian

Báo cáo ngày 26/10/2026 về hoạt động Đoàn và phong trào thanh niên năm học 2026–2027. Có 8 chi đoàn (7 HS, 1 GV); 107 đoàn viên HS và 10 đoàn viên GV, tổng cộng 117 đoàn viên (tổng tính toán). Không lấy 107 làm tổng toàn trường. BCH 10 đồng chí: Bí thư Trương Thị Thu Thảo; Phó Bí thư Nguyễn Hữu Nhanh Tiến và Đoàn Thị Phương Dung; 7 ủy viên chưa nêu tên. Ban Thường vụ 3 đồng chí (DT P0005–11).

## Nội dung phân tích

Giáo dục tư tưởng/đạo đức, học tập/giảng dạy, văn hóa/TDTT, phát triển đoàn viên và giới thiệu đoàn viên ưu tú. Các thành tích 2017–2026 là dữ liệu lịch sử được báo cáo lại; không viết là thành tích tuần đầu TTSP hoặc năm học mới. Giải bóng đá lần VI được mô tả là đang tổ chức năm 2026–2027 (P0050). Phần kế hoạch tháng 8/2026 đến 7/2027 là dự kiến theo văn bản, không coi ngày đã qua là bằng chứng hoàn thành.

8 chi đoàn không bằng 13 lớp: chỉ so sánh cơ cấu tổ chức Đoàn với quy mô lớp, chưa có căn cứ giải thích lớp nào chưa có chi đoàn. Phong trào Học sinh 3 tốt nếu chưa có mô tả/tiêu chí trong nguồn thì ghi đề xuất hoặc nội dung cần hỏi, không khẳng định số lượng đạt danh hiệu.''',
[source('DT')])

# Preserve all worksheet records, grouping continuation tasks only until the next teacher or subject.
sheet=D['XL'][0]; teachers=[]; subjects=[]; current=None; subject=''
for row in sheet['rows']:
    vals={re.sub(r'\d','',k):v for k,v in row.items()}; rn=int(re.sub(r'\D','',next(iter(row))))
    b=vals.get('B','').strip()
    if re.match(r'^\d+\.',b):
        subject=b; subjects.append([rn,b,vals.get('F',''),vals.get('G','')]); current=None
    elif b and 9<=rn<=126:
        current={'row':rn,'subject':subject,'name':b,'unit':vals.get('C',''),'degree':vals.get('D',''),'tasks':[],'total':vals.get('G','')}; teachers.append(current)
    if current is not None and vals.get('E'): current['tasks'].append(f"E{rn}: {vals['E']} [F{rn}={vals.get('F','trống')}]")
gvrows=[]
for t in teachers:
    for task in t['tasks']:
        for match in re.finditer(r'GVCN\s+(\d+/\d+)([^;\n]*)',task): gvrows.append([match[1],t['name'],match[0],f"B{t['row']}; "+task.split(':')[0]])
save('05_phan_cong_chuyen_mon_gv.md','Phân công chuyên môn và chủ nhiệm học kỳ I 2026–2027',
'''## Quy tắc đọc bảng

Nguồn XL có một sheet `HK1 SÁNG có đăng kí ngày dạy`, ký ngày 05/9/2026. Phần công tác có cả dòng kiêm nhiệm và ghi chú buổi chiều; không hiểu tổng tiết là riêng tiết đứng lớp. Ô G là giá trị cache của công thức, chưa tính lại bằng Excel. Ô tên trống chỉ nối nhiệm vụ trong cùng nhóm GV, không tự điền trình độ trống.

### Sai khác cần giữ nguyên và hỏi lại

- F8/G8 Toán =79, cộng các ô F9:F26 và G9:G26 đều bằng79; tổng này gồm cả công tác kiêm nhiệm, không gọi79 là riêng tổng tiết đứng lớp môn Toán.
- F27/G27 Vật lý =24 khớp SUM(F29:F36) và SUM(G29:G36), nhưng công thức đều bỏ dòng28=3 của Dương Đức Giáp. Tổng bao gồm dòng28 là27. Cần hỏi lại phạm vi thống kê, không tự sửa24 thành27.
- F79 Địa lí =17 trong cache, F80:F82 chỉ có 17, bỏ F83=5; G79=17 trong cache trong khi G80:G82=17 và toàn nhóm có 22. Không tự sửa nguồn hoặc cộng chéo để chốt số tiết.
- Trần Văn Dũng: dòng D32 ghi Cử nhân, D115 ghi Thạc sĩ. Hoàng Đức Vương: D24 Cử nhân, D123 Thạc sĩ. Giữ sai khác, không tự xác nhận học vị.
- Ghi chú môn Ngữ văn có 10/3 và 11/1 được nêu ở nhiều GV; cần xác nhận phạm vi buổi/nhóm, không tự kết luận phân công sai.
- Không có lớp 11/2–11/4 trong bảng này; khối 11 năm mới có một lớp 11/1 theo KH.

## Tổng theo nhóm nguyên trạng

'''+table(['Dòng','Nhóm môn','F cache và công thức','G cache và công thức'],subjects)+
'\n\n## Danh sách phân công giáo viên và toàn bộ nhiệm vụ\n\n'+table(['Dòng tên','Nhóm','Giáo viên','Đơn vị','Trình độ nguồn','Nhiệm vụ và ô','G nguồn'],[[t['row'],t['subject'],t['name'],t['unit'],t['degree'],'<br>'.join(t['tasks']),t['total']] for t in teachers])+
'\n\n## Tra cứu GVCN theo lớp và buổi\n\n'+table(['Lớp','Giáo viên','Ghi chú nguyên văn','Ô nguồn'],gvrows),
['## Toàn bộ ô có dữ liệu\n\n'+(X/(names['XL']+'.md')).read_text(encoding='utf-8')])

def merged_table(index):
    with zipfile.ZipFile(R/'01_raw_data'/(names['TT']+'.docx')) as z: body=ET.fromstring(z.read('word/document.xml')).find(W+'body')
    tb=[e for e in body if e.tag==W+'tbl'][index]; rows=[]; active={}
    for tr in tb.findall(W+'tr'):
        row=[]; col=0
        for tc in tr.findall(W+'tc'):
            pr=tc.find(W+'tcPr'); vm=pr.find(W+'vMerge') if pr is not None else None
            s=text_of(tc)
            if vm is not None:
                if vm.get(W+'val')=='restart': active[col]=s
                else: s=active.get(col,s)
            else: active.pop(col,None)
            row.append(s); col+=1
        rows.append(row)
    return rows
# Find table index from source XML, rather than relying on a human-facing STT.
with zipfile.ZipFile(R/'01_raw_data'/(names['TT']+'.docx')) as z: body=ET.fromstring(z.read('word/document.xml')).find(W+'body')
tabs=[e for e in body if e.tag==W+'tbl']
cm=merged_table(len(tabs)-3); cn=merged_table(len(tabs)-1)
def key(r): return unicodedata.normalize('NFC',' '.join((r[1]+' '+r[2]).split())).upper(),r[3]
cnmap={key(r):r for r in cn if r[0].isdigit()}
roster=[]
for r in cm:
    if not r[0].isdigit(): continue
    n=cnmap[key(r)]
    roster.append({'stt_chuyen_mon':int(r[0]),'stt_chu_nhiem':int(n[0]),'ho_ten':key(r)[0],'ngay_sinh_nguon':r[3],'nganh':r[4],'gioi_tinh_nguon':r[5] or None,'gvhd_chuyen_mon':r[6],'gvhd_chu_nhiem':n[7],'chuc_vu':n[6] or None})
assert len(roster)==46 and len(cnmap)==46 and all(x['gvhd_chuyen_mon'] and x['gvhd_chu_nhiem'] for x in roster)
(R/'00_meta/student_roster.json').write_text(json.dumps(roster,ensure_ascii=False,indent=2),encoding='utf-8')
save('06_danh_sach_46_sinh_vien_ttsp1.md','Danh sách 46 sinh viên và hai phân công hướng dẫn',
'''## Quy tắc định danh

Khi người dùng chỉ nhập STT, mặc định là STT chuyên môn trong bảng chuẩn hóa dưới đây, cần nhắc rõ hệ quy chiếu. Hai bảng nguồn TT T0056 và T0063 sắp thứ tự khác nhau; ghép bằng HỌ TÊN + NGÀY SINH, không ghép theo STT. Tên GVHD của ô gộp dọc được triển khai theo thuộc tính vMerge của OOXML, không điền suy đoán. Ngày sinh giữ nguyên dạng hai số năm như tài liệu, không tự xác nhận năm đầy đủ. Lớp thực tập chủ nhiệm cần người dùng xác nhận, có thể đối chiếu file 05 theo GVHD nhưng không tự gán vì có phân công buổi chiều.

Chú ý sửa ví dụ trong prompt cũ: Nguyễn Trọng Lộc có STT chuyên môn 17, chủ nhiệm 11, ngành SP Công nghệ, GVHD chuyên môn Hồ Đắc Thái Sơn và Nguyễn Thị Hiền, GVHD chủ nhiệm Trần Ngọc Đức Toàn. Nguyễn Thị Phương Thảo có GVHD chuyên môn Trương Thị Bình, chủ nhiệm Lê Nguyễn Tú Trinh. Không dùng ví dụ cũ thay bảng nguồn.

'''+table(['STT CM','STT CN','Họ tên','Ngày sinh nguồn','Ngành','GVHD CM','GVHD CN','Chức vụ'],[[r['stt_chuyen_mon'],r['stt_chu_nhiem'],r['ho_ten'],r['ngay_sinh_nguon'],r['nganh'],r['gvhd_chuyen_mon'],r['gvhd_chu_nhiem'],r['chuc_vu'] or ''] for r in roster]),
[source('TT',select('TT',51,64))])
save('07_quy_che_va_bieu_mau_dhsp.md','Quy chế TTSP và biểu mẫu sử dụng',
'''## Phân biệt ba sản phẩm và các hạn nộp

TT T0039 và P0040–46: bài tìm hiểu thực tế giáo dục nộp sau tuần 1, hạn 02/11/2026. Bài thu hoạch giảng dạy/chủ nhiệm cùng 7 đề cương + 7 phiếu chuyên môn, 3 đề cương + 3 phiếu chủ nhiệm nộp chậm nhất 17/11. GVHD đánh giá, nộp hồ sơ 18/11; tổng kết 14h ngày 21/11. Bài nộp 02/11 không được nhận đã hoàn tất toàn bộ hồ sơ cuối đợt.

Mỗi SV dự 7 tiết chuyên môn và 3 tiết chủ nhiệm/HĐTN-HN; riêng SP Công nghệ gồm 4 tiết công nghiệp và 3 tiết nông nghiệp, hai GVHD. Tiết chủ nhiệm/HĐTN-HN theo phân công thứ Bảy. Đề cương phải trình GVHD trước giờ dự; ghi chép thực tế, hội ý rút kinh nghiệm và ký xác nhận sau đó.

## Bản đồ phụ lục và tiêu chí chấm

| Phụ lục | Phạm vi | Cách dùng |
| --- | --- | --- |
| 1 | Nội quy | Đúng giờ, xin phép, tác phong, ứng xử, nhiệm vụ chuyên môn |
| 2–3 | Hướng dẫn dự giờ môn học và chủ nhiệm | Chuẩn bị, quan sát GV/HS, rút kinh nghiệm |
| 4 | Phiếu dự giờ | Thời gian; hoạt động GV; hoạt động HS; nhận xét theo tiến trình; tổng kết; nhận xét GVHD/chữ ký |
| 5 | Thu hoạch thực tế giáo dục | Phương pháp, kết quả, bài học sư phạm |
| 6 | Kế hoạch công tác thực tập GIẢNG DẠY | Bảng tuần/nội dung/dự kiến kết quả/ghi chú, KHÔNG phải mẫu giáo án 5512 |
| 7 | Kế hoạch công tác chủ nhiệm | Yêu cầu; tình hình lớp; phương hướng; kế hoạch theo tuần |
| 8 | Chấm tìm hiểu thực tế GD | 20 ý thức + 20 phương pháp + 6 tiêu chí kết quả ×10 =100 |
| 9 | Chấm TT giảng dạy TTSP1 | Bài thu hoạch 30; dự giờ 70 (chuẩn bị 35, ghi chép 20, rút kinh nghiệm 15) |
| 10 | Chấm TT chủ nhiệm TTSP1 | Bài thu hoạch 30 (15+15); dự giờ 70 (35+20+15) |
| 11–13 | Nhận xét, tổng kết, kết quả TTSP1 | Để người có thẩm quyền nhận xét/cho điểm/ký |
| 14–24 | Các mẫu TTSP2 | Chỉ lưu tham chiếu; không áp dụng thay mẫu TTSP1 |

Tên tệp gợi QĐ 2760/QĐ-ĐHSP nhưng tệp chỉ chứa phụ lục, không có toàn văn quyết định, ngày ký hoặc xác nhận hiệu lực hiện tại. Dẫn theo tên bộ phụ lục được cung cấp; không tự thêm ngày ban hành.

## Hình thức và yêu cầu KHBD

Theo HT P0002–15: Times New Roman 13, đen; Before/After 0 pt, Multiple 1.2, first line 1–1,27 cm, Justify, A4; trái 3 cm, trên/dưới/phải 2 cm; nếu đánh số thì chính giữa footer. Tích hợp năng lực số và AI là yêu cầu trong tài liệu HT địa phương, không tuyên bố là nguyên văn yêu cầu AI của CV 5512 năm 2020.

Tài liệu HT nhắc hạn chế lạm dụng AI, tùy GVHD đánh giá. Phiếu dự giờ cần phản ánh tiết thực, góp ý xây dựng theo hướng dẫn GVHD; không tạo lời nhận xét, chữ ký hoặc điểm giả.

## Khung KHBD 5512 để bàn giao

Bản Phụ lục IV đăng trên cổng UBND xã Ba Vì được đối chiếu ngày 01/11/2026: [Khung kế hoạch bài dạy](https://bavi.quangngai.gov.vn/upload/2007096/20250911/20201218%20Phu%20luc%204%20Khung%20Ke%20hoach%20bai%20day%20%28giao%20an%29.pdf). Tóm tắt: ghi môn, lớp, thời lượng; mục tiêu kiến thức, năng lực, phẩm chất; thiết bị và học liệu; tiến trình mở đầu, kiến thức mới, luyện tập, vận dụng. Mỗi hoạt động xác định mục tiêu, nội dung, sản phẩm và cách tổ chức; khâu tổ chức theo giao việc, thực hiện, báo cáo/thảo luận, kết luận. Đây là đối chiếu cấu trúc bản năm 2020, chưa xác nhận hiệu lực toàn bộ quy định năm 2026.

Năng lực số/AI trong bản thiết kế đề xuất cần có hành vi quan sát được, sản phẩm và tiêu chí kiểm chứng; không tự gán mã năng lực theo một khung pháp lý chưa có nguồn.''',
[source('TT',select('TT',1,50)),source('HT'),source('BIA'),source('FM'),source('QD')])
print('Built 7 knowledge files; roster:',len(roster),'teachers/tasks records:',len(teachers))
