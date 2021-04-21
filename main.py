
from src import app_factory

app = app_factory()

if __name__ == '__main__':
    app.run(debug = True)
