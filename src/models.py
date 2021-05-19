"""
Database models
"""

from os import environ
from pydal import DAL, Field

DB_URI = environ['DATABASE_URL']

db = DAL(DB_URI, lazy_tables=True)

db.define_table('users',
	Field('name', type='string', required=True, notnull=True),
	Field('email', type='string', required=True, notnull=True, unique=True),
	Field('password', type='string', required=False, notnull=False, default=None),
	Field('role', type='string', required=True, notnull=True, default='user')
	)


db.define_table('blogs' ,
    Field('title' , type='string' , required=True , notnull=True),
    Field('content',type='text' , required=True , notnull=True),
    Field('posted_on',type='date' , required=True , notnull=True),
    Field('user',type='reference users' , required=True , notnull=True , ondelete='CASCADE') ,
    Field('reported',type='boolean' , required=True , notnull=True , default=False),
    Field('slug',type='string' , required=True , notnull=True),
    Field('private',type='boolean' , required=True , notnull=True , default=False)
    )


db.define_table('comments',
    Field('comment' , type='string' , required=True , notnull=True),
    Field('commented_at' , type='datetime' , required=True , notnull=True),
    Field('blog' , type='reference blogs' , required=True , notnull=True , ondelete='CASCADE'),
    Field('user' , type='reference users' , required=True , notnull=True , ondelete='CASCADE')
    )


db.define_table('likes',
    Field('user' , type='reference users' , required=True , notnull=True , ondelete='CASCADE'),
    Field('blog' , type='reference blogs' , required=True , notnull=True , ondelete='CASCADE')
    )


db.commit()
