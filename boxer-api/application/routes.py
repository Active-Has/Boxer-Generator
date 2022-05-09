from application import app 
from flask import Flask, render_template, request, Response
import requests, random, json

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/boxer_gen', methods=['GET', 'POST'])
def boxer():
    boxer_api = requests.get('http://stamina-api:5000/get_boxer').text
    stamina_api = requests.get('http://stamina-api:5000/get_stamina').json()
    strength_api = requests.get('http://strength-api:5000/get_strength').json()

    gen = {'stamina_api' : stamina_api, 'strength_api' : strength_api, 'name' : boxer_api}
    stats = requests.post('http://merge-api:5000/post_stats', json = gen).text

    return render_template('boxer_gen.html', boxer_api = boxer_api, stamina_api = stamina_api, strength_api = strength_api, stats = stats)
#    return Response(f"Boxer: {boxer_api.text} Stamina: {stamina_api.text} Strength: {strength_api.text}", mimetype="text/plain")
