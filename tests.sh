#!/usr/bin/env bash
sudo apt update
sudo apt install python3 python3-pip python3-venv -python3
python3 -m venv venv
source venv/bin/activate
pip3 install -r testrequirements.txt
python3 -m pytest archetype/tests/tests.py --cov
python3 -m pytest character/tests.py --cov
python3 -m pytest flask-app/tests/tests.py --cov
python3 -m pytest race/tests/tests.py --cov