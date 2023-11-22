from flask import Flask

app = Flask(__name__, static_url_path='/static')

from flaskr import routes

app.config['SECRET_KEY'] = 'f4dccf5e141748b5efe91de31d91491c'