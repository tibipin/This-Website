from flask import Flask

app = Flask(__name__)


import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir,'database.db')}"
db = SQLAlchemy(app)

from app import views
from app import admin_views