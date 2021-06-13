from flask import Blueprint
from flask import request
import json
import random
from flask_cors import cross_origin
import app.services.dbService as dbService

scores = Blueprint("scores", __name__)
session = {}

@scores.route("/addScore", methods = ['POST'])
@cross_origin(supports_credentials=True)
def addScore():
    data = request.get_json()
    name = data.get('name')
    score = data.get('score')
    dbService.updateScore(name, score)
    response = {
        "message": "success"
    }
    return response

@scores.route("/getLeaderBoard", methods = ['GET'])
@cross_origin(supports_credentials=True)
def getLeaderBoard():
    result = dbService.getTopScores()
    response = {
        "result": result
    }
    return response