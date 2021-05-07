"""
Database models
"""

from os import environ
from pydal import DAL, Field

DB_URI = environ['DB_URI']

db = DAL(DB_URI, pool_size=5)

db.define_table('users',
	Field('name', type='string', required=True, notnull=True),
	Field('email', type='string', required=True, notnull=True, unique=True),
	Field('password', type='string', required=False, notnull=False, default=None),
	Field('role', type='string', required=True, notnull=True, default='user')
	)



db.commit()