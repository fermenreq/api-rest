# Simple Python API Rest

We will be creating a RESTful API using **Flask** that is used to store users details, which will have CRUD (Create, Read, Update, Delete) functions, allowing us to create new items, get details of existing items, update details of existing items and delete it.

The function readPDF.py process an external PDF file from a URL path

## 1. Installation & Deployment

``` ./up.sh ``` && ```python apy.py```

## Testing tool:

For testing a good way is to install [Postman](https://www.getpostman.com/apps) tool.


## **GET** method:

Request:
``` http://localhost:8081/user/invoice/0/```

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



