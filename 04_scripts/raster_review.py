"""Rasterize a Word-exported PDF with the selected runtime's Poppler for visual QA."""
from pathlib import Path
import sys,json,hashlib
from pdf2image import convert_from_path
from PIL import Image,ImageOps,ImageDraw
from pypdf import PdfReader
R=Path(__file__).resolve().parents[1]
runtime=Path(sys.executable).resolve().parent.parent
poppler=runtime/'native/poppler/Library/bin'
pdf=R/'05_final_report/BAI_THU_HOACH_TTSP1_HO_QUANG_HUY.pdf'
out=R/'04_scripts/qa_review/final'; out.mkdir(parents=True,exist_ok=True)
previous={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in out.glob('*.png') if not p.name.startswith('sheet-')}
pages=convert_from_path(str(pdf),dpi=110,poppler_path=str(poppler),fmt='png',output_folder=str(out),output_file='page',paths_only=True)
changed=[i+1 for i,p in enumerate(pages) if previous.get(Path(p).name)!=hashlib.sha256(Path(p).read_bytes()).hexdigest()]
(out/'pixel_change_review.json').write_text(json.dumps({'changed_pages_since_previous_render':changed,'all_other_pages':'identical PNG bytes to previous visually reviewed render'},indent=2),encoding='utf-8')
texts=[p.extract_text() or '' for p in PdfReader(pdf).pages]
(out/'page_text.json').write_text(json.dumps([{'page':i+1,'words':len(t.split()),'text':t} for i,t in enumerate(texts)],ensure_ascii=False,indent=2),encoding='utf-8')
for n in range(0,len(pages),4):
    im=Image.open(pages[n]).convert('RGB'); w,h=im.size
    sheet=Image.new('RGB',(2*w,2*(h+30)), '#cccccc'); draw=ImageDraw.Draw(sheet)
    for j,path in enumerate(pages[n:n+4]):
        p=Image.open(path).convert('RGB'); x=(j%2)*w;y=(j//2)*(h+30)
        sheet.paste(p,(x,y)); draw.text((x+10,y+h+5),f'PAGE {n+j+1}',fill='black')
    sheet.save(out/f'sheet-{n//4+1:02}.png')
print('Rendered',len(pages),'pages; created', (len(pages)+3)//4,'review sheets in',out)
print('Word counts by page:',[len(t.split()) for t in texts])
print('PNG pages changed since previous visual review:',changed)
