from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField, BooleanField

from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', 
                           validators=[DataRequired(), Length(min=2, max=16)])
    email = StringField('Email', 
                        validators=[DataRequired(), Email()], render_kw = {"placeholder":"johndoe@example.com"})
    password = PasswordField('Password', 
                             validators=[DataRequired(), Length(min=8, max=24)])
    confirm_pass = PasswordField('Confirm Password',
                                  validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', 
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', 
                             validators=[DataRequired(), Length(min=8, max=24)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')