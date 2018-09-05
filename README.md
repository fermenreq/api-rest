# Fake OFION rest services

We will be creating a RESTful API using **Flask** that is used to store users details, which will have CRUD (Create, Read, Update, Delete) functions, allowing us to create new items, get details of existing items, update details of existing items and delete it.

Also it process an invoice file from an example URL.

## 1.Installation & Deployment

``` ./up.sh ``` && ```python apy.py```

## 2.Testing tool
For testing a good way is to install [Postman](https://www.getpostman.com/apps) tool.

## 3.Options to create an invoice:
3.1. Create an invoice  executing ```sh post.sh``` located in test folder
3.2. Create a defualt user by a PDF http requested. The defualt user_id value is zero. For that, execute the following request:
```http://localhost:8081/invoice/user/0```

## 4.GET methods:

From step 2: Get an invoice for default user: ID is zero

Request:
``` http://localhost:8081/invoice/user/0```

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
      "Address": "23 East Road France", 
      "Date": "Wed, 29 Aug 2018 07:52:42 GMT", 
      "InvoiceID": "123456789", 
      "Name": "Mr.Romeo Trump", 
      "State": "EEUU", 
      "Url_invoice": "http://external_services_ofion_invoice.pdf", 
      "Zone": "New York", 
      "id_user": 3
    }, 
    {
      "Address": "23 East Road France", 
      "Date": "Wed, 29 Aug 2018 07:52:43 GMT", 
      "InvoiceID": "123456789", 
      "Name": "Mr.Romeo Trump", 
      "State": "EEUU", 
      "Url_invoice": "http://external_services_ofion_invoice.pdf", 
      "Zone": "New York", 
      "id_user": 28
    }
  ]
}

```

## 5. Install and enable mod_wsgi

Install: ```sh /install/basic.sh```

## 5.1 Apache setup - WSGI
In this chapter we want to serve the page using Apache via WSGI which helps to get our code deployed on Apache.
Here is the Apache config file (**/etc/apache2/sites-available/ofion.conf**):

```
<VirtualHost *:80>

	ServerAdmin webmaster@localhost
	ServerName localhost

	ErrorLog ${APACHE_LOG_DIR}/error.log
	CustomLog ${APACHE_LOG_DIR}/access.log combined

	WSGIDaemonProcess services user=www-data group=www-data threads=5
	WSGIProcessGroup services
	
	WSGIScriptAlias / /var/www/FLASKAPPS/services/ofion.wsgi
	#Alias /static/ /var/www/FLASKAPPS/services/static

	<Directory /var/www/FLASKAPPS/services/static>
            Order allow,deny
            Allow from all
    </Directory>
</VirtualHost>

```

```$ sudo a2ensite ofion.conf```

The WSGI file (**/var/www/FlASKAPPS/ofion.wsgi**)
```
#!/usr/bin/python
import sys
sys.path.insert(0,"/var/www/FLASKAPPS/")
from services import app as application
```

