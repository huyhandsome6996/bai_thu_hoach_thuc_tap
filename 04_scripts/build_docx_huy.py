# -*- coding: utf-8 -*-
"""Dựng bài thu hoạch TTSP1 (Hồ Quang Huy) dạng .docx theo FORM gốc và thể thức quy định.

Thể thức: A4; lề trái 3cm, trên/dưới/phải 2cm; Times New Roman 13 đen;
Multiple 1.2; Before/After 0pt; Justify; thụt đầu dòng 1cm; số trang giữa footer.
"""
import os, re, sys
from docx import Document
from docx.shared import Pt, Cm, RGBColor, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.enum.section import WD_SECTION
from docx.oxml.ns import qn, nsmap
from docx.oxml import OxmlElement

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEC = os.path.join(BASE, "05_final_report", "sections")
MEDIA = os.path.join(BASE, "04_scripts", "extracted_sources", "media", "Bìa bài thu hoạch trường")
OUT = os.path.join(BASE, "05_final_report", "BAI_THU_HOACH_TTSP1_HO_QUANG_HUY.docx")

FONT = "Times New Roman"
BLACK = RGBColor(0, 0, 0)
FIRST_LINE = Cm(1.0)
USABLE = Cm(16.0)

SECTIONS_ORDER = [
    "01_loi_cam_on.md",
    "02_A_ban_than.md",
    "03_BI_hoat_dong.md",
    "04_BII1_2_nha_truong.md",
    "05_BII27_28_3_co_cau.md",
    "06_BII4_5.md",
    "07_BII6_ke_hoach.md",
    "08_BIII_ttsp.md",
    "09_BIV_tong_ket.md",
    "10_BV_nhan_xet.md",
]

# ---------------------------------------------------------------- helpers

def set_run_font(run, size=13, bold=False, italic=False):
    run.font.name = FONT
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = BLACK
    rPr = run._element.get_or_add_rPr()
    rFonts = rPr.find(qn("w:rFonts"))
    if rFonts is None:
        rFonts = OxmlElement("w:rFonts")
        rPr.append(rFonts)
    for attr in ("w:ascii", "w:hAnsi", "w:eastAsia", "w:cs"):
        rFonts.set(qn(attr), FONT)

def set_para_format(p, align=WD_ALIGN_PARAGRAPH.JUSTIFY, first_line=FIRST_LINE,
                    left=None, hanging=None, before=0, after=0, line=1.2,
                    keep_next=False):
    pf = p.paragraph_format
    pf.alignment = align
    pf.space_before = Pt(before)
    pf.space_after = Pt(after)
    # Multiple 1.2 -> line = 240 * 1.2 = 288, lineRule auto
    pPr = p._element.get_or_add_pPr()
    spacing = pPr.find(qn("w:spacing"))
    if spacing is None:
        spacing = OxmlElement("w:spacing")
        pPr.append(spacing)
    spacing.set(qn("w:line"), "288")
    spacing.set(qn("w:lineRule"), "auto")
    spacing.set(qn("w:before"), str(int(before * 20)))
    spacing.set(qn("w:after"), str(int(after * 20)))
    if first_line is not None:
        pf.first_line_indent = first_line
    else:
        pf.first_line_indent = Cm(0)
    if left is not None:
        pf.left_indent = left
    if hanging is not None:
        pf.first_line_indent = -hanging
    if keep_next:
        pPr = p._element.get_or_add_pPr()
        kn = OxmlElement("w:keepNext")
        pPr.append(kn)

def add_para(doc, text, size=13, bold=False, italic=False,
             align=WD_ALIGN_PARAGRAPH.JUSTIFY, first_line=FIRST_LINE,
             left=None, hanging=None, before=0, after=0, keep_next=False,
             style=None):
    p = doc.add_paragraph(style=style)
    r = p.add_run(text)
    set_run_font(r, size=size, bold=bold, italic=italic)
    set_para_format(p, align=align, first_line=first_line, left=left,
                    hanging=hanging, before=before, after=after, keep_next=keep_next)
    return p

