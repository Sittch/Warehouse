import docx

def getText(filename)
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraps:
        fullText.append(para.text)
    return '\n'.join(fullText)
##Replace PATH with filepath
print(getText('PATH.docx'))
