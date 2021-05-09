"""
Controllers for Authentication
"""

from werkzeug.security import generate_password_hash, check_password_hash
from flask import (
    render_template,
    request,
    redirect,
    url_for,
    session,
    jsonify,
)
from .models import (
    new_user, 
    get_user, 
)

def auth():
    return render_template('auth.html')

def register():
    name = request.form['name'] 
    email = request.form['email']
    password = generate_password_hash(request.form['password'], 'sha256')
    if not new_user(name, email, password):
        return ('User alresdy registered', 200)
    session['username'] = name
    session['role'] = 'user'    
    return ('DATABASE INSERTION COMPLETE' , 200)    #REDIRECT ROUTE 
    
    
def login():
    email = request.form['email']
    password = request.form['password']
    user = get_user(email)
    if not user:
        return ('Email or Password incorrect', 200)
    if not check_password_hash(user.password, password):
        return ('Email or Password incorrect', 200)
    session['username'] = user.name
    session['role'] = user.role
    return user.as_json()

def logout():
    session.pop('username')
    session.pop('role')
    return redirect(url_for('index'))
