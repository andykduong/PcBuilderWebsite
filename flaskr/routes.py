from flask import redirect, url_for, render_template, flash
from flaskr import app, db, Bcrypt
from flaskr.forms import RegistrationForm, LoginForm
from flaskr.models import User, CPU, CPUCooler, Mobo, GPU, RAM, drive, PSU, case, fans



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
        hashed_pass = Bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_pass)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger') 
    return render_template('login.html', title='Login', form=form)
