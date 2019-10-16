from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, validators
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    """Login form to access writing and settings pages"""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


class RegistrationForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    password = PasswordField('New Password', [validators.DataRequired()])
    confirm = PasswordField('Repeat Password', 
        [validators.DataRequired(),validators.EqualTo('password', message='Passwords must match')])