from application import app 
from flask import Flask, jsonify, request, Response 
import random

@app.route('/get_boxer', methods=['GET'])
def get_boxer():
    boxer_name = ["Mike Tyson", "Floyd Mayweather", "Muhammad Ali", "Manny Pacquiao", "Gennady Golovkin"]
    boxer_picked = random.choice(boxer_name)
    return Response(f"{boxer_picked}", mimetype="text/plain")

@app.route('/get_stamina', methods=['GET'])
def get_stamina():
    return jsonify(random.randint(1, 100))