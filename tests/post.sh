#!/bin/bash

curl -i -H "Content-Type: application/json" -X POST -d '
{
	"Address": "23 East Road France",  
    "InvoiceID": "123456789", 
    "Name": "Mr.Romeo Trump", 
    "State": "EEUU", 
    "Url_invoice": "http://external_services_ofion_invoice.pdf", 
    "Zone": "New York"
}' http://0.0.0.0:8081/invoice/user