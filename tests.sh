#!/bin/bash
declare -a directories=("archetype" "race" "character" "flask-app")
for dir in "${directories[@]}"
do
  cd ${dir}
  sudo apt-get update
  sudo apt-get install python3 python3-pip python3-venv
  python3 -m venv venv
  SOURCE venv/bin/activate
  pip3 install -r testrequirements.txt
  python3 -m pytest --cov=application --cov-report=term-missing
  SOURCE deactivate
  cd ..
done