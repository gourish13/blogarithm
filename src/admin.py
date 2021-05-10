"""
Admin Controllers
"""

from werkzeug.security import generate_password_hash
from .models import new_user

def new_superuser():
	from getpass import getpass
	from sys import exit
    
	name = input('Name: ')
	email = input('Email: ')
	while True:
		password = getpass()
		if password == getpass('Confirm Password: '):
			password = generate_password_hash(password, 'sha256')
			new_user(name, email, password, superuser=True)
			print('Superuser created')
			exit()
		print('Password does not match. Try again')