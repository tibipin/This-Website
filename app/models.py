from sqlalchemy import Column, Integer, String, DateTime
from app import db


class PagePost(db.Model):
    __tablename__='Posts'
    id = Column(Integer, autoincrement=True, primary_key=True)
    post = Column(String)
    title = Column(String)
    timestamp = DateTime()

