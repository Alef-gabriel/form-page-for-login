from flask import render_template,redirect
from .form import MyForm
from app import db, Users

def ways(app):
    @app.route("/",methods = ['GET','POST'])
    def inicial():
        return render_template('home.html')

    @app.route("/logout", methods = ['GET','POST'])

    def index():
        form = MyForm()
        if form.validate_on_submit():
            try:
                new_user = Users(name=form.name.data, password=form.password.data,email=form.email.data)
                db.session.add(new_user)
                db.session.commit()
                return redirect('/success')
            except:
                return "erro", 404

        return render_template('loguin.html', form=form)

    @app.route('/success')
    def susses():
        return render_template('usuario.html')