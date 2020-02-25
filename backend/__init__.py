from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from backend.config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
# migrate = Migrate(app, db)

CORS(app, resources={r'/*': {'origins': '*'}})

from backend import routes