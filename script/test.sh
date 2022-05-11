#!/bin/bash
#ls -a
source venv/bin/activate
declare -a directories=("boxer-api" "stamina-api" "strength-api" "merge-api")
for dir in "${directories[@]}"
do
    cd $dir
    pip3 install -r requirements.txt
    python3 -m pytest --cov=application
    cd..
done