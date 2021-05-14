"""
User model for user data
"""

from .models import db

from psycopg2.errors import UniqueViolation

# Create a new user account
def new_user(name, email, password, superuser = False):
    try:
        if not superuser: 
            db.users.insert(
                name = name , email = email , password = password
            )
        else:
            db.users.insert(
                name = name , email = email , password = password, role='superuser'
            )
    except UniqueViolation as _:
        return None
    db.commit()
    return True



# Get user data by email
def get_user(email):
    user = db(db.users.email == email).select(
                    db.users.id, db.users.name, db.users.password, db.users.role
                )
    return user if not user else user[0]

# Checking Registration
def is_registered(email):
    return db(db.users.email == email).count()