def add_field(p, instr, placeholder=""):
    """Chèn complex field vào paragraph p."""
    r1 = p.add_run()
    fld = OxmlElement("w:fldChar"); fld.set(qn("w:fldCharType"), "begin")
    fld.set(qn("w:dirty"), "true")
    r1._element.append(fld)
    set_run_font(r1)
    r2 = p.add_run()
    it = OxmlElement("w:instrText"); it.set(qn("xml:space"), "preserve")
    it.text = instr
    r2._element.append(it)
    set_run_font(r2)
    r3 = p.add_run()
    sep = OxmlElement("w:fldChar"); sep.set(qn("w:fldCharType"), "separate")
    r3._element.append(sep)
    set_run_font(r3)
    if placeholder:
        r4 = p.add_run(placeholder)
        set_run_font(r4)
    r5 = p.add_run()
    end = OxmlElement("w:fldChar"); end.set(qn("w:fldCharType"), "end")
    r5._element.append(end)
    set_run_font(r5)
    return p

def add_page_number_footer(section):
    footer = section.footer
    p = footer.paragraphs[0] if footer.paragraphs else footer.add_paragraph()
    p.text = ""
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_para_format(p, align=WD_ALIGN_PARAGRAPH.CENTER, first_line=None)
    add_field(p, " PAGE ", "1")

def caption_seq_para(doc, title):
    """Chú thích bảng: 'Bảng {SEQ}. Tên' có field SEQ để tạo danh mục bảng."""
    p = doc.add_paragraph()
    set_para_format(p, align=WD_ALIGN_PARAGRAPH.CENTER, first_line=None,
                    keep_next=True)
    r1 = p.add_run("Bảng ")
    set_run_font(r1, size=12, bold=True)
    add_field(p, ' SEQ Bảng \\* ARABIC ', "1")
    # fix formatting for field runs
    for r in p.runs:
        set_run_font(r, size=12, bold=True)
    r_last = p.add_run(". " + title)
    set_run_font(r_last, size=12, bold=True)
    return p

def add_source_line(doc, text):
    return add_para(doc, text, size=12, italic=True,
                    align=WD_ALIGN_PARAGRAPH.JUSTIFY, first_line=None, after=6)

# ------------------------------------------------------------ table build

def set_cell_margins(table, cm=0.08):
    tblPr = table._tbl.tblPr
    mar = OxmlElement("w:tblCellMar")
    for side in ("top", "left", "bottom", "right"):
        el = OxmlElement(f"w:{side}")
        el.set(qn("w:w"), str(int(cm * 567)))
        el.set(qn("w:type"), "dxa")
        mar.append(el)
    tblPr.append(mar)

def set_repeat_header(row):
    trPr = row._tr.get_or_add_trPr()
    th = OxmlElement("w:tblHeader")
    th.set(qn("w:val"), "true")
    trPr.append(th)

def table_borders(table):
    tblPr = table._tbl.tblPr
    borders = OxmlElement("w:tblBorders")
    for side in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement(f"w:{side}")
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), "4")
        el.set(qn("w:space"), "0")
        el.set(qn("w:color"), "000000")
        borders.append(el)
    tblPr.append(borders)

def set_tbl_grid(tbl, widths):
    """Ghi đè lưới cột (dxa) để LibreOffice/Word tôn trọng chiều rộng cột."""
    tblEl = tbl._tbl
    grid = tblEl.find(qn("w:tblGrid"))
    if grid is not None:
        tblEl.remove(grid)
    grid = OxmlElement("w:tblGrid")
    for w in widths:
        col = OxmlElement("w:gridCol")
        col.set(qn("w:w"), str(int(w.twips if hasattr(w, 'twips') else int(w))))
        grid.append(col)
    # tblGrid phải đứng ngay sau tblPr
    tblPr = tblEl.tblPr
    tblPr.addnext(grid)
    # tổng chiều rộng bảng cố định
    tblW = tblPr.find(qn("w:tblW"))
    if tblW is None:
        tblW = OxmlElement("w:tblW")
        tblPr.append(tblW)
    total = sum(int(w) for w in widths)
    tblW.set(qn("w:w"), str(total))
    tblW.set(qn("w:type"), "dxa")


