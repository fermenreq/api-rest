# Simple Python API Rest

We will be creating a RESTful API using **Flask** that is used to store users details, which will have CRUD (Create, Read, Update, Delete) functions, allowing us to create new items, get details of existing items, update details of existing items and delete it.

The function readPDF.py process an external PDF file from a URL path

## 1. Installation & Deployment

``` ./up.sh ``` && ```python apy.py```

## Testing tool
For testing a good way is to install [Postman](https://www.getpostman.com/apps) tool.

## Options to create an user invoice:
1. Create an invoice user executing ```sh post.sh``` located in test folder
2. Create a defualt user by a PDF http requested. The defualt user_id value is zero. For that, execute the following request:
```http://localhost:8081/invoice/user/0```

## **GET** methods:

From step 2: Get an invoice for default user: ID is zero

Request:
``` http://localhost:8081/invoice/user/0/```

Response:

```content-type:application/json
content-length:99
server: Werkzeug/0.14.1 Python/2.7.12
date:Thu, 09 Aug 2018 11:33:53 GMT
{
  "invoice": {
    "Address": "254 East Road", 
    "Date": "26/02/2001", 
    "InvoiceID": 859652, 
    "Name": "Mr. Christopher Jones", 
    "State": "Globeland             1001", 
    "Url_invoice": "http://visibillity.com/collateral/electronic_documents/invoice.pdf", 
    "Zone": "Globecity East", 
    "id_user": 0
  }
}
```

Get all invoices:

Request:
``` http://localhost:8081/invoices```

Response:
```
{
  "invoice": [
    {
      "invoice": {
        "Address": "23 East Road France", 
        "Date": "Wed, 29 Aug 2018 07:40:05 GMT", 
        "InvoiceID": "123456789", 
        "Name": "Mr.Romeo Trump", 
        "State": "EEUU", 
        "Url_invoice": "http://external_services_ofion_invoice.pdf", 
        "Zone": "New York", 
        "id_user": 93
      }
    }, 
    {
      "invoice": {
        "Address": "23 East Road France", 
        "Date": "Wed, 29 Aug 2018 07:40:08 GMT", 
        "InvoiceID": "123456789", 
        "Name": "Mr.Romeo Trump", 
        "State": "EEUU", 
        "Url_invoice": "http://external_services_ofion_invoice.pdf", 
        "Zone": "New York", 
        "id_user": 1
      }
    }, 
    {
      "invoice": {
        "Address": "23 East Road France", 
        "Date": "Wed, 29 Aug 2018 07:40:08 GMT", 
        "InvoiceID": "123456789", 
        "Name": "Mr.Romeo Trump", 
        "State": "EEUU", 
        "Url_invoice": "http://external_services_ofion_invoice.pdf", 
        "Zone": "New York", 
        "id_user": 29
      }
    }, 
    {
      "invoice": {
        "Address": "23 East Road France", 
        "Date": "Wed, 29 Aug 2018 07:40:09 GMT", 
        "InvoiceID": "123456789", 
        "Name": "Mr.Romeo Trump", 
        "State": "EEUU", 
        "Url_invoice": "http://external_services_ofion_invoice.pdf", 
        "Zone": "New York", 
        "id_user": 48
      }
    }, 
    {
      "invoice": {
        "Address": "23 East Road France", 
        "Date": "Wed, 29 Aug 2018 07:40:10 GMT", 
        "InvoiceID": "123456789", 
        "Name": "Mr.Romeo Trump", 
        "State": "EEUU", 
        "Url_invoice": "http://external_services_ofion_invoice.pdf", 
        "Zone": "New York", 
        "id_user": 1
      }
    }
  ]
}
```




