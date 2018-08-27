## This file is part of OFION
## 
##fernando.mendez@atos.net

import PyPDF2
import urllib2
import io
from PyPDF2.pdf import PageObject, u_, ContentStream, b_, TextStringObject

URL_INVOICE = "http://visibillity.com/collateral/electronic_documents/invoice.pdf"


def extractTextList(self):
    text_list = []
    content = self["/Contents"].getObject()
    if not isinstance(content, ContentStream):
        content = ContentStream(content, self.pdf)

    for operands, operator in content.operations:
        if operator == b_("Tj"):
            _text = operands[0]
            if isinstance(_text, TextStringObject) and len(_text.strip()):
                text_list.append(_text.strip())
        elif operator == b_("T*"):
            pass
        elif operator == b_("'"):
            pass
            _text = operands[0]
            if isinstance(_text, TextStringObject) and len(operands[0]):
                text_list.append(operands[0])
        elif operator == b_('"'):
            _text = operands[2]
            if isinstance(_text, TextStringObject) and len(_text):
                text_list.append(_text)
        elif operator == b_("TJ"):
            for i in operands[0]:
                if isinstance(i, TextStringObject) and len(i):
                    text_list.append(i)
    return text_list


def between(text_elements, drop_while, take_while):    
    return list(itertools.takewhile(take_while, itertools.dropwhile(drop_while, text_elements)))[1:]

def downloadFile(url):    
    content = ""
    req = urllib2.Request(url)
    response = urllib2.urlopen(url)
    remote_file = urllib2.urlopen(req).read()
    memory_file  = io.BytesIO(remote_file)
    read_pdf = PyPDF2.PdfFileReader(memory_file)
    
    page0 = read_pdf.getPage(0)
    text_elements = page0.extractTextList()

    lines = between(text_elements, lambda x: x != 'RATING', lambda x: 'DAYS' not in x)
    print('\n'.join(lines))
    

def main():
    downloadFile(URL_INVOICE)


if __name__ == "__main__":
	main()
