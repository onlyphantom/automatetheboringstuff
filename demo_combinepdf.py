import PyPDF2, os

pdfFiles = [f for f in os.listdir('reports') if f.endswith('.pdf')]
pdfFiles.sort(key=str.lower)

pdfWriter = PyPDF2.PdfFileWriter()
for f in pdfFiles:
    pdfFileObj = open(os.path.join('reports', f), 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)     
with open('combined.pdf', 'wb') as output:
    pdfWriter.write(output)
