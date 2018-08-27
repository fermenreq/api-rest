## This file is part of OFION process BPM.
## 
# Fernando Mendez - fernando.mendez@atos.net
#
############################################
#-*- coding: UTF-8 -*-

from flask import Flask,jsonify
from flask_restful import Api, Resource, reqparse
from flask import abort
import readPDF
import json


app = Flask(__name__)

# invoices = [
#     {
#         "Name": "Mr. Christopher Jones", 
#         "Zone": "Globecity East", 
#         "Url_invoice": "http://visibillity.com/collateral/electronic_documents/invoice.pdf", 
#         "InvoiceID": 22, 
#         "State": "Globeland             1001", 
#         "Address": "254 East Road", 
#         "Date": "26/02/2001"
#     }

# ]

data = readPDF.processData()

@app.route('/user/<int:id_user>', methods=['GET'])

def get_invoice(id_user):
    return json.dump(data)


def post(invoiceId):
    parser = reqparse.RequestParser()

    parser.add_argument("Name")
    args = parser.parse_args()

    for invoice in invoices:
        if (invoiceId == invoice["InvoiceID"]):
            return "The id {} already exists".format(invoiceId), 400

    invoice = [
        {
            "InvoiceID": invoiceId, 
            "Name": args["Name"], 
            "Zone": "Globecity East", 
            "Url_invoice": "http://visibillity.com/collateral/electronic_documents/invoice.pdf", 
            "State": "Globeland             1001", 
            "Address": "254 East Road", 
            "Date": "26/02/2001"
        }
    ]
    invoices.append(invoice)
    return invoice, 201



if __name__ == '__main__':

    app.run(host='127.0.0.1', port="8081",debug=True)
