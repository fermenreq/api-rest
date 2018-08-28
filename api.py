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
from flask import make_response
from flask import request
from flask import url_for

app = Flask(__name__)

# {
#     "Invoice": {
#         "Url_invoice": "http://visibillity.com/collateral/electronic_documents/invoice.pdf", 
#         "State": "Globeland             1001", 
#         "InvoiceID": 859652, 
#         "id_user": 0, 
#         "Name": "Mr. Christopher Jones", 
#         "Zone": "Globecity East", 
#         "Address": "254 East Road", 
#         "Date": "26/02/2001"
#     }
# }

invoices = []

data_invoice = readPDF.processData()
decoded_data_invoice = json.loads(data_invoice)
invoices.append(decoded_data_invoice)

@app.route('/user/invoice/<int:id_user>/', methods=['GET'])
def get_invoice(id_user):
    for i in invoices:
        if str(i['Invoice']['id_user']) == str(id_user):
            return jsonify({"invoice": i['Invoice']})
        else:
            abort(404)

        
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error":"Not found invoice for the user selected"}),404)

@app.route('/user/invoice', methods=['POST'])
def create_invoice():
    if not request.json or not 'InvoiceID' in request.json:
        abort(404)
    id = int(decoded_data_invoice["Invoice"]["id_user"])

    invoice = {
        "Url_invoice": "http://external_services_ofion_invoice.pdf",
        "State": "SO France", 
        "InvoiceID": request.json['InvoiceID'], 
        "id_user": id + 1, 
        "Name": "Mr.Duck Lucas", 
        "Zone": "DisneyLand Paris", 
        "Address": "23 East Road France", 
        "Date": "26/02/2018"
    }
    invoices.append(invoice)
    return jsonify({"invoice": invoice}),201

# This function generates a "public" version o an invoice to send to the client/services in order 
# to avoid clients to be forced to construct URLs from the invoice id

def make_public_invoice(invoice):
    new_invoice= {}

    for i in invoice:
        if i == 'id_user':
            new_invoice['uri'] = url_for('get_invoice_version2',invoice_id=invoice['id_user'],_external=True)
        else:
            new_invoice[i] = invoice[i]

    return new_invoice

def get_invoice_version2():
    return jsonify({'Invoice': [make_public_invoice(invoice) for invoice in invoices]})


#ToDo Securing RESTful api


if __name__ == '__main__':
    app.run(host='0.0.0.0', port="8081",debug=True)
