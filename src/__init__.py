

from os import environ

from flask import Flask


def app_factory():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = environ['SECRET']


    from .views import (
            index,
            blog_view
    )

    app.add_url_rule('/', view_func=index)
    app.add_url_rule('/blog/<string:slug>', view_func=blog_view)

    
    return app
