# -*- coding: utf-8 -*-
"""QA nội dung bản Word: tìm chuỗi cấm, kiểm tra thể thức cơ bản."""
from docx import Document
from docx.shared import Cm

PATH = "/home/z/my-project/repo_btt/05_final_report/BAI_THU_HOACH_TTSP1_HO_QUANG_HUY.docx"
doc = Document(PATH)

texts = [p.text for p in doc.paragraphs]
for t in doc.tables:
    for row in t.rows:
        for cell in row.cells:
            texts.append(cell.text)
full = "\n".join(texts)

FORBIDDEN = {
    "12A2": "lớp phải là 12/2",
    "chủ nghiệm": "chính tả sai (chủ nhiệm)",
    "biễu": "chính tả sai (biểu)",
    "SaPa": "cần ghi Sa Pa",
    "Sa pa": "cần ghi Sa Pa",
    "TODO": "còn việc dở",
    "【": "còn placeholder",
    "XXX": "còn placeholder",
    "____": "còn placeholder",
    "null": "còn null",
    "undefined": "còn undefined",
    "NaN": "còn NaN",
    "sau bốn tuần": "không được viết như đã kết thúc cả đợt",
    "kết thúc đợt thực tập": "không được tuyên bố đã kết thúc đợt",
    "đã dự đủ": "chỉ được nói ở dạng kế hoạch",
    "đã hoàn thành cả đợt": "chưa hoàn thành cả đợt",
    "cả bốn tuần": "phạm vi bài là tuần 1",
    "Chưa đạt 100%": "n/a",
}

ok = True
for k, why in FORBIDDEN.items():
    if k in full:
        ok = False
        print(f"[FAIL] tìm thấy '{k}' ({why})")

# các cụm chỉ được trong ngữ cảnh kế hoạch
for k in ["17/11/2026", "18/11/2026", "21/11/2026", "02/11/2026"]:
    idx = 0
    while True:
        idx = full.find(k, idx)
        if idx == -1:
            break
        ctx = full[max(0, idx-90):idx+40].replace("\n", " ")
        print(f"[INFO] '{k}' …{ctx}…")
        idx += 1

# kiểm tra mốc đã xác nhận
for need in ["Hồ Quang Huy", "24S1020030", "Tin3A", "Sư phạm Tin học",
             "Sa Pa, Lào Cai", "12/2", "Mai Xuân Văn", "Nguyễn Thị Thu Phương",
             "26/10/2026", "9 giờ 45 phút", "10 giờ 30 phút",
             "0 tiết chuyên môn và 0 tiết chủ nhiệm",
             "Trường Đại học Sư phạm, Đại học Huế", "Trường THPT Thuận Hóa"]:
    if need not in full:
        ok = False
        print(f"[FAIL] thiếu dữ kiện bắt buộc: {need}")

sec = doc.sections[0]
checks = [
    ("Lề trái 3cm", abs(sec.left_margin.cm - 3.0) < 0.01),
    ("Lề phải 2cm", abs(sec.right_margin.cm - 2.0) < 0.01),
    ("Lề trên 2cm", abs(sec.top_margin.cm - 2.0) < 0.01),
    ("Lề dưới 2cm", abs(sec.bottom_margin.cm - 2.0) < 0.01),
    ("Khổ A4", abs(sec.page_width.cm - 21.0) < 0.05 and abs(sec.page_height.cm - 29.7) < 0.05),
]
for name, passed in checks:
    print(("[PASS] " if passed else "[FAIL] ") + name)
    ok = ok and passed

# kiểm font Normal
n = doc.styles["Normal"]
print("[INFO] Normal font:", n.font.name, n.font.size.pt if n.font.size else None)

# đếm bảng, đoạn
print("[INFO] Số bảng:", len(doc.tables))
print("[INFO] Số đoạn:", len(doc.paragraphs))
print("[INFO] Số ký tự toàn văn:", len(full))
print("KẾT QUẢ:", "PASS" if ok else "CÓ LỖI")
