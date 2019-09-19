#!/bin/bash

pip install -r requirements.txt
sleep 5

cd /opt/bicyparking/bicypark/tools/
python update_db.py
cd -
python web/run.py

