

from os import environ

from flask import Flask


def app_factory():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = environ['SECRET']
    app.config['TEMPLATES_AUTO_RELOAD'] = True

    from .views import (
            index,
            blog_view , 
            blog_create , 
            blog_update
    )

    app.add_url_rule('/', view_func=index)
    app.add_url_rule('/blog-create', view_func=blog_create) 
    app.add_url_rule('/blog-update/<string:slug>', view_func=blog_update) 
    app.add_url_rule('/blog/<string:slug>', view_func=blog_view)


    return app
