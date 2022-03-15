from sqlalchemy import Column, String, DateTime
from sqlalchemy.sql import func
from app import db, ma


class Sticky(db.Model):
    __tablename__='sticky_notes'
    sticky_id = Column(String, primary_key=True)
    content = Column(String)
    timestamp = Column(DateTime(timezone=True), default=func.now())
    title = Column(String)

class StickySchema(ma.Schema):
    class Meta:
        fields = ('sticky_id','content', 'timestamp', 'title')

class User(db.Model):
    __tablename__='users'
    username = Column(String, primary_key=True)
    password = Column(String)
    email = Column(String)