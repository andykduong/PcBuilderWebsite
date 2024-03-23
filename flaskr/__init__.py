from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_session import Session
import click
from flask.cli import with_appcontext

app = Flask(__name__, static_url_path='/static')
app.config.from_object(Config)

#Flask Session Configs
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"  # Choose your preferred backend

db = SQLAlchemy(app)
migrate = Migrate(app, db)
Bcrypt = Bcrypt(app)
login  = LoginManager(app)
login.login_view='login'

from flaskr import controlDB, routes, models
from flaskr.models import CPU, CPUCOOLER, MOBO, GPU, RAM, DRIVE, PSU, CASE, FANS

@app.cli.command('repop-db')
@with_appcontext

def repopulate_db_cmd():
    controlDB.reset_db(CPU)
    controlDB.reset_db(CPUCOOLER)
    controlDB.reset_db(MOBO)
    controlDB.reset_db(GPU)
    controlDB.reset_db(RAM)
    controlDB.reset_db(DRIVE)
    controlDB.reset_db(PSU)
    controlDB.reset_db(CASE)
    controlDB.reset_db(FANS)
    controlDB.repopulate_db()
    click.echo('db repopulated')


