from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_testing import TestCase

class MyTest(TestCase):

    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True

    def create_app(self):
        # pass in test configuration
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
        db = SQLAlchemy(app)

        migrate = Migrate(app, db)
        from src.models.geoname_model import Geoname

        # import routes
        from src.routes import suggestions
        app.register_blueprint(suggestions)
        return app

    def setUp(self):
        """
        Creates a new database for the unit test to use
        """
        self.app = Flask(__name__)
        db.init_app(self.app)
        with self.app.app_context():
            db.create_all()
            self.populate_db()

    def tearDown(self):
        """
         Ensures that the database is emptied for next unit test
         """
        self.app = Flask(__name__)
        db.init_app(self.app)
        with self.app.app_context():
            db.drop_all()

    def test_suggest(self):
        response = self.app.get('/suggestions?q=Montreal')
        self.assertEqual(response.status_code, 200)



