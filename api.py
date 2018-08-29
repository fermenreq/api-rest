#-*- coding: UTF-8 -*-
# OFION demo process BPM services.
#
# 
#
# Fernando Mendez - fernando.mendez@atos.net


from flask import Flask,jsonify
from flask_restful import Api, Resource, reqparse
from flask import abort
import utils
import json
from flask import make_response
from flask import request
from flask import url_for
import time
import datetime


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

# External functions from utils.py

data_invoice = utils.processData()

invoices = []
decoded_data_invoice = json.loads(data_invoice)

# This function get an invoice for an user id
@app.route('/invoice/user/<int:id_user>', methods=['GET'])
def get_user_invoice(id_user):
    invoices.append(decoded_data_invoice)
    for i in invoices:
        if str(i['invoice']['id_user']) == str(id_user):
            return jsonify({"invoice": i['invoice']})
        else:
            abort(404)

# This funcition get all invoices from invoices list
@app.route('/invoices', methods=['GET'])
def get_invoices():
    if len(invoices)==0:
        abort(404)
    else:
         return jsonify({"invoice": invoices})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error":"Not found invoice for the user selected"}),404)


#This function generates a new invoice throw user parameters. 
@app.route('/invoice/user', methods=['POST'])
def create_invoice():
    if not request.json or not 'InvoiceID' in request.json:
        abort(404)
    date = datetime.datetime.now()
    random_id = utils.generateRandomId()

    #Payload for a new invoice
    invoice = {
            "Url_invoice": request.json['Url_invoice'],
            "State": request.json['State'], 
            "InvoiceID": request.json['InvoiceID'], 
            "id_user": random_id, 
            "Name": request.json['Name'], 
            "Zone": request.json['Zone'], 
            "Address": request.json['Address'], 
            "Date": date
    }

    invoices.append(invoice)
    print "Tam", len(invoices)
    return jsonify({"invoice": invoice}),201

#Fake function to send data to another service
@app.route('/invoice/send', methods=['POST'])
def send_invoice():
    create_invoice()
    
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
