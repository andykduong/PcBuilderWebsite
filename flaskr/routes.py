from flask import redirect, url_for, render_template

from flaskr import app

from flaskr.forms import RegistrationForm, LoginForm


@app.route('/')

@app.route('/index')
def index():

    return render_template("index.html")

@app.route('/about')
def about():
    return render_template('about.html', title="About the Developer")

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)
