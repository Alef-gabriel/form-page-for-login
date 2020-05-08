from flask import render_template,redirect,url_for
from .model import User, db
from flask_login import  login_user, logout_user

def ways(app):
    @app.route("/",methods = ['GET', 'POST'])
    def loguin():
        return render_template('loguin.html'), 200

    @app.route("/create_user", methods = ['GET','POST'])
    def create_user():
        """
        if .validate_on_submit():
            try:
                new_user = User(password=form.password.data,email=form.email.data)
                db.session.add(new_user)
                db.session.commit()
                return redirect(url_for('user'))
            except:
                return "erro", 404
        return render_template('creat_user.html', form=form)
        """
    @app.route('/user')
    def user():
        return render_template('usuario.html')

    @app.route('/logout')
    def logout():
        logout_user()
        return redirect(url_for())