from flask import Flask
from .model import configure as config_db
from flask_migrate import Migrate

#?app definition
app = Flask(__name__)
app.config.from_object('config')

#?db config
config_db(app)

#!migrate config
migrate = Migrate(app, app.db)

#import routes
from .controls import ways
ways(app)
