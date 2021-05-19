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
    flash
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
    next_url = request.args['next'] if 'next' in request.args else '/'
    if 'username' in session:
        return redirect(next_url)
    if 'name' in request.args:
        return render_template('auth.html',
            next=next_url, email=request.args['email'],
            name=request.args['name'], signup=True)
    if 'email' in request.args:
        return render_template('auth.html',
            next=next_url, logemail=request.args['email'])
    return render_template('auth.html', next=next_url)


def register():
    name = request.form['name']
    email = request.form['email']
    next_url = request.form['next']
    password = generate_password_hash(request.form['password'], 'sha256')
    hashed_otp = request.form['hashed-otp']
    otp = request.form['otp']
   

    if not check_password_hash(hashed_otp, otp):
        flash('Incorrect OTP, Verification Failed')
        return redirect(f'/auth?next={next_url}&email={email}&name={name}')

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
    if not user:
        flash('Incorrect Email or Password')
        return redirect(f'/auth?next={next_url}&email={email}')
    if not check_password_hash(user.password, password):
        flash('Incorrect Email or Password')
        return redirect(f'/auth?next={next_url}&email={email}')
    session['username'] = user.name
    session['role'] = user.role
    session['uid'] = user.id
    return redirect(next_url)


def logout():
    session.pop('username', None)
    session.pop('role', None)
    session.pop('uid', None)
    return redirect(url_for('index'))


def mailcheck(mode):
    email = request.args['email']
    registered = is_registered(email) if mode=="send" else None
    if not registered:
        otp = genkey()
        send_email('otp' , email , otp=otp)
        return jsonify(dict(otp = generate_password_hash(otp)))
    else:
        return jsonify(dict(status='is-danger'))


def resetpwd():
    email = request.args['email']
    if request.method=="GET":
        if is_registered(email):
            otp = genkey()
            send_email('reset password' , email , otp=otp)
            return jsonify(dict(otp = generate_password_hash(otp)))
        else:
            return jsonify(dict(status='is-danger'))
    else:
        pass
