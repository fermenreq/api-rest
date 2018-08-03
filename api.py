from flask import flask
from flask_result impor Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

invoices = [
    {
        "id":"invoice_00",
        "debtor":"Paul Smith",
        "path_invoice":"/seres/path",
    }
]

class Invoice(Resource):
    def get(self, id):
        for i in invoices:
            if (id == invoices["id"]):
                return id, 200
        return "Invoice not found" , 404

    def post(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("debtor")
        args = parser.parse_args()
        for i in invoices:
            if id == invoices["id"]:
                return "The id {} already exists".format(id), 400
        invoice = [
            {
                "id":id,
                "debtor":args["debtor"],
                "path_invoice":"/seres/path",
            }
        ]
        invoices.append(invoice)
        return invoice, 201


api.add_resource(User, "/invoice/<string:name>")
app.run(debug=True)
