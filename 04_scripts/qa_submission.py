"""Audit the actual DOCX and Word-exported PDF; visual review is a separate gate."""
from pathlib import Path
import json,re,sys,hashlib
from docx import Document
from docx.oxml.ns import qn
from pypdf import PdfReader
R=Path(__file__).resolve().parents[1]; O=R/'05_final_report'
doc=Document(O/'BAI_THU_HOACH_TTSP1_HO_QUANG_HUY.docx'); checks=[]
style_by_id={s.style_id:s for s in doc.styles}
def check(name,ok,detail=None): checks.append({'check':name,'passed':bool(ok),'detail':detail})
full='\n'.join(t.text for t in doc.element.body.iter(qn('w:t')) if t.text)
check('Confirmed personal data',all(s in full for s in ('Hồ Quang Huy','24S1020030','25/02/2006','Tin3A','Sư phạm Tin học','Sa Pa, Lào Cai','12/2','Mai Xuân Văn','Nguyễn Thị Thu Phương')))
check('Actual meeting times and zero observations',all(s in full for s in ('9 giờ 45 phút','10 giờ 30 phút','0 tiết chuyên môn và 0 tiết chủ nhiệm')))
for s in ('12A2','chủ nghiệm','biễu','SaPa','TODO','[CHỜ','undefined','NaN','người dùng','quay video','hai môn mà sinh viên Sư phạm Tin học','đã hoàn thành cả đợt','sau bốn tuần','đã dự đủ'):
    check('No erroneous/internal phrase: '+s,s not in full)
check('Different 12/2 cohorts distinguished','không phải cùng tập thể' in full and 'không dùng sĩ số' in full)
check('10-minute schedule vs15-minute activity','tức 10 phút' in full and 'không đồng nhất' in full)
check('Correct class maximum and computed khối totals',all(s in full for s in ('70,37%','29/149','73/136')))
check('Formatting source correctly S03','[S07, P0015]' not in full and '[S07, P0002' not in full and '[S03, P0015]' in full)
check('KHBD source S10 mapped','[S10]' in full and '[S10]' in (O/'source_map.md').read_text(encoding='utf-8'))
heads=[p.text for p in doc.paragraphs if p.style.name.startswith('Heading')]
seq=['A. TÓM LƯỢC','B. HOẠT ĐỘNG','I. HOẠT ĐỘNG','II. KẾT QUẢ','1. Tình hình giáo dục','2. Đặc điểm']+[f'2.{i}.' for i in range(1,9)]+['3. Cơ cấu']+[f'3.{i}.' for i in range(1,5)]+['4. Hoạt động giáo dục','5. Hoạt động Đoàn','5.1.','5.2.','6. Kế hoạch']+[f'6.{i}.' for i in range(1,6)]+['III. CÔNG TÁC','1. Vai trò','2. Công tác hướng dẫn','3. Một số yêu cầu','IV. TỔNG KẾT','V. NHẬN XÉT']
cursor=-1; missing=[]
for prefix in seq:
    found=[i for i,h in enumerate(heads) if i>cursor and h.startswith(prefix)]
    if found: cursor=found[0]
    else: missing.append(prefix)
check('Mandatory FORM headings in order',not missing,missing)
check('No extra main C/D/E/F sections',not any(re.match(r'^[C-F]\. ',h) for h in heads))
for i,s in enumerate(doc.sections,1):
    check(f'Section{i} A4 and margins3/2/2/2',abs(s.page_width.cm-21)<.03 and abs(s.page_height.cm-29.7)<.03 and abs(s.left_margin.cm-3)<.03 and all(abs(x.cm-2)<.03 for x in (s.right_margin,s.top_margin,s.bottom_margin)))

def props(p,r):
    chain=[]
    if r.find(qn('w:rPr')) is not None: chain.append(r.find(qn('w:rPr')))
    sid=p.find('w:pPr/w:pStyle',p.nsmap); st=style_by_id[sid.get(qn('w:val'))] if sid is not None else doc.styles['Normal']; seen=set()
    while st is not None and st.style_id not in seen:
        seen.add(st.style_id)
        if st.element.find(qn('w:rPr')) is not None: chain.append(st.element.find(qn('w:rPr')))
        st=st.base_style
    return chain
def prop(chain,tag,attr='val'):
    for pr in chain:
        el=pr.find(qn('w:'+tag))
        if el is not None and el.get(qn('w:'+attr)) is not None: return el.get(qn('w:'+attr))
    return None