def build_table(doc, rows, title=None):
    n_cols = len(rows[0])
    fsize = 13 if n_cols <= 5 else 12
    tbl = doc.add_table(rows=len(rows), cols=n_cols)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    tbl.style = "Table Grid"
    table_borders(tbl)
    set_cell_margins(tbl)
    # layout fixed
    tblPr = tbl._tbl.tblPr
    layout = OxmlElement("w:tblLayout")
    layout.set(qn("w:type"), "fixed")
    tblPr.append(layout)
    # weighted widths
    weights = []
    for c in range(n_cols):
        w = max(len(r[c]) if c < len(r) else 0 for r in rows)
        weights.append(max(w, 4))
    total = sum(weights)
    weights = []
    for c in range(n_cols):
        w = max(len(r[c]) if c < len(r) else 0 for r in rows)
        weights.append(max(w, 4))
    total = sum(weights)
    cm_vals = [max(16.0 * w / total, 1.6) for w in weights]
    sc = 16.0 / sum(cm_vals)
    cm_vals = [x * sc for x in cm_vals]
    widths = [Cm(x) for x in cm_vals]
    # ghi lưới cột để khóa chiều rộng (twips)
    set_tbl_grid(tbl, [int(x * 567) for x in cm_vals])
    for i, row in enumerate(rows):
        for j, cell_text in enumerate(row):
            cell = tbl.cell(i, j)
            cell.width = widths[j]
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            p = cell.paragraphs[0]
            txt = cell_text.strip()
            r = p.add_run(txt)
            header = (i == 0)
            set_run_font(r, size=fsize, bold=header)
            is_short = len(txt) <= 14
            align = WD_ALIGN_PARAGRAPH.CENTER if (header or is_short) else WD_ALIGN_PARAGRAPH.LEFT
            set_para_format(p, align=align, first_line=None)
            tcPr = cell._tc.get_or_add_tcPr()
    for j, w in enumerate(widths):
        for i in range(len(rows)):
            tbl.cell(i, j).width = w
    set_repeat_header(tbl.rows[0])
    if title:
        caption_seq_para(doc, title)
    return tbl

# ------------------------------------------------------- markdown parser

def parse_md(md_text):
    """Trả về danh sách khối: (kind, payload)."""
    lines = md_text.split("\n")
    blocks = []
    i = 0
    while i < len(lines):
        line = lines[i].rstrip()
        if not line.strip():
            i += 1
            continue
        if line.startswith("####"):
            blocks.append(("h4", line.lstrip("#").strip()))
            i += 1
        elif line.startswith("###"):
            blocks.append(("h3", line.lstrip("#").strip()))
            i += 1
        elif line.startswith("##"):
            blocks.append(("h2", line.lstrip("#").strip()))
            i += 1
        elif line.startswith("#"):
            blocks.append(("h1", line.lstrip("#").strip()))
            i += 1
        elif line.startswith("TBL|"):
            title = line[4:].strip()
            rows = []
            i += 1
            while i < len(lines) and lines[i].strip().startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                rows.append(cells)
                i += 1
            blocks.append(("table", (title, rows)))
        elif line.startswith("- "):
            blocks.append(("li", line[2:].strip()))
            i += 1
        elif line.startswith("Nguồn:"):
            blocks.append(("src", line.strip()))
            i += 1
        elif line.startswith(">>"):
            blocks.append(("right", line.lstrip(">").strip()))
            i += 1
        elif line.startswith(">"):
            blocks.append(("center", line.lstrip(">").strip()))
            i += 1
        elif line.strip() == "SIGTABLE":
            blocks.append(("sig", None))
            i += 1
        else:
            blocks.append(("p", line.strip()))
            i += 1
    return blocks

HEADING_SIZES = {"h1": 14, "h2": 13, "h3": 13, "h4": 13}

