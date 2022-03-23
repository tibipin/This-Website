from sqlalchemy import Column, String, DateTime
from sqlalchemy.sql import func
from app import db, ma, login_manager
from flask_login import UserMixin

class Sticky(db.Model):
    __tablename__='sticky_notes'
    sticky_id = Column(String, primary_key=True)
    content = Column(String)
    timestamp = Column(DateTime(timezone=True), default=func.now())
    title = Column(String)

class StickySchema(ma.Schema):
    class Meta:
        fields = ('sticky_id','content', 'timestamp', 'title')

class User(UserMixin, db.Model):
    __tablename__='users'
    username = Column(String, primary_key=True)
    password = Column(String)
    email = Column(String)

    def get_id(self):
        return self.username

@login_manager.user_loader
def load_user(username):
    if username:
        user_x = User.query.filter_by(username=username).first()
        if user_x: 
            return user_x
        else:
            return None
    else: 
        return None
