## This file it uses to read a PDF from an URL
## 
##fernando.mendez@atos.net

import PyPDF2
import urllib2
import io

URL_INVOICE = "http://visibillity.com/collateral/electronic_documents/invoice.pdf"


def downloadFile(url):
	content = ""
	req = urllib2.Request(url)
	response = urllib2.urlopen(url)
	remote_file = urllib2.urlopen(req).read()
	memory_file  = io.BytesIO(remote_file)
	read_pdf = PyPDF2.PdfFileReader(memory_file)
	num_page = read_pdf.getNumPages()

	if num_page > 0:
		for i in range(0,num_page):
			x = read_pdf.getPage(i).extractText()+'\n'
			content += x
	else:
		aux = "PDF is empty"

	return content

	def between(value, a, b):
		pos_ = value.find(a)
		if pos



def extractTextLit(self):
	text_list=[]
	content = self["/Context"].getObject()



	

def main():
	print downloadFile(URL_INVOICE)


if __name__ == "__main__":
	main()