def render_blocks(doc, blocks, heading_map=None):
    for kind, payload in blocks:
        if kind in ("h1", "h2", "h3", "h4"):
            level = int(kind[1])
            if heading_map is not None:
                payload = heading_map.get(payload, payload)
            p = doc.add_heading(level=level)
            r = p.add_run(payload)
            set_run_font(r, size=HEADING_SIZES[kind], bold=(kind != "h4"),
                         italic=(kind == "h4"))
            set_para_format(p, align=WD_ALIGN_PARAGRAPH.LEFT, first_line=None,
                            before=0, after=0, keep_next=True)
        elif kind == "p":
            add_para(doc, payload)
        elif kind == "li":
            add_para(doc, "– " + payload, left=Cm(1.0), hanging=Cm(0.4),
                     first_line=None)
        elif kind == "src":
            add_source_line(doc, payload)
        elif kind == "center":
            add_para(doc, payload, align=WD_ALIGN_PARAGRAPH.CENTER,
                     first_line=None)
        elif kind == "right":
            add_para(doc, payload, align=WD_ALIGN_PARAGRAPH.RIGHT,
                     first_line=None)
        elif kind == "table":
            title, rows = payload
            build_table(doc, rows, title=title)
        elif kind == "sig":
            add_signature_table(doc)

def add_signature_table(doc):
    # chừa khoảng trống để khu chữ ký nằm ở nửa dưới trang
    for _ in range(9):
        p = doc.add_paragraph()
        set_para_format(p, first_line=None)
    tbl = doc.add_table(rows=2, cols=2)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    w = [Cm(8.0), Cm(8.0)]
    heads = [("Ban Giám hiệu", "(Ký và ghi rõ họ tên)"),
             ("Sinh viên thực tập", "(Ký và ghi rõ họ tên)")]
    for j in range(2):
        for i, txt in enumerate(heads[j]):
            cell = tbl.cell(i, j)
            cell.width = w[j]
            p = cell.paragraphs[0]
            r = p.add_run(txt)
            set_run_font(r, size=13, bold=(i == 0))
            set_para_format(p, align=WD_ALIGN_PARAGRAPH.CENTER, first_line=None)
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
    set_tbl_grid(tbl, [int(x.cm * 567) for x in w])
    for j in range(2):
        cell = tbl.cell(1, j)
        for _ in range(5):
            p = cell.add_paragraph()
            set_para_format(p, align=WD_ALIGN_PARAGRAPH.CENTER, first_line=None)
    tblPr = tbl._tbl.tblPr
    borders = OxmlElement("w:tblBorders")
    for side in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement(f"w:{side}")
        el.set(qn("w:val"), "none")
        borders.append(el)
    tblPr.append(borders)
    # ngắt trang sau khối chữ ký
    pbr = doc.add_paragraph()
    set_para_format(pbr, first_line=None)
    run = pbr.add_run()
    br = OxmlElement("w:br"); br.set(qn("w:type"), "page")
    run._element.append(br)

# ------------------------------------------------------------ cover page

def floating_image(doc, path, rid_holder):
    """Ảnh nổi phủ toàn trang, phía sau chữ (khung viền bìa)."""
    rid, _ = doc.part.get_or_add_image(path)
    cx, cy = 7560000, 10692000  # A4 21cm x 29.7cm in EMU
    xml = (
        '<w:drawing xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
        'xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" '
        'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
        'xmlns:pic="http://schemas.openxmlformats.org/drawingml/2006/picture" '
        'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
        '<wp:anchor distT="0" distB="0" distL="0" distR="0" simplePos="0" '
        'relativeHeight="0" behindDoc="1" locked="0" layoutInCell="1" allowOverlap="1">'
        '<wp:simplePos x="0" y="0"/>'
        '<wp:positionH relativeFrom="page"><wp:posOffset>0</wp:posOffset></wp:positionH>'
        '<wp:positionV relativeFrom="page"><wp:posOffset>0</wp:posOffset></wp:positionV>'
        f'<wp:extent cx="{cx}" cy="{cy}"/>'
        '<wp:effectExtent l="0" t="0" r="0" b="0"/>'
        '<wp:wrapNone/>'
        '<wp:docPr id="901" name="Khung bia"/>'
        '<wp:cNvGraphicFramePr/>'
        '<a:graphic><a:graphicData uri="http://schemas.openxmlformats.org/drawingml/2006/picture">'
        '<pic:pic>'
        '<pic:nvPicPr><pic:cNvPr id="901" name="Khung bia"/><pic:cNvPicPr/></pic:nvPicPr>'
        f'<pic:blipFill><a:blip r:embed="{rid}"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>'
        f'<pic:spPr><a:xfrm><a:off x="0" y="0"/><a:ext cx="{cx}" cy="{cy}"/></a:xfrm>'
        '<a:prstGeom prst="rect"><a:avLst/></a:prstGeom></pic:spPr>'
        '</pic:pic>'
        '</a:graphicData></a:graphic>'
        '</wp:anchor>'
        '</w:drawing>'
    )
    from docx.oxml import parse_xml
    return parse_xml(xml)

