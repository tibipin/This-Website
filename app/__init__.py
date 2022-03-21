from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://jukvqtdiodjvfa:ea7563f1138820cd1a17d78177fe373bc59711e9771af9bf694a261b6cdf4a6a@ec2-52-22-226-8.compute-1.amazonaws.com:5432/d9efbdoe69kv1r"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
db = SQLAlchemy(app)
ma = Marshmallow(app)

from app import views