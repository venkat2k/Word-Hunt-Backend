from flask import Blueprint
from flask import request
import json
import random
from flask_cors import cross_origin

gamePlay = Blueprint("gameplay", __name__)
session = {}

@gamePlay.route("/getGameDetails", methods = ['GET'])
@cross_origin(supports_credentials=True)
def getGameDetails():
    gameId = random.randint(1000000, 10000000)
    while gameId in session:
        gameId = random.randint(1000000, 10000000)
    # session[gameId] = hash authentication to be added
    gameWord = 'word'
    gameId = str(gameId)
    session[gameId] = gameWord # need to add word picking 
    # print(session)
    response = {
        "gameId": gameId
    }
    
    return response

@gamePlay.route("/validate", methods = ['GET'])
@cross_origin(supports_credentials=True)
def validate():
    correct = 0
    misplaced = 0
    valid = True
    gameId = request.args.get('gameId')
    guess = request.args.get('guess')
    word = session.get(gameId)
    match = False
    if len(guess) != 4 or len(set(guess)) != 4:
        response = {
            "valid": False,
            "guess": guess
        }
        return response
    guess = guess.lower()
    for x in guess:
        if x not in "qwertyuioplkjhgfdsazxcvbnm":
            response = {
                "valid": False,
                "guess": guess
            }
            return response  
    common = len(set(word).intersection(set(guess)))
    for x in range(4):
        if word[x] == guess[x]:
            correct += 1
    misplaced = common - correct
    if guess == word:
        match = True
    response = {
        "valid": True,
        "misplaced": misplaced,
        "correct": correct,
        "match": match,
        "guess": guess
    }
    return response