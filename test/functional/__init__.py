import os

from flask_sqlalchemy import SQLAlchemy
from src import create_app
from src.config.config import Config
from test import initialize_test_database
from flask_migrate import Migrate


def setup_app():
    os.environ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    os.environ['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'
    app = create_app()
    config = Config().dev
    app.env = config.ENV
    return app


def setup_db(app):
    db = SQLAlchemy(app)
    # Flask Migrate instance to handle database migrations
    migrate = Migrate(app, db)
    from src.models.geoname_model import Geoname
    initialize_test_database()
    return db

