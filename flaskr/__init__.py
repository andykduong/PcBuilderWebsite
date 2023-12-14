from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

app = Flask(__name__, static_url_path='/static')
app.config.from_object(Config);


db = SQLAlchemy(app)
migrate = Migrate(app, db)
Bcrypt = Bcrypt(app)

from flaskr import routes, models



