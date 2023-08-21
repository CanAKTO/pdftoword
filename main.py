from pdf2docx import Converter
pdf_file = "06DET413.pdf"
docx_file = "çıktı.docx"

cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()
