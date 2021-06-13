from flask import Blueprint
from flask import request, jsonify
import json
import random
from flask_cors import cross_origin
import app.utils.wordUtil as wordUtil
import app.services.dbService as dbService

gamePlay = Blueprint("gameplay", __name__)
session = {}

@gamePlay.route("/getGameDetails", methods = ['GET'])
@cross_origin(supports_credentials=True)
def getGameDetails():
    gameId = random.randint(1000000, 10000000)
    while gameId in session:
        gameId = random.randint(1000000, 10000000)
    gameWord = dbService.chooseWord()
    gameId = str(gameId)
    session[gameId] = gameWord
    response = jsonify(
        gameId= gameId
    )
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@gamePlay.route("/validate", methods = ['GET'])
@cross_origin(supports_credentials=True)
def validate():
    gameId = request.args.get('gameId')
    guess = request.args.get('guess')
    word = session.get(gameId)
    response = wordUtil.validate(guess, word)
    response = jsonify(response)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response