from flask import flash,render_template,redirect,url_for,request,abort
from .model import User, db

def ways(app):
    @app.route("/",methods = ['GET', 'POST'])
    def loguin():
        if request.method == 'POST':
            email = request.form['email']
            pwd = request.form['password']
            user = User.query.filter_by(email=email).first()
            if user:
                if User.query.filter_by(password=pwd).first():
                    flash('Logged in successfully.')
                    return redirect(url_for('user'))
            else:
                flash('Logged in filed')
        return render_template('loguin.html'), 200

    @app.route("/create_user", methods = ['GET','POST'])
    def create_user():
        if request.method == 'POST':
            email = request.form['email']
            pwd = request.form['password']
            err = 0
            data = request.get_json()
            while err <= 5:
                try:
                    new_user = User(password=pwd.data,email=email.data)
                    db.session.add(new_user)
                    db.session.commit()
                    return redirect(url_for('user'))
                except:
                    return abort(400)
                    err += 1
        return render_template('creat_user.html')
        
    @app.route('/user')
    def user():
        return render_template('usuario.html')
        