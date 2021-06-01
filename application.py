from flask import *
from api.gameplay import gamePlay
from flask_cors import CORS

app = Flask(__name__)
# app.config['SERVER_NAME'] = 'http://127.0.0.1:5000/'
app.secret_key = "secretkey123"
CORS(app)

app.register_blueprint(gamePlay, url_prefix='/api')

# login
# signup
# username picking in frontend
# all these with authentication