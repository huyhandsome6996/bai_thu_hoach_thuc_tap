"""Read OOXML with stdlib; legacy DOC is converted by convert_legacy_docs.ps1.
Usage: python 04_scripts/parse_all_docs.py
Original files are never modified. Block IDs are stable within each extraction.
"""
from pathlib import Path
import zipfile, xml.etree.ElementTree as ET, json, hashlib
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'04_scripts/extracted_sources'
W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
S = '{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'
def text_of(el):
    return ''.join((e.text or '') if e.tag == W+'t' else '\n' if e.tag in (W+'br', W+'p') else '\t' if e.tag == W+'tab' else '' for e in el.iter()).strip()
def mdcell(s): return s.replace('|','\\|').replace('\n','<br>').replace('\t',' ')
def docx(path):
    with zipfile.ZipFile(path) as z:
        root=ET.fromstring(z.read('word/document.xml'))
    blocks=[]
    for el in root.find(W+'body'):
        if el.tag==W+'p':
            t=text_of(el)
            if t: blocks.append({'id':f'P{len(blocks)+1:04}', 'text':t})
        elif el.tag==W+'tbl':
            rows=[[text_of(c) for c in r.findall(W+'tc')] for r in el.findall(W+'tr')]
            blocks.append({'id':f'T{len(blocks)+1:04}', 'rows':rows})
    return blocks
def render(blocks):
    out=[]
    for b in blocks:
        out.append('### '+b['id'])
        if 'text' in b: out.append(b['text'])
        else:
            n=max(map(len,b['rows']),default=0)
            if n:
                lines=['| '+' | '.join('C'+str(i+1) for i in range(n))+' |',
                       '| '+' | '.join('---' for _ in range(n))+' |']
                lines.extend('| '+' | '.join(mdcell(x) for x in r+['']*(n-len(r)))+' |' for r in b['rows'])
                out.append('\n'.join(lines))
    return '\n\n'.join(out)
def xlsx(path):
    with zipfile.ZipFile(path) as z:
        shared=[]
        if 'xl/sharedStrings.xml' in z.namelist():
            shared=[''.join(t.text or '' for t in x.iter(S+'t')) for x in ET.fromstring(z.read('xl/sharedStrings.xml'))]
        wb=ET.fromstring(z.read('xl/workbook.xml'))
        rels={e.attrib['Id']:e.attrib['Target'] for e in ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))}
        sheets=[]
        for sh in wb.find(S+'sheets'):
            target=rels[sh.attrib['{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id']]
            target=target.lstrip('/') if target.startswith('/') else 'xl/'+target
            tree=ET.fromstring(z.read(target)); rows=[]
            for r in tree.iter(S+'row'):
                cells={}
                for c in r:
                    v=c.find(S+'v'); val=v.text if v is not None else ''
                    if c.get('t')=='s': val=shared[int(val)] if val else ''
                    if c.get('t')=='inlineStr': val=''.join(t.text or '' for t in c.iter(S+'t'))
                    f=c.find(S+'f')
                    if f is not None: val=f'{val} [công thức: {f.text}]'
                    if val: cells[c.get('r')]=val
                if cells: rows.append(cells)
            sheets.append({'name':sh.get('name'),'rows':rows,'merges':[m.get('ref') for m in tree.iter(S+'mergeCell')]})
        return sheets
def main():
    OUT.mkdir(exist_ok=True)
    for p in sorted((ROOT/'01_raw_data').iterdir()):
        source=p
        if p.suffix=='.doc': source=OUT/(p.stem+'.docx')
        if not source.exists():
            print('MISSING CONVERSION:',p.name); continue
        if p.suffix in ('.doc','.docx'):
            blocks=docx(source)
            (OUT/(p.stem+'.json')).write_text(json.dumps(blocks,ensure_ascii=False,indent=2),encoding='utf-8')
            (OUT/(p.stem+'.md')).write_text('# '+p.name+'\n\n'+render(blocks),encoding='utf-8')
            print(p.name,len(blocks),'blocks')
        elif p.suffix=='.xlsx':
            sheets=xlsx(p)
            (OUT/(p.stem+'.json')).write_text(json.dumps(sheets,ensure_ascii=False,indent=2),encoding='utf-8')
            lines=['# '+p.name,'','Ô trống do gộp giữ nguyên; xem danh sách merged ranges trong JSON. Công thức giữ cả giá trị cache và biểu thức.']
            for sh in sheets:
                lines+=['\n## Sheet '+sh['name'],'','| Dòng | Ô và nội dung |','| --- | --- |']
                for r in sh['rows']: lines.append('| '+''.join(c for c in next(iter(r)) if c.isdigit())+' | '+'; '.join(k+': '+mdcell(v) for k,v in r.items())+' |')
            (OUT/(p.stem+'.md')).write_text('\n'.join(lines),encoding='utf-8')
            print(p.name,[(s['name'],len(s['rows'])) for s in sheets])
if __name__=='__main__': main()
