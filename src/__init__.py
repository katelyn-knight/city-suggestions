from flask import Flask
import os

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from src.config.config import Config
from dotenv import load_dotenv

# loading environment variables
load_dotenv()

# declaring flask app
app = Flask(__name__)

# initialize with dev configuration
config = Config().dev
app.env = config.ENV

# path for local db
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')

db = SQLAlchemy(app)

# Flask Migrate instance to handle database migrations
migrate = Migrate(app, db)

from .models.geoname_model import Geoname


@app.route("/")
def index():
    return "<h1>Hello, World!</h1>"
