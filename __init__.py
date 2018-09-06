#-*- coding: UTF-8 -*-
#
# Fake services for OFION process invoice factoring
# 
# Fernando Mendez - fernando.mendez@atos.net

from flask import Flask,jsonify
from flask_restful import Api, Resource, reqparse
from flask import abort
import utils
import json
from flask import make_response
from flask import request,redirect
from flask import url_for
import time
import datetime
from urllib2 import Request
import requests
from flask import send_file
import io
import ConfigParser

app = Flask(__name__)


CONFIG_FILE="/var/www/FLASKAPPS/services/config..ini"

# Load the configuration file
with open(CONFIG_FILE,'r+') as f:
	sample_config=f.read()
config = ConfigParser.RawConfigParser(allow_no_value=True)
config.readfp(io.BytesIO(sample_config))



# External functions from utils.py
data_invoice = utils.processData()
print data_invoice 
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

# Fake function to invoke another service
@app.route('/post', methods=['GET'])
def send_invoice():

    URL_EXTERNAL_SERVICE=config.get('API','url_external')
    content_type=config.get('API','content_type')

    headers = {
        'Content-Type': content_type,
    }

    for i in invoices:
        if i <= len(invoices)-1 :
            content = json.dumps(i['invoice'])
            r = requests.post(URL_EXTERNAL_SERVICE, data=content, headers=headers)

    return jsonify({"invoice": invoices}),201


@app.route('/show_invoice/<int:id_invoice>',methods=['GET'])
def show_static_invoice(id_invoice):
	path=config.get('APACHE','STATIC_PATH')
	file = str(id_invoice)+'.pdf'
	completed_path_with_file = str(path)+file

	static_file = open(completed_path_with_file,'rb')
	return send_file(static_file, attachment_filename=file, as_attachment=False)
	

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
    #app.run(host='0.0.0.0', port="8081",debug=True)
    app.run(port=80)
