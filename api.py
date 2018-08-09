from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

invoices = [
    {
        "invoiceId":"invoice_00",
        "debtor":"Paul Smith",
        "path_invoice":"/seres/path",
    },
    {
        "invoiceId":"invoice_01",
        "debtor":"Rebeca Singson",
        "path_invoice":"/seres/path",
    }
]

class Invoice(Resource):

    def get(self, invoiceId):
        for invoice in invoices:
            if (invoiceId == invoice["invoiceId"]):
                return invoice, 200
        return "Invoice not found" , 404

    def post(self, invoiceId):
        parser = reqparse.RequestParser()

        parser.add_argument("debtor")
        args = parser.parse_args()

        for invoice in invoices:
            if (invoiceId == invoice["invoiceId"]):
                return "The id {} already exists".format(invoiceId), 400

        invoice = [
            {
                "invoiceId":invoiceId,
                "debtor":args["debtor"],
                "path_invoice":"/seres/path",
            }
        ]
        invoices.append(invoice)
        return invoice, 201


api.add_resource(Invoice, "/invoices/<string:invoiceId>")

app.run(host='0.0.0.0', port=8081, debug=True)
