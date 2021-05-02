"""
View related route controllers
"""

from flask import render_template

# @desc     Home Page
# @route    GET /
def index():
    return render_template('index.html')

#Create View function
def blog_create():
    return render_template('blog-edit.html') 

#Update View function     
def blog_update(title): 
    return render_template('blog-edit.html') 
    

        
    