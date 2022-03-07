from sqlalchemy import Column, String, DateTime
from app import db
from datetime import datetime

class BlogPost(db.model):
    __tablename__='blog_posts'
    post = Column(String)
    title = Column(String)
    timestamp = DateTime(default=datetime.now())
