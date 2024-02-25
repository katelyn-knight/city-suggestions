from flask import Flask
import os

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from src.config.config import Config
from dotenv import load_dotenv

# loading environment variables
load_dotenv()


def create_app():
    # declaring flask app
    this_app = Flask(__name__)

    # path for local db
    this_app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    this_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
    return this_app


app = create_app()
# initialize with dev configuration
config = Config().dev
app.env = config.ENV
db = SQLAlchemy(app)

# Flask Migrate instance to handle database migrations
migrate = Migrate(app, db)
from src.models.geoname_model import Geoname

# import routes
from src.routes import suggestions_api
app.register_blueprint(suggestions_api)


@app.route("/")
def index():
    return "<h1>Hello, World!</h1>"

