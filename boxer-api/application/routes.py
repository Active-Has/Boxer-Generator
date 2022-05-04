from application import app 
from flask import Flask, request, Response 
import requests

@app.route('/', methods=['GET'])
def home():
    stamina_api = request.get('http://stamina_api:5000/get_stamina')
    strength_api = requests.get('http://strength_api:5000/get_strength')
    return Response(f"Stamina: {stamina_api.text} Strength: {strength_api.text}", mimetype="text/plain")