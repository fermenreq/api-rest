## This file is part of OFION process BPM.
## 
# Fernando Mendez - fernando.mendez@atos.net
#
############################################
#-*- coding: UTF-8 -*-


import PyPDF2
import urllib2
import io
from PyPDF2.pdf import PageObject, u_, ContentStream, b_, TextStringObject
import itertools
import json
from flask import jsonify
import random
import os


URL_INVOICE = "http://visibillity.com/collateral/electronic_documents/invoice.pdf"
attributes = ["Name", "Address", "State" ,"Country","InvoiceID","Date","Url"]
password = ""
#Attributes previusly know it from invoice
FROM = "Globeland            1001"
TO = "1 of 2"

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


PageObject.extractTextList = extractTextList
	
def between(text_elements, drop_while, take_while):   
    return list(itertools.takewhile(take_while, itertools.dropwhile(drop_while, text_elements)))[1:]
    
def downloadFile(): 
    content = ""
    req = urllib2.Request(URL_INVOICE)
    remote_file = urllib2.urlopen(req).read()
    memory_file  = io.BytesIO(remote_file)
    read_pdf = PyPDF2.PdfFileReader(memory_file)
    read_pdf.decrypt(password)

    page0 = read_pdf.getPage(0)
    text_elements = page0.extractTextList()
        
    data = between(text_elements, lambda x: x != FROM, lambda x: TO not in x)

    # [u'Mr. Christopher Jones', u'254 East Road', u'Globecity East', u'Globeland 1001', u'127-96', u'98750-96', 
    # u'Speed Transport', u'Road', u'95643', u'26/02/2001', u'859652']

    return data

def saveData(name_file):
    req = urllib2.Request(URL_INVOICE)
    remote_file = urllib2.urlopen(req)

    with open(os.path.join('/var/www/FLASKAPPS/static/invoices/', name_file), 'w') as file:
        file.write(remote_file.read())
        file.close()


def processData():
    data = downloadFile()
    invoice = data[9]

    date = data[10]

    for i in data:
        del data[4:8]
    data.append(invoice)
    data.append(date)
    data.insert(len(data)-1, URL_INVOICE)

    name_file_saved=str(data[6])
    saveData(name_file_saved)
    

    id_user = 0

    data = {
        "invoice":{
            "Name": data[0],
            "Address":data[1],
            "Zone":data[2],
            "State":data[3],
            "Date":data[4],
            "Url_invoice": data[5],
            "InvoiceID":long(data[6]),
            "id_user":id_user
        }
    }
    return json.dumps(data,encoding="ascii",ensure_ascii=True,indent=4)


def generateRandomId():
    for x in range(100):
        return random.randint(1,100)

    
    