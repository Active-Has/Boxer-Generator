from application import app 
from flask import Flask, request, Response 
import random

@app.route('/get_stamina', methods=['GET'])
def get_stamina():
    return Response(str(random.randint(1, 100)), mimetype='text/plain')