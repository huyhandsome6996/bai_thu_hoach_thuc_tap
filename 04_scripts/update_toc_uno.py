# -*- coding: utf-8 -*-
"""Cập nhật mục lục (TOC, danh mục bảng) trong .docx bằng LibreOffice UNO.

Cách chạy: khởi động soffice headless listener, rồi /usr/bin/python3 script.
"""
import os, sys, time, subprocess
import uno
from com.sun.star.beans import PropertyValue

SRC = sys.argv[1]
OUT = sys.argv[2]

def connect(retries=30):
    localContext = uno.getComponentContext()
    resolver = localContext.ServiceManager.createInstanceWithContext(
        "com.sun.star.bridge.UnoUrlResolver", localContext)
    for i in range(retries):
        try:
            ctx = resolver.resolve(
                "uno:socket,host=127.0.0.1,port=2002;urp;StarOffice.ComponentContext")
            return ctx
        except Exception:
            time.sleep(1)
    raise RuntimeError("Không kết nối được LibreOffice listener")

ctx = connect()
smgr = ctx.ServiceManager
desktop = smgr.createInstanceWithContext("com.sun.star.frame.Desktop", ctx)

def P(name, value):
    p = PropertyValue(); p.Name = name; p.Value = value
    return p

url = "file://" + os.path.abspath(SRC)
doc = desktop.loadComponentFromURL(url, "_blank", 0, (P("Hidden", True), P("ReadOnly", False)))

# refresh tất cả trường và chỉ mục
doc.refresh()
try:
    indexes = doc.getDocumentIndexes()
    print("Số chỉ mục:", indexes.getCount())
    for i in range(indexes.getCount()):
        idx = indexes.getByIndex(i)
        print(" - cập nhật:", idx.getServiceName() if hasattr(idx, 'getServiceName') else idx.Name)
        idx.update()
except Exception as e:
    print("Lỗi cập nhật chỉ mục:", e)

doc.refresh()
time.sleep(1)

out_url = "file://" + os.path.abspath(OUT)
doc.storeToURL(out_url, (P("FilterName", "MS Word 2007 XML"), P("Overwrite", True)))
doc.close(False)
print("Đã lưu bản đã cập nhật mục lục:", OUT)
