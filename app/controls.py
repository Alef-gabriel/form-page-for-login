from flask import render_template

def ways(app):
    @app.route("/", methods = ['GET'])
    def index():
        return render_template('index.html')