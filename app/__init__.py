from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#?app definition
app = Flask(__name__)
app.config.from_object('config')
#?db config
db = SQLAlchemy(app)

Migrate(app,db)
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30),unique=True)
    email = db.Column(db.String(30),unique=True)
    password = db.Column(db.String(50))

#import routes
from .controls import ways
ways(app)
