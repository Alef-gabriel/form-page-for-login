from flask import render_template
from .form import MyForm
from .model import User,db

def ways(app):
    @app.route("/", methods = ['GET','POST'])
    def index():

        form = MyForm()
        # new_user = User(name=form['name'], password=form['password'],email=form['email'])
        # db.session.add(new_user)
        # db.session.commit()
        return render_template('loguin.html', form=form)