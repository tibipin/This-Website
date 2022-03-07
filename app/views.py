from app import app
from flask import jsonify
from app.models import PagePost, PagePostSchema

@app.route('/', methods=['GET'])
def home():
    page_posts_schema = PagePostSchema(many=True)
    posts_list = PagePost.query.all()
    result = page_posts_schema.dump(posts_list)
    return jsonify(result)