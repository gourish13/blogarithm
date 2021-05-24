

from os import environ

from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = environ['SECRET']

def app_factory():

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

    from .oauth import (
        twitter_login,
        twitter_authorize,
        google_login,
        google_authorize,
        github_login,
        github_authorize,
    )
    app.add_url_rule('/login/twitter', view_func=twitter_login)
    app.add_url_rule('/login/twitter/authorize', view_func=twitter_authorize)
    app.add_url_rule('/login/google', view_func=google_login)
    app.add_url_rule('/login/google/authorize', view_func=google_authorize)
    app.add_url_rule('/login/github', view_func=github_login)
    app.add_url_rule('/login/github/authorize', view_func=github_authorize)

    return app
