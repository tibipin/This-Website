from app import app

@app.route('/')
def home():
    return 'this is the public home view'

