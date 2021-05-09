
from src import app_factory

app = app_factory()

if __name__ == '__main__':
	from sys import argv
	if 'create-superuser' in argv:
		from src.admin import new_superuser
		new_superuser()
	app.run(debug = True)