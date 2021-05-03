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
# @route    GET /blog-create
def blog_create():
    if request.method == 'GET' :
        return render_template('blog-edit.html')  
    
    blog_info = request.form 


# @desc     Blog Update Page
# @route    GET /blog-update/<string:slug>
def blog_update(slug): 
    if request.method == 'GET': 
        return render_template('blog-edit.html' ,title='title' , content='blogcontent') 
     
    blog_info = request.form        #RETURN JSON TO CLIENT   
        
        


# @desc     Blog View Page
# @route    GET /blog/<string:slug>
def blog_view(slug):
    return render_template('blogview.html' , title='title' , content='blogcontent')



