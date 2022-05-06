from application import app 
from flask import Flask, jsonify
import random

@app.route('/get_strength', methods=['GET'])
def get_strength():
    return jsonify(random.randint(1, 100))