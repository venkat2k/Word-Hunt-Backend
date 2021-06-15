from flask import Blueprint
from flask import request
import json
import random
from flask_cors import cross_origin
import app.utils.wordUtil as wordUtil
import app.services.dbService as dbService

gamePlay = Blueprint("gameplay", __name__)

@gamePlay.route("/getGameDetails", methods = ['GET'])
def getGameDetails():
    try:
        gameId = random.randint(1000000, 10000000)
        gameWord = dbService.chooseWord()
        gameId = str(gameId)
        response = {
            "gameId": gameId,
            "gameWord": gameWord
        }
        return response
    except Exception as error:
        response = {
            "error": str(error)
        }
        return response

@gamePlay.route("/validate", methods = ['GET'])
def validate():
    try:
        gameId = request.args.get('gameId')
        guess = request.args.get('guess')
        response = wordUtil.validate(guess, word)
        return response
    except Exception as error:
        response = {
            "error": str(error)
        }
        return response