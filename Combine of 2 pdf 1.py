# to get all the pages from multipule documents in one documents pdf
import PyPDF2
pdf1 = open('Absolute File/ PDF Path.', 'rb')
pdf2 = open('Absolute File/ PDF Path.', 'rb')
reader1 = PyPDF2.PdfFileReader(pdf1)
reader2 = PyPDF2.PdfFileReader(pdf2)
writer = PyPDF2.PdfFileWriter()
for pageNum in range(reader1.numPages):
    page = reader1.getPage(pageNum)
    writer.addPage(page)

for pageNum in range(reader2.numPages):
    page = reader2.getPage(pageNum)
    writer.addPage(page)
output = open('Combine PDF.pdf', 'wb')
writer.write(output)
output.close()
pdf1.close()
pdf2.close()
