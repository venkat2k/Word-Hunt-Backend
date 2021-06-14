from flask import *
from app.api.gameplay import gamePlay
from app.api.scores import scores
from flask_cors import CORS
import os

app = Flask(__name__)
app.secret_key = os.environ["SECRET_KEY"]
CORS(app, resources={r"/api/*": {"origins": "https://word-hunt-app.herokuapp.com"}})

app.register_blueprint(gamePlay, url_prefix='/api/gamePlay')
app.register_blueprint(scores, url_prefix='/api/scores')
