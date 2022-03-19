from datetime import datetime
import json
from re import U
import re
from dateutil import relativedelta
from app import app
from flask import jsonify, render_template, request, redirect, url_for
from app.models import Sticky, StickySchema, User
from app.forms import LoginForm, StickyForm
from app import db
from secrets import token_urlsafe
from markdown import markdown

# =================================
# ===> ABOUT ME section <===
# =================================

@app.route('/', methods=['GET'])
def home():
    datedif = relativedelta.relativedelta(datetime.now(),datetime(2021,9, 22, 16,41,00))
    date_format = f'{datedif.years} years, {datedif.months} months, {datedif.days} days, {datedif.hours} hours and {datedif.minutes} minutes'
    return render_template('public/home.html', date=date_format)

# =======================================
# ===> RECIPES section <===
# =======================================

@app.route('/recipes', methods=['GET','POST'])
def recipes():
    if request.method == 'GET':
        stickies_list = StickySchema(many=True).dump(Sticky.query.order_by(Sticky.timestamp.desc()).limit(10))
        if stickies_list:
            return render_template('public/recipes.html', stickiez=stickies_list, title=stickies_list[0]['title'])
        else: 
            return jsonify(messsage='no posts yet')
    elif request.method == 'POST':
        if 'read_it' in request.form.keys():
            return redirect(url_for('read_recipe', recipe_id = request.form['recipe_id']))
        elif 'delete_it' in request.form.keys():
            to_delete = Sticky.query.filter_by(sticky_id=request.form['recipe_id']).first()
            db.session.delete(to_delete)
            db.session.commit()
            return redirect(url_for('recipes'))

# ==========================
# ===> Projects section <===
# ==========================

@app.route('/projects', methods=['GET'])
def projects():
    return render_template('public/projects.html')

# ====================
# ===> CV section <===
# ====================

@app.route('/cv', methods=['GET'])
def resume():
    return redirect(url_for('static', filename='Tiberiu_Pintilie_CV.pdf'))

# =======================
# ===> MUSIC section <===
# =======================

@app.route('/music', methods=['GET'])
def music():
    return render_template('public/music.html')

# =======================
# ===> ADMIN section <===
# =======================

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

# =================================
# ===> CREATE NEW POST section <===
# =================================

@app.route('/_admin/<username>', methods=['GET','POST'])
def my_admin_dashboard(username):
    sticky_form = StickyForm()
    if request.method == 'GET':
        return render_template('admin/dashboard.html', form=sticky_form), 200
    if request.method == 'POST':
        if sticky_form.validate_on_submit():
            new_sticky = Sticky(sticky_id=token_urlsafe(16), content=markdown(sticky_form.content.data), title=sticky_form.title.data)
            db.session.add(new_sticky)
            db.session.commit()
            return redirect(url_for('recipes'))


# =================================
# ===> VIEW BLOG POST section <===
# =================================

@app.route('/recipes/<recipe_id>', methods=['GET', 'POST'])
def read_recipe(recipe_id):
    if request.method == 'GET':
        recipe =  StickySchema(many=False).dump(Sticky.query.filter_by(sticky_id=recipe_id).first())
        content = recipe['content']
        title = recipe['title']
        posted_on = recipe['timestamp']
        return render_template('public/blogpost.html', title=title, content=markdown(content), posted_on=posted_on)
    elif request.method == 'POST':
            if request.form['back_to_recipes']:
                return redirect(url_for('recipes'))
