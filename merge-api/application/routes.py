from application import app 
from flask import Flask, request, Response, jsonify 
import random

level = {
    0: "Beginner",
    1: "Intermediate",
    2: "Advanced",
    3: "Expert",
    4: "Professional",
    5: "World Class"
}

@app.route ('/post_stats', methods=['POST'])
def get_stats():

    name = eval(request.get_json()['stamina_api'])
    stats = eval(request.get_json()['strength_api'])

    sum = 0
    for name in name:
        sum += name
    if sum < 10:
        return Response(f"{level[0]}", mimetype="text/plain")
    elif sum < 25:
        return Response(f"{level[1]}", mimetype="text/plain")
    elif sum < 40:
        return Response(f"{level[2]}", mimetype="text/plain")
    elif sum < 60:
        return Response(f"{level[3]}", mimetype="text/plain")
    elif sum < 75:
        return Response(f"{level[4]}", mimetype="text/plain")
    elif sum < 90:
        return Response(f"{level[5]}", mimetype="text/plain")
    else:
        return Response(f"{level[0]}", mimetype="text/plain")

