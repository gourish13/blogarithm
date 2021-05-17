

from os import environ

from flask import Flask


def app_factory():
    
    app = Flask(__name__)
    app.config['SECRET_KEY'] = environ['SECRET']
    app.config['TEMPLATES_AUTO_RELOAD'] = True

# View Routes
    from .views import (
            index,
            blog_view ,
            blog_create,
            blog_update,
            privacy_policy,
            page_not_found_404,
    )
    app.register_error_handler(404, page_not_found_404)
    app.add_url_rule('/', view_func=index)
    app.add_url_rule('/blog-create', view_func=blog_create, methods=['GET', 'POST'])
    app.add_url_rule('/blog-update/<string:slug>', view_func=blog_update, methods=['GET', 'POST'])
    app.add_url_rule('/blog/<string:slug>', view_func=blog_view)
    app.add_url_rule('/privacy-policy', view_func=privacy_policy)

# Auth Routes
    from .auth import (
        auth , 
        register,
        login,
        logout,
        mailcheck,
        resetpwd
     )
    app.add_url_rule('/auth' , view_func=auth)
    app.add_url_rule('/auth/register' , view_func=register , methods=['POST'])
    app.add_url_rule('/auth/login' , view_func=login , methods=['POST'])
    app.add_url_rule('/auth/logout' , view_func=logout)
    app.add_url_rule('/auth/otp/<string:mode>' , view_func=mailcheck)
    app.add_url_rule('/auth/resend-password' , view_func=resetpwd , methods=['POST'])
        
        
    return app
