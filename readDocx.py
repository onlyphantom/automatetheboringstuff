import docx

def getText(filename):
    doc = docx.Document(filename)
    fullText = [p.text for p in doc.paragraphs]
    return '\n'.join(fullText)
