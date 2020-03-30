from flask import Flask
from flask_cors import CORS
from cookbookServer.config import Config

app = Flask(__name__)
app.config.from_object(Config)

CORS(app, resources={r'/*': {'origins': '*'}})

from cookbookServer import routes