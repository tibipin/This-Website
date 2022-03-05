from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from . import orm

import os

app = Flask(__name__)

# ======================================================
# ==> set base directory based on location of app.py <==
# ======================================================
basedir = os.path.abspath(os.path.dirname(__file__))

# =================================================================================
# ==> configure sqlite as database engine and save the database file in basedir <==
# =================================================================================
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "planets.db")}'

# ================================
# ==> intializing the database <==
# ================================
db = SQLAlchemy(app)




@app.route('/')
def home():
    return jsonify(message='Pizza'), 200 # 200 here is the http response status

@app.route('/parameters/<string:name>/<int:age>')
def parameters(name: str, age: int):
    if age < 18: 
        return jsonify(message=f'Sorry, {name}. You are not old enough'), 401
    else:
        return jsonify(message=f'Welcome {name}, you are old enough to see this website')


if __name__ == '__main__':
    app.run(debug=True)
