from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

# TODO move into a config
DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///showws.db'
API_PREFIX = "/v1/"

app = Flask(__name__)
app.config.from_object(__name__)
db = SQLAlchemy(app)

import api.models
import api.views
