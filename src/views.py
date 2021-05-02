"""
View related route controllers
"""

from flask import (
    render_template,
    request,
    redirect,
    url_for,
    session,
)


# @desc     Home Page
# @route    GET /
def index():
    return render_template('index.html')



# @desc     Blog Create Page
# @route    GET /blog/<string:slug>
def blog_create():
    return render_template('blog-edit.html') 



# @desc     Blog Update Page
# @route    GET /blog-create
def blog_update(slug): 
    return render_template('blog-edit.html') 



# @desc     Blog View Page
# @route    GET /blog-update/<string:slug>
def blog_view(slug):
    return render_template('blogview.html' , title='title' , content='blogcontent')