font_errors=[];spacing_errors=[];body=False
for p in doc.element.body.iter(qn('w:p')):
    text=''.join(x.text or '' for x in p.iter(qn('w:t')))
    if text.startswith('LỜI CẢM ƠN'): body=True
    if not body or not text.strip(): continue
    for r in p.iter(qn('w:r')):
        if not ''.join(x.text or '' for x in r.iter(qn('w:t'))).strip(): continue
        chain=props(p,r); size=prop(chain,'sz'); font=prop(chain,'rFonts','ascii'); color=prop(chain,'color')
        if size!='26' or font!='Times New Roman' or color not in (None,'000000','auto'): font_errors.append([text[:70],size,font,color])
    pr=p.find(qn('w:pPr')); sp=pr.find(qn('w:spacing')) if pr is not None else None
    if sp is not None and any(sp.get(qn('w:'+k),v)!=v for k,v in [('line','288'),('lineRule','auto'),('before','0'),('after','0')]): spacing_errors.append([text[:70],dict(sp.attrib)])
check('Visible body/table/TOC text TNR13 black',not font_errors,font_errors[:12])
check('Direct body spacing Multiple1.2 before/after0',not spacing_errors,spacing_errors[:12])
learn=[];conduct=[];grids=[];repeat=[];splits=[]
for t in doc.tables:
    rows=[[c.text for c in r.cells] for r in t.rows]
    if rows[0]==['Lớp','Sĩ số','Tốt','Khá','Đạt']: learn=rows[1:]
    if rows[0]==['Lớp','Sĩ số','Tốt','Khá','Đạt','Chưa đạt']: conduct=rows[1:]
    if t.cell(0,0).text in ('GVHD Chuyên môn','Ban Giám hiệu'): continue
    grids.append(sum(int(c.get(qn('w:w'))) for c in t._tbl.tblGrid)<=9080)
    repeat.append(t.rows[0]._tr.find('w:trPr/w:tblHeader',t.rows[0]._tr.nsmap) is not None)
    splits.extend(r._tr.find('w:trPr/w:cantSplit',r._tr.nsmap) is not None for r in t.rows)
check('Actual learning table12rows sum302/104/161/37',len(learn)==12 and [sum(int(r[i]) for r in learn) for i in range(1,5)]==[302,104,161,37])
check('Actual conduct table12rows sum302/263/31/5/3',len(conduct)==12 and [sum(int(r[i]) for r in conduct) for i in range(1,6)]==[302,263,31,5,3])
check('Tables within16cm repeating headers no split records',all(grids) and all(repeat) and all(splits))
footer=doc.sections[0].footer.paragraphs[0]
check('Centered PAGE footer separate cover',footer.alignment==1 and 'PAGE' in ''.join(x.text or '' for x in footer._p.iter(qn('w:instrText'))) and doc.sections[0].different_first_page_header_footer)
pdf=PdfReader(O/'BAI_THU_HOACH_TTSP1_HO_QUANG_HUY.pdf'); texts=[p.extract_text() or '' for p in pdf.pages]
check('Word-rendered PDF30–35 pages',30<=len(pdf.pages)<=35,len(pdf.pages))
check('All PDF pages A4',all(abs(float(p.mediabox.width)-595.276)<1 and abs(float(p.mediabox.height)-841.89)<1 for p in pdf.pages))
check('No unresolved fields/Markdown in PDF',all(s not in '\n'.join(texts) for s in ('Error!','Lỗi!','TBL|','Mục lục tự động – mở tài liệu','Danh mục bảng tự động – cập nhật')))
check('No near-empty body pages',all(len(t.split())>=100 for t in texts[4:-1]),[len(t.split()) for t in texts])
check('Final page reserved for BGH/signatures',all(s in texts[-1] for s in ('V. NHẬN XÉT','Ban Giám hiệu','Sinh viên thực tập')))
result={'reviewed_commit':'36ea69e1217ea207f5bedca3b0eac9ecf076dfe1','word_pdf_pages':len(pdf.pages),'artifact_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (O/'BAI_THU_HOACH_TTSP1_HO_QUANG_HUY.docx',O/'BAI_THU_HOACH_TTSP1_HO_QUANG_HUY.pdf')},'checks':checks,'passed':all(x['passed'] for x in checks),'visual_review':'Required separately; this script does not establish visual quality or authenticate signatures.'}
(O/'qa_checks.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
for c in checks:
    if not c['passed']: print('FAIL:',c['check'],c['detail'])
print(('PASS' if result['passed'] else 'FAIL'),f'{sum(x["passed"] for x in checks)}/{len(checks)} document checks; {len(pdf.pages)} Word-rendered pages.')
sys.exit(0 if result['passed'] else 1)
