from datetime import date
from sqlalchemy import desc
from app import app
from flask import jsonify, render_template, request, redirect, url_for
from app.models import Sticky, StickySchema, User
from app.forms import LoginForm, StickyForm
from app import db
from secrets import token_urlsafe
from markdown import markdown

@app.route('/about_me', methods=['GET'])
@app.route('/', methods=['GET'])
def home():
    current_date = (date(2022,9,22) - date.today()).days
    return render_template('public/home.html', date=current_date)

@app.route('/blog', methods=['GET'])
def blog():
    stickies_list = StickySchema(many=True).dump(Sticky.query.order_by(Sticky.timestamp.desc()).limit(10))
    return render_template('public/blog.html', stickiez=stickies_list, title=stickies_list[0]['username'])

@app.route('/music', methods=['GET'])
def music():
    return jsonify(message='this is the music page')

@app.route('/projects', methods=['GET'])
def projects():
    return jsonify(message='this is the projects page'), 200

@app.route('/cv', methods=['GET'])
def resume():
    return jsonify(message='this is the resume page'), 200

@app.route('/_admin', methods=['GET','POST'])
def my_admin_login():
    form = LoginForm()
    if request.method == 'GET':
        return render_template('admin/login.html', form=form)
    else:
        if form.validate_on_submit():
            if User.query.filter_by(username=form.username.data, password=form.password.data).first():
                return redirect(url_for('my_admin_dashboard', username=form.username.data))
            else:
                return render_template('admin/login.html')

@app.route('/_admin/<username>', methods=['GET','POST'])
def my_admin_dashboard(username):
    sticky_form = StickyForm()
    if request.method == 'GET':
        return render_template('admin/dashboard.html', form=sticky_form), 200
    if request.method == 'POST':
        if sticky_form.validate_on_submit():
            new_sticky = Sticky(sticky_id=token_urlsafe(16), content=markdown(sticky_form.content.data), username=username)
            db.session.add(new_sticky)
            db.session.commit()
            return redirect(url_for('home'))