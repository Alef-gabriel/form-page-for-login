from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager,UserMixin
from werkzeug import generate_password_hash, check_password_hash

db = SQLAlchemy()

def configure(app):
    db.init_app(app)
    app.db = db

def login_manager(app):
    login_manager = LoginManager()
    login_manager.init_app(app)

@login_manager.user_loader
def get_user(user_id):
    return User.query.filter_by(id=user_id)

class User(db.Model , UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50),unique=True)
    password = db.Column(db.String(30))

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def verify_password(self,pwd):
        return check_password_hash(self.password,pwd)

    def __repr__(self):
        return '<User %r>' % self.name

