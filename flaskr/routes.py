from flask import redirect, url_for, render_template

from flaskr import app

@app.route('/')

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template('about.html', title="About the Developer")