from app import app
from flask import jsonify

@app.route('/admin', methods=['GET', 'POST'])
def admin_login():
    return jsonify(location='admin login page')


@app.route('/admin/dashboard')
def admin_dashboard():
    return jsonify(location='admin dashboard')