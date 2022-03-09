from app import app
from flask import jsonify, render_template
from app.models import Sticky, StickySchema
import os

@app.route('/', methods=['GET'])
def home():
    stickies_list = StickySchema(many=True).dump(Sticky.query.all())
    return render_template('public/index.html', stickiez=stickies_list, title=stickies_list[0]['username'])


@app.route('/admin')
def my_admin_login():
    return render_template('admin/login.html')

@app.route('/sign-up')
def sign_up():
    pass

@app.route('/login')
def login():
    pass