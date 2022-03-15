from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class StickyForm(FlaskForm):
    content = TextAreaField('Sticky', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    post_it = SubmitField('Post It!')