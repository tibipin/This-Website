from app import app
from flask import jsonify

@app.route('/', methods=['GET'])
def home():
    return jsonify(location='home_page')