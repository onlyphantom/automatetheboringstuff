import PyPDF2
import re
import webbrowser

with open('sample.pdf', 'rb') as pdfFile:
    reader = PyPDF2.PdfFileReader(pdfFile)
    page1 = reader.getPage(1)
    text = page1.extractText()

    rex = re.compile("(?<=\%\%\(S\$\))(.*)", re.DOTALL)
    body = re.search(rex, text).group(0)
    holdings = re.findall(r'([a-zA-Z\s]+)(?=\n)', body)

    for company in holdings:
        webbrowser.open_new_tab(f'http://google.com/search?q={company}')
