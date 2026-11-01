"""Normalize the report's table layouts and source/heading labels after content review."""
from pathlib import Path
R=Path(__file__).resolve().parents[1]; S=R/'05_final_report/sections'
p=S/'05_BII27_28_3_co_cau.md'; s=p.read_text(encoding='utf-8')
start=s.index('TBL|Kết quả học tập – rèn luyện theo lớp'); end=s.index('\n\nNguồn:',start)
lines=s[start:end].splitlines(); rows=[[c.strip() for c in line.strip('|').split('|')] for line in lines[1:]]
learn=[['Lớp','Sĩ số','Tốt','Khá','Đạt']]+[[r[i] for i in (0,1,2,3,4)] for r in rows[1:]]
conduct=[['Lớp','Sĩ số','Tốt','Khá','Đạt','Chưa đạt']]+[[r[i] for i in (0,1,5,6,7,8)] for r in rows[1:]]
def tbl(title,rr): return 'TBL|'+title+'\n'+'\n'.join('| '+' | '.join(r)+' |' for r in rr)
s=s[:start]+tbl('Kết quả học tập theo lớp năm học 2025 – 2026',learn)+'\n\nNguồn: [S06, bảng T0093]; các ô số lượng trống được quy đổi 0 để đối chiếu tổng. Không có học sinh học tập mức Chưa đạt.\n\n'+tbl('Kết quả rèn luyện theo lớp năm học 2025 – 2026',conduct)+s[end:]
p.write_text(s,encoding='utf-8')
p=S/'04_BII1_2_nha_truong.md'; s=p.read_text(encoding='utf-8'); start=s.index('TBL|Quy mô trường qua'); end=s.index('\n\nNguồn:',start)
rows=[['Mốc thời gian','Lớp','Học sinh','Khối 10','Khối 11','Khối 12'],['Đầu năm 2025–2026','12','310','1 lớp/20 HS','6 lớp/152 HS','5 lớp/138 HS'],['Cuối năm 2025–2026','12','302','1 lớp/17 HS','6 lớp/149 HS','5 lớp/136 HS'],['Đầu năm 2026–2027','13','346','6 lớp/185 HS','1 lớp/18 HS','6 lớp/143 HS']]
s=s[:start]+tbl('Quy mô trường qua hai niên độ học 2025 – 2026 và 2026 – 2027',rows)+s[end:]; p.write_text(s,encoding='utf-8')
p=S/'07_BII6_ke_hoach.md'; s=p.read_text(encoding='utf-8'); s=s.replace('#### 6. Kế hoạch','### 6. Kế hoạch').replace('##### 6.','#### 6.'); p.write_text(s,encoding='utf-8')
p=R/'05_final_report/source_map.md'; s=p.read_text(encoding='utf-8').replace('[S01]–[S09]','[S01]–[S10]').replace('tới 9 tệp gốc','tới 9 tệp gốc và 1 nguồn đối chiếu khung KHBD')
url='https://bavi.quangngai.gov.vn/upload/2007096/20250911/20201218%20Phu%20luc%204%20Khung%20Ke%20hoach%20bai%20day%20%28giao%20an%29.pdf'
s += '\n## Nguồn bổ sung [S10]\n\nPhụ lục IV, Khung kế hoạch bài dạy kèm Công văn 5512/BGDĐT-GDTrH ngày 18/12/2020; [bản trên cổng UBND xã Ba Vì]('+url+'). Đã đối chiếu cấu trúc trong bước QA. Nguồn này chỉ dùng cho cấu trúc KHBD, không chứng minh yêu cầu AI có trong nguyên văn công văn năm 2020. [S03] mới là tài liệu hình thức yêu cầu bổ sung năng lực số/AI.\n'
p.write_text(s,encoding='utf-8')
print('Split narrow result table, normalized headings and source map.')
