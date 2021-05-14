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
from .user_models import (
    new_user, 
    get_user, 
    is_registered
)
from .mail import send_email
from .otpgen import genkey


# Authentication Page
def auth():
    next_url = '/' + (request.args['next'] if 'next' in request.args else '')
    if 'username' in session:
        return redirect(next_url)
    return render_template('auth.html', next=next_url)


def register():
    name = request.form['name'] 
    email = request.form['email']
    next_url = request.form['next'] 
    password = generate_password_hash(request.form['password'], 'sha256')
    hashed_otp = request.form['hashed-otp']
    otp = request.form['otp']

    if not check_password_hash(otp, hashed_otp):
        message = f"<b>Unable to register, OTP does not match.<a href='/auth?next={next_url}'><i>Try Registering Again</i></a> .</b>"
        return (message, 403)
    
    uid = new_user(name, email, password)
    session['username'] = name
    session['role'] = 'user'    
    session['uid'] = uid
    return redirect(next_url)  
    
    
def login():
    email = request.form['email']
    password = request.form['password']
    next_url= request.form['next']
    user = get_user(email)
    message = f"<b>Email or Password incorrect. <a href='/auth?next={next_url}'><i>Try again</i> .</b>"
    if not user:
        return (message, 401)
    if not check_password_hash(user.password, password):
        return (message, 401)
    session['username'] = user.name
    session['role'] = user.role
    session['uid'] = user.id
    return redirect(next_url)


def logout():
    session.pop('username', None)
    session.pop('role', None)
    session.pop('uid', None)
    return redirect(url_for('index'))


def mailcheck():
    email = request.args['email']
    if not is_registered(email):
        otp = genkey()
        send_email('otp' , email , otp=otp)
        return jsonify(dict(otp = generate_password_hash(otp)))
    else:
        return jsonify(dict(status = 'is-danger'))
