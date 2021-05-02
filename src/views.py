"""
View related route controllers
"""

from flask import render_template

# @desc     Home Page
# @route    GET /
def index():
    return render_template('index.html')

def blog_view(slug):
    return render_template('blogview.html' , title=title , content=blogcontent)