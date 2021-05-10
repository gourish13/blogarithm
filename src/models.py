"""
Database models
"""

from os import environ
from pydal import DAL, Field

DB_URI = environ['DATABASE_URL']

db = DAL(DB_URI, pool_size=5)

db.define_table('users',
	Field('name', type='string', required=True, notnull=True),
	Field('email', type='string', required=True, notnull=True, unique=True),
	Field('password', type='string', required=False, notnull=False, default=None),
	Field('role', type='string', required=True, notnull=True, default='user')
	)


db.define_table('blogs' , 
    Field('title' , type='string' , required=True , notnull=True) , 
    Field('content',type='text' , required=True , notnull=True) ,
    Field('posted_on',type='date' , required=True , notnull=True) ,
    Field('author',type='string' , required=True ,    notnull=True) ,
    Field('user',type='reference users' , required=True ,    notnull=True , ondelete='CASCADE') ,
    Field('reported',type='boolean' , required=True , notnull=True , default=False) ,
    Field('slug',type='string' , required=True , notnull=True) ,
    Field('private',type='boolean' , required=True , notnull=True , default=False)
    ) 


db.define_table('comments',
    Field('comment' , type='string' , required=True , notnull=True),
    Field('commented_at' , type='datetime' , required=True , notnull=True),
    Field('commenter' , type='string' , required=True , notnull=True),
    Field('blog' , type='reference blogs' , required=True , notnull=True , ondelete='CASCADE'),
    Field('user' , type='reference users' , required=True , notnull=True , ondelete='CASCADE')
    )


db.define_table('likes',
    Field('user' , type='reference users' , required=True , notnull=True , ondelete='CASCADE'),
    Field('blog' , type='reference blogs' , required=True , notnull=True , ondelete='CASCADE')
    )


db.commit()

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
                    db.users.name, db.users.password, db.users.role
                )
    return user if not user else user[0]

# Checking Registration
def is_registered(email):
    return db(db.users.email == email).count()
