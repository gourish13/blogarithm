

from os import environ

from flask import Flask


def app_factory():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = environ['SECRET']
    
    return app
