from flask import (
    render_template,
    request,
    redirect,
    url_for,
    session,
    jsonify,
)
from .models import db

def auth():
    return render_template('auth.html')

def register():
    reg_data = request.form
    name = reg_data['name'] 
    email = reg_data['email']
    password = reg_data['password']
    
    
    #INSERTION TO DATABASE 
    try : 
        db.users.insert(name = name , email = email , password = password)
        db.commit()
        session['username'] = name
        session['role'] = 'user'
    except Exception as e:                   #DATABASE EXCEPTION HANDLING
        print(e)
        return ('ERROR in insertion' , 500)
    
    return ('DATABASE INSERTION COMPLETE' , 200)    #REDIRECT ROUTE 
    
    
def login():
    email = request.form['email']
    password = request.form['password']
    user = db(db.users.email==email & db.users.password==password).select(db.user.name , db.user.role)
    if not user:
        session['username'] = user.name
        session['role'] = user.role
        return users.as_json
    return ('USER DOES NOT EXIST' , 200)
