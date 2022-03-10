from app import app
from flask import jsonify, render_template, request, redirect, url_for
from app.models import Sticky, StickySchema, User
from app.forms import LoginForm

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

@app.route('/_admin/dashboard', methods=['GET','POST'])
def my_admin_dashboard():
    return render_template('admin/dashboard.html', username=request.args.get('username'))