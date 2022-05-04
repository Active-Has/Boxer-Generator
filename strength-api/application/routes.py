from application import app 
from flask import Flask, request, Response 
import random

@app.route('/get_strength', methods=['GET'])
def get_strength():
    return Response(str(random.randint(1, 100)), mimetype='text/plain')