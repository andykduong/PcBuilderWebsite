from flask import redirect, url_for, render_template, flash

from flaskr import app

from flaskr.forms import RegistrationForm, LoginForm


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
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('index'))
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
