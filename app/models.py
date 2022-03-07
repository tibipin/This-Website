from sqlalchemy import Column, Integer, String, DateTime
from app import db, ma


class PagePost(db.Model):
    __tablename__='Posts'
    id = Column(Integer, autoincrement=True, primary_key=True)
    post = Column(String)
    title = Column(String)
    timestamp = Column(DateTime)

class PagePostSchema(ma.Schema):
    class Meta:
        fields = ('id','post','title', 'timestamp')