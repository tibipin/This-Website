from app import app
from flask import jsonify, render_template, request, redirect, url_for
from app.models import Sticky, StickySchema, User
from app.forms import LoginForm, StickyForm
from app import db
from secrets import token_urlsafe
from markdown import markdown

@app.route('/', methods=['GET'])
def home():
    stickies_list = StickySchema(many=True).dump(Sticky.query.all())
    return render_template('public/index.html', stickiez=stickies_list, title=stickies_list[0]['username'])


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

@app.route('/_admin/dashboard/<username>', methods=['GET','POST'])
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