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


data = readPDF.processData()
decoded = json.loads(data)

@app.route('/user/<int:id_user>/', methods=['GET'])

def get_invoice(id_user):
    if (decoded["Invoice"]["id_user"]) == (id_user):
        return jsonify({"invoice":data})
    else:
        abort(404)
    
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error":"Not found"}),404)


    
if __name__ == '__main__':

    app.run(host='127.0.0.1', port="8081",debug=True)
