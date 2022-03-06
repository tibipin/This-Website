from app import app

@app.route('/admin')
def admin_view():
    return 'this is the admin view'