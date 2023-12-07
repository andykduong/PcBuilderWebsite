from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

app = Flask(__name__, static_url_path='/static')


app.config['SECRET_KEY'] = 'f4dccf5e141748b5efe91de31d91491c'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

from flaskr import routes
from .models import CPU_db, CPUCooler_db, Mobo_db, GPU_db, RAM_db, drive_db, PSU_db, case_db, fans_db