def build_cover(doc):
    if doc.paragraphs:
        p0 = doc.paragraphs[0]
    else:
        p0 = doc.add_paragraph()
    frame = floating_image(doc, os.path.join(MEDIA, "image1.jpeg"), None)
    r0 = p0.add_run()
    r0._element.append(frame)
    set_para_format(p0, align=WD_ALIGN_PARAGRAPH.CENTER, first_line=None)

    def cover_line(text, size, bold=True, after=0, before=0, italic=False):
        add_para(doc, text, size=size, bold=bold, italic=italic,
                 align=WD_ALIGN_PARAGRAPH.CENTER, first_line=None,
                 before=before, after=after)

    cover_line("TRƯỜNG ĐẠI HỌC SƯ PHẠM, ĐẠI HỌC HUẾ", 14, after=2)
    cover_line("TRƯỜNG THPT THUẬN HÓA", 14, after=30)
    # logo
    plogo = doc.add_paragraph()
    set_para_format(plogo, align=WD_ALIGN_PARAGRAPH.CENTER, first_line=None)
    rlogo = plogo.add_run()
    rlogo.add_picture(os.path.join(MEDIA, "image2.png"), width=Cm(6.8))
    cover_line("", 13, after=20)
    cover_line("BÀI THU HOẠCH", 22, after=6)
    cover_line("TÌM HIỂU THỰC TẾ GIÁO DỤC THỰC TẬP SƯ PHẠM 1", 17, after=40)

    rows = [
        ("GVHD Chuyên môn", "Mai Xuân Văn"),
        ("GVHD Chủ nhiệm", "Nguyễn Thị Thu Phương"),
        ("Sinh viên thực tập", "Hồ Quang Huy"),
        ("Ngành thực tập", "Sư phạm Tin học"),
        ("Trường TTSP 1", "Trường THPT Thuận Hóa"),
        ("Thời gian thực tập", "26/10/2026 – 21/11/2026"),
    ]
    tbl = doc.add_table(rows=len(rows), cols=3)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    widths = [Cm(4.6), Cm(0.5), Cm(7.9)]
    set_tbl_grid(tbl, [int(w.cm * 567) for w in widths])
    for i, (k, v) in enumerate(rows):
        c0, c1, c2 = tbl.cell(i, 0), tbl.cell(i, 1), tbl.cell(i, 2)
        for c, w in ((c0, widths[0]), (c1, widths[1]), (c2, widths[2])):
            c.width = w
        p = c0.paragraphs[0]; r = p.add_run(k)
        set_run_font(r, size=14, bold=False)
        set_para_format(p, align=WD_ALIGN_PARAGRAPH.LEFT, first_line=None)
        p = c1.paragraphs[0]; r = p.add_run(":")
        set_run_font(r, size=14)
        set_para_format(p, align=WD_ALIGN_PARAGRAPH.CENTER, first_line=None)
        p = c2.paragraphs[0]; r = p.add_run(v)
        set_run_font(r, size=14, bold=False)
        set_para_format(p, align=WD_ALIGN_PARAGRAPH.LEFT, first_line=None)
    tblPr = tbl._tbl.tblPr
    borders = OxmlElement("w:tblBorders")
    for side in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement(f"w:{side}")
        el.set(qn("w:val"), "none")
        borders.append(el)
    tblPr.append(borders)

    cover_line("", 13, after=70)
    cover_line("Huế, tháng 11 năm 2026", 14, bold=False)
    # page break sau bìa
    pbr = doc.add_paragraph()
    set_para_format(pbr, first_line=None)
    run = pbr.add_run()
    br = OxmlElement("w:br"); br.set(qn("w:type"), "page")
    run._element.append(br)

