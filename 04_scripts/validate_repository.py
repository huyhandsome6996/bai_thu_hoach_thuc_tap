"""Meaningful data-integrity checks for the QA handoff, not report-pagination tests."""
from pathlib import Path
import json,hashlib,re,zipfile
R=Path(__file__).resolve().parents[1]; X=R/'04_scripts/extracted_sources'
checks=[]
def check(label,condition):
    checks.append({'check':label,'passed':bool(condition)})
    if not condition: raise AssertionError(label)
manifest=json.loads((R/'00_meta/raw_manifest.json').read_text(encoding='utf-8-sig'))
check('Manifest records all 9 raw Office files',len(manifest)==9)
for f in manifest:
    p=R/'01_raw_data'/f['name']
    check('Original bytes and SHA-256: '+f['name'],p.stat().st_size==f['bytes'] and hashlib.sha256(p.read_bytes()).hexdigest().upper()==f['sha256'])
    check('JSON + Markdown extraction: '+f['name'],all((X/(p.stem+e)).is_file() for e in ('.md','.json')))
roster=json.loads((R/'00_meta/student_roster.json').read_text(encoding='utf-8'))
check('46 students, unique names+birth dates, complete teacher assignments',len(roster)==46 and len({(r['ho_ten'],r['ngay_sinh_nguon']) for r in roster})==46 and all(r['gvhd_chuyen_mon'] and r['gvhd_chu_nhiem'] for r in roster))
check('Both student STT sets cover 1..46',all(sorted(r[k] for r in roster)==list(range(1,47)) for k in ('stt_chuyen_mon','stt_chu_nhiem')))
tk=json.loads((X/'Báo cáo tổng kết năm học 2025 -2026.chốt.json').read_text(encoding='utf-8'))
rows=next(b['rows'] for b in tk if b['id']=='T0093')
classes=[r for r in rows if len(r)==13 and r[0].isdigit() and r[3]=='SL']
check('12 class records and 302 students',len(classes)==12 and sum(int(r[2]) for r in classes)==302)
check('Each class learning and conduct categories sum to enrolment',all(sum(int(v or 0) for v in r[4:8])==int(r[2]) and sum(int(v or 0) for v in r[8:12])==int(r[2]) for r in classes))
totals=[sum(int(r[i] or 0) for r in classes) for i in range(4,12)]
check('Class totals reconcile to 104/161/37/0 and 263/31/5/3',totals==[104,161,37,0,263,31,5,3])
check('10 outstanding and 92 excellent student award entries',len(next(b['rows'] for b in tk if b['id']=='T0096'))-1==10 and len(next(b['rows'] for b in tk if b['id']=='T0098'))-1==92)
check('New school enrolment and class breakdown reconcile',185+18+143==346 and 6+1+6==13)
check('Exactly seven knowledge documents',len(list((R/'02_extracted_knowledge').glob('*.md')))==7)
pagination=(R/'03_report_blueprint/pagination_strategy.md').read_text(encoding='utf-8')
check('Pagination covers physical pages 1..35 exactly once',list(map(int,re.findall(r'^\| (\d+) \|',pagination,re.M)))==list(range(1,36)))
outline=(R/'03_report_blueprint/master_outline_detailed.md').read_text(encoding='utf-8')
check('Detailed outline reaches H4 and preserves required FORM topics',len(re.findall(r'^#### ',outline,re.M))>=40 and all(s in outline for s in ('TÓM LƯỢC VỀ BẢN THÂN','Kết quả tìm hiểu','CÔNG TÁC TTSP 1','TỔNG KẾT','NHẬN XÉT CỦA BGH')))
profile=json.loads((R/'00_meta/student_profile.json').read_text(encoding='utf-8'))
check('Confirmed personal identity and exact assigned class',profile['ho_ten']=='Hồ Quang Huy' and profile['mssv']=='24S1020030' and profile['lop_thuc_tap_chu_nhiem']=='12/2' and profile['ngay_sinh']=='2006-02-25')
check('Word output and no completed lesson observations in week one',profile['dinh_dang_dau_ra']=='docx' and profile['observed_lesson_counts']['chuyen_mon']==0 and profile['observed_lesson_counts']['chu_nhiem']==0)
check('Master prompt exists and has handoff instructions',(R/'03_report_blueprint/prompt_for_coding_agent.md').stat().st_size>10000)
# Audit numeric cached totals independently without silently changing the source workbook.
sheet=json.loads((X/'Phân công giảng dạy HK1 năm học 2026- 2027.json').read_text(encoding='utf-8'))[0]
cells={k:v for row in sheet['rows'] for k,v in row.items()}
def num(c):
    v=cells.get(c,'').split(' [công thức:')[0]
    return float(v) if re.fullmatch(r'-?\d+(\.\d+)?',v) else 0
formula_audit=[]
for c,v in cells.items():
    m=re.search(r'công thức: SUM\(([FG])(\d+):([FG])(\d+)\)',v)
    if m:
        col,a,col2,b=m.groups(); value=sum(num(f'{col}{i}') for i in range(int(a),int(b)+1))
        formula_audit.append({'cell':c,'cache':num(c),'sum_recomputed':value,'matches':value==num(c)})
check('All explicit single-range SUM caches reconcile',all(x['matches'] for x in formula_audit))
# Copy embedded media to a separate evidence cache. Never interpret a photo as a dated student observation.
media=[]
for p in (R/'01_raw_data').glob('*.docx'):
    with zipfile.ZipFile(p) as z:
        for name in z.namelist():
            if name.startswith('word/media/') and not name.endswith('/'):
                target=X/'media'/p.stem/Path(name).name; target.parent.mkdir(parents=True,exist_ok=True); target.write_bytes(z.read(name))
                media.append({'source':p.name,'member':name,'extracted':target.relative_to(R).as_posix()})
(R/'00_meta/media_inventory.json').write_text(json.dumps(media,ensure_ascii=False,indent=2),encoding='utf-8')
result={'scope':'QA repository only, not a final report or Word layout validation','checks':checks,'formula_audit':formula_audit,'media_count':len(media),'source_formula_scope_notes':['F27/G27 exclude row28 (3 periods)','F79/G79 exclude row83 (5 periods)']}
(R/'00_meta/validation_results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(f'PASS: {len(checks)} integrity checks; {len(formula_audit)} SUM caches checked; {len(media)} embedded media extracted.')
