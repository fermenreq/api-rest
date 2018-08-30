#!/bin/bash

# Create & Activate Virtualenv
virtualenv .venv --always-copy

pip install -r requirements.txt
source .venv/bin/activate

