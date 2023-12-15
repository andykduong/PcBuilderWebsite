from flask import redirect, url_for, render_template, flash, request
from flaskr import app, db
from flaskr.forms import RegistrationForm, LoginForm
from flaskr.models import User, CPU, CPUCooler, Mobo, GPU, RAM, drive, PSU, case, fans
from flask_login import current_user, login_user, logout_user



@app.route('/')

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template('about.html', title="About the Developer")

@app.route('/register', methods=['GET', "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_pass(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user is None or not user.check_pass(form.password.data):
            flash('Invalid Email or Password', 'error')
            return redirect(request.url)

        login_user(user, remember=form.remember.data)
        flash('You have been logged in successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
