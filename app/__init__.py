from flask import Flask
from .model import configure as config_db
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    config_db(app)

    migrate = Migrate(app, app.db)

    return app