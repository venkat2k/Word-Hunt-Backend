from flask import Blueprint
from flask import request
import json
import random
from flask_cors import cross_origin
import app.services.dbService as dbService

scores = Blueprint("scores", __name__)

@scores.route("/addScore", methods = ['POST'])
def addScore():
    try:
        data = request.get_json()
        name = data.get('name')
        score = data.get('score')
        dbService.updateScore(name, score)
        response = {
            "message": "success"
        }
        return response
    except Exception as error:
        response = {
            "error": str(error)
        }
        return response

@scores.route("/getLeaderBoard", methods = ['GET'])
def getLeaderBoard():
    try:
        result = dbService.getTopScores()
        response = {
            "result": result
        }
        return response
    except Exception as error:
        response = {
            "error": str(error)
        }
        return response