# ------------------------------------------------------------ TOC pages

def build_toc(doc):
    add_para(doc, "MỤC LỤC", size=14, bold=True,
             align=WD_ALIGN_PARAGRAPH.CENTER, first_line=None, after=6)
    p = doc.add_paragraph()
    set_para_format(p, first_line=None)
    add_field(p, ' TOC \\o "1-3" \\h \\z \\u ',
              "Mục lục tự động – mở tài liệu trong Microsoft Word và cập nhật trường để hiển thị.")
    add_para(doc, "DANH MỤC BẢNG", size=14, bold=True,
             align=WD_ALIGN_PARAGRAPH.CENTER, first_line=None, before=12, after=6)
    p2 = doc.add_paragraph()
    set_para_format(p2, first_line=None)
    add_field(p2, ' TOC \\h \\z \\c "Bảng" ',
              "Danh mục bảng tự động – cập nhật cùng lúc với mục lục.")
    add_para(doc, "CHỮ VIẾT TẮT", size=14, bold=True,
             align=WD_ALIGN_PARAGRAPH.CENTER, first_line=None, before=12, after=6)
    for ab, full in [
        ("BGH", "Ban Giám hiệu"),
        ("BCH", "Ban Chấp hành"),
        ("CB-GV-NV", "Cán bộ, giáo viên, nhân viên"),
        ("CLB", "Câu lạc bộ"),
        ("CNTT", "Công nghệ thông tin"),
        ("CSVC", "Cơ sở vật chất"),
        ("GDPT", "Giáo dục phổ thông (Chương trình GDPT 2018)"),
        ("GVHD", "Giáo viên hướng dẫn"),
        ("GVCN", "Giáo viên chủ nhiệm"),
        ("HĐTN-HN", "Hoạt động trải nghiệm, hướng nghiệp"),
        ("HS", "Học sinh"),
        ("HT", "Học tập (trong bảng số liệu)"),
        ("IOE", "Olympic Tiếng Anh trên Internet (International Olympiad of English)"),
        ("KH", "Kế hoạch giáo dục nhà trường năm học 2026 – 2027"),
        ("KNS", "Kỹ năng sống"),
        ("KHBD", "Kế hoạch bài dạy"),
        ("PPDH", "Phương pháp dạy học"),
        ("RL", "Rèn luyện (trong bảng số liệu)"),
        ("SV", "Sinh viên"),
        ("Sở GD&ĐT", "Sở Giáo dục và Đào tạo"),
        ("TK", "Báo cáo tổng kết năm học 2025 – 2026"),
        ("TT", "Kế hoạch hướng dẫn Thực tập sư phạm I năm học 2026 – 2027"),
        ("TTCM", "Tổ trưởng chuyên môn"),
        ("NTBM", "Nhóm trưởng bộ môn"),
        ("TTSP1", "Thực tập sư phạm 1"),
    ]:
        p = doc.add_paragraph()
        set_para_format(p, align=WD_ALIGN_PARAGRAPH.LEFT, first_line=None,
                        left=Cm(0.6))
        r1 = p.add_run(ab + ": "); set_run_font(r1, size=13, bold=True)
        r2 = p.add_run(full); set_run_font(r2, size=13)
    # page break sau mục lục
    pbr = doc.add_paragraph()
    set_para_format(pbr, first_line=None)
    run = pbr.add_run()
    br = OxmlElement("w:br"); br.set(qn("w:type"), "page")
    run._element.append(br)

# ----------------------------------------------------------------- main

def main():
    doc = Document()
    # trang và lề
    sec = doc.sections[0]
    sec.page_width = Cm(21.0)
    sec.page_height = Cm(29.7)
    sec.left_margin = Cm(3.0)
    sec.top_margin = Cm(2.0)
    sec.bottom_margin = Cm(2.0)
    sec.right_margin = Cm(2.0)
    sec.header_distance = Cm(1.0)
    sec.footer_distance = Cm(1.0)
    sec.different_first_page_header_footer = True  # bìa không đánh số

    # style chuẩn
    normal = doc.styles["Normal"]
    normal.font.name = FONT
    normal.font.size = Pt(13)
    normal.font.color.rgb = BLACK
    rPr = normal.element.get_or_add_rPr()
    rFonts = OxmlElement("w:rFonts")
    for attr in ("w:ascii", "w:hAnsi", "w:eastAsia", "w:cs"):
        rFonts.set(qn(attr), FONT)
    rPr.append(rFonts)
    npf = normal.paragraph_format
    npf.space_before = Pt(0); npf.space_after = Pt(0)
    npf.line_spacing = 1.2

    # heading styles -> đen, TNR
    for lvl in range(1, 5):
        st = doc.styles[f"Heading {lvl}"]
        st.font.name = FONT
        st.font.size = Pt(13 if lvl > 1 else 14)
        st.font.bold = True
        st.font.italic = False
        st.font.color.rgb = BLACK
        srPr = st.element.get_or_add_rPr()
        sFonts = OxmlElement("w:rFonts")
        for attr in ("w:ascii", "w:hAnsi", "w:eastAsia", "w:cs"):
            sFonts.set(qn(attr), FONT)
        srPr.append(sFonts)
        spf = st.paragraph_format
        spf.space_before = Pt(0); spf.space_after = Pt(0)
        spf.line_spacing = 1.2

    # cập nhật trường khi mở trong Word
    settings = doc.settings.element
    upd = OxmlElement("w:updateFields")
    upd.set(qn("w:val"), "true")
    settings.append(upd)

    # footer: số trang chính giữa
    add_page_number_footer(sec)

    # 1) bìa
    build_cover(doc)
    # 2) lời cảm ơn + ngắt trang cuối phần
    with open(os.path.join(SEC, "01_loi_cam_on.md"), encoding="utf-8") as f:
        md = f.read()
    render_blocks(doc, parse_md(md))
    # ký tên lời cảm ơn căn phải
    paras = doc.paragraphs
    for idx, para in enumerate(paras):
        if para.text.strip() == "Hồ Quang Huy" and idx > 2:
            prev = paras[idx - 1].text.strip() if idx > 0 else ""
            if prev.startswith("Em xin trân trọng cảm ơn"):
                para.alignment = WD_ALIGN_PARAGRAPH.RIGHT
                para.paragraph_format.right_indent = Cm(2.0)
                break
    pbr = doc.add_paragraph()
    set_para_format(pbr, first_line=None)
    run = pbr.add_run()
    br = OxmlElement("w:br"); br.set(qn("w:type"), "page")
    run._element.append(br)
    # 3) mục lục + danh mục bảng + viết tắt
    build_toc(doc)
    # 4) nội dung từ A trở đi
    for fname in SECTIONS_ORDER[1:]:
        with open(os.path.join(SEC, fname), encoding="utf-8") as f:
            md = f.read()
        blocks = parse_md(md)
        render_blocks(doc, blocks)

    # ngắt trang trước "B. HOẠT ĐỘNG..." và trước "V. NHẬN XẾT..."
    for para in doc.paragraphs:
        text = para.text.strip()
        if text.startswith("B. HOẠT ĐỘNG ĐÃ THỰC HIỆN") or text.startswith("V. NHẬN XÉT CỦA BGH"):
            pPr = para._element.get_or_add_pPr()
            pb = OxmlElement("w:pageBreakBefore")
            pPr.append(pb)

    doc.save(OUT)
    print("Đã tạo:", OUT)

if __name__ == "__main__":
    main()
