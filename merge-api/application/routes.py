from urllib import response
from application import app 
from flask import Flask, request, Response, jsonify 
import random

level = {
    0: "Beginner",
    1: "Intermediate",
    2: "Advanced",
    3: "Expert",
    4: "Professional",
    5: "World Class",
    6: "Legendary"
}

@app.route ('/post_stats', methods=['POST'])
def get_stats():

    name = request.get_json()['name']
    stats = int(request.get_json()['strength_api'])
    fighter_name = ""
    fighter_level = ""
    sum = stats

    for n in name:
        fighter_name.join(n)
    if sum < 10:
       # fighter_level=f"{level[0]}"
        if name == "Mike Tyson" or name == "Floyd Mayweather" or name == "Muhammad Ali" or name == "Manny Pacquiao" or name == "Gennady Golovkin":
            fighter_level=f"{level[0]}"
    elif sum > 10 and sum < 25:
      #  fighter_level=f"{level[1]}"
        if name == "Mike Tyson" or name == "Floyd Mayweather" or name == "Muhammad Ali" or name == "Manny Pacquiao" or name == "Gennady Golovkin":
            fighter_level=f"{level[1]}"
    elif sum > 25 and sum< 40:
       # fighter_level=f"{level[2]}"
        if name == "Mike Tyson" or name == "Floyd Mayweather" or name == "Muhammad Ali" or name == "Manny Pacquiao" or name == "Gennady Golovkin":
            fighter_level=f"{level[2]}"
    elif sum  > 40 and sum < 60:
       # fighter_level=f"{level[3]}"
        if name == "Mike Tyson" or name == "Floyd Mayweather" or name == "Muhammad Ali" or name == "Manny Pacquiao" or name == "Gennady Golovkin":
            fighter_level=f"{level[3]}"
    elif sum > 60 and sum < 75:
      #  fighter_level=f"{level[4]}"
        if name == "Mike Tyson" or name == "Floyd Mayweather" or name == "Muhammad Ali" or name == "Manny Pacquiao" or name == "Gennady Golovkin":
            fighter_level=f"{level[4]}"
    elif sum > 75 and sum < 90: 
       # fighter_level=f"{level[5]}"
        if name == "Mike Tyson" or name == "Floyd Mayweather" or name == "Muhammad Ali" or name == "Manny Pacquiao" or name == "Gennady Golovkin":
            fighter_level=f"{level[5]}"
    elif sum > 90 and sum < 100:
        if name == "Mike Tyson" or name == "Floyd Mayweather" or name == "Muhammad Ali" or name == "Manny Pacquiao" or name == "Gennady Golovkin":
            fighter_level=f"{level[6]}"
    else:
        fighter_level=f"{level[0]}"
    return Response(f"{fighter_level}", mimetype="text/plain")