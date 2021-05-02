

from os import environ

from flask import Flask



def app_factory():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = environ['SECRET']


    from .views import (index , blog_create , blog_update)

    app.add_url_rule('/', view_func=index)
    
    # View functions for Create and update blog 
    app.add_url_rule('/blog-create' , view_func=blog_create) 
    app.add_url_rule('/blog-update/<title>' , view_func=blog_update) 
    

    
    return app
