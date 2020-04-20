from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired,Email,Length

class MyForm(FlaskForm):
    name = StringField('name', validators=[InputRequired(), Length(min=8,max=30)])
    password = PasswordField('password',validators=[InputRequired(), Length(min=8,max=30)])
    email = StringField('email',validators=[InputRequired(), Email('invalid email'),Length(max=50)])
