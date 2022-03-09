from sqlalchemy import Column, String, DateTime
from app import db, ma
from secrets import token_urlsafe


class Sticky(db.Model):
    __tablename__='sticky_notes'
    sticky_id = Column(String, primary_key=True, default=token_urlsafe(16))
    content = Column(String)
    timestamp = Column(DateTime)
    username = Column(String)

class StickySchema(ma.Schema):
    class Meta:
        fields = ('sticky_id','content', 'timestamp', 'username')

class User(db.Model):
    __tablename__='users'
    username = Column(String, primary_key=True)
    password = Column(String)
    email = Column(String)