from flask import Flask
from .model import configure as config_db
from.model import login_manager
from flask_migrate import Migrate


#?app definition
app = Flask(__name__)
app.config.from_object('config')
#?db config
config_db(app)
#! migrations
Migrate(app,app.db)
#config loguin
login_manager(app)

from .controls import ways
ways(app)
