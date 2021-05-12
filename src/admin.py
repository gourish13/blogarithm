"""
Admin Controllers
"""

from werkzeug.security import generate_password_hash
from .user_models import new_user

def new_superuser():
	from getpass import getpass
	from sys import exit
    
	name = input('Name: ')
	email = input('Email: ')
	while True:
		password = getpass()
		if password == getpass('Confirm Password: '):
			password = generate_password_hash(password, 'sha256')
			if new_user(name, email, password, superuser=True):
				print('Superuser created')
			else:
				print('Account already exist with the entered email')
			exit()
		print('Password does not match. Try again')