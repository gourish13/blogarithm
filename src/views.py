"""
View related route controllers
"""

from flask import (
    render_template,
    request,
    redirect,
    url_for,
    session,
    jsonify,
)
from slugify import slugify


# @desc     Home Page
# @route    GET /
def index():
    return render_template('index.html')


def auth():
    return render_template('auth.html')

# @desc     Blog Create Page
# @route    GET /blog-create
# @route    POST /blog-create
def blog_create():
    if request.method == 'GET' :
        return render_template('blog-edit.html')
    blog_info = dict(request.form)
    blog_info['slug'] = slugify(request.form['blog-title'])
    return jsonify(blog_info)




# @desc     Blog Update Page
# @route    GET /blog-update/<string:slug>
# @route    POST /blog-update/<string:slug>
def blog_update(slug):
    if request.method == 'GET':
        return render_template('blog-edit.html' ,title='title' , content='blogcontent')
    blog_info = request.form
    return jsonify(blog_info)


# @desc     Blog View Page
# @route    GET /blog/<string:slug>
def blog_view(slug):
    return render_template('blogview.html', title='title', content='blogcontent')



# @desc     Privacy Policy
# @route    GET /privacy-policy
def privacy_policy():
    return render_template('privacy-policy.html')
