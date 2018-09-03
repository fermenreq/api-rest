#!/bin/bash

# Create & Activate Virtualenv
virtualenv .venv --always-copy

pip install -r requirements.txt
/etc/init.d/apache2 restart

sudo a2enmod wsgi

source .venv/bin/activate

