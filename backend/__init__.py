from flask import Flask
from flask_cors import CORS
from backend.config import Config

app = Flask(__name__)
app.config.from_object(Config)

CORS(app, resources={r'/*': {'origins': '*'}})

from backend import routes