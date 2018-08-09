# Simple Python API Rest

We will be creating a RESTful API using **Flask** that is used to store users details, which will have CRUD (Create, Read, Update, Delete) functions, allowing us to create new items, get details of existing items, update details of existing items and delete it.


## 1. Installation & Deployment

``` ./up.sh ``` && ```python apy.py```

## Testing tool:

For testing a good way is to install [Postman](https://www.getpostman.com/apps) tool.


## Example using method **GET**:

Request:
``` http://**IP**:8081/invoices/invoice_00```

Response:
```content-type:application/json
content-length:99
server: Werkzeug/0.14.1 Python/2.7.12
date:Thu, 09 Aug 2018 11:33:53 GMT
{
    "debtor": "Paul Smith", 
    "invoiceId": "invoice_00", 
    "path_invoice": "/seres/path"
}
```



