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
from .blog_models import new_blog

# @desc     Home Page
# @route    GET /
def index():
    return render_template('index.html')



# @desc     Blog Create
# @route    GET /blog-create
# @route    POST /blog-create
def blog_create():
    
    if request.method == 'GET' :
        return render_template('blog-edit.html')
    
    blog_info = dict(request.form)
    blog_info['slug'] = slugify(request.form['blog-title'])
    blog_info['user'] = session['username']
    if blog_info['private'] == 'true' :
        _id = new_blog(blog_info['blog-title'] , blog_info['content'] , blog_info['user'] , blog_info['slug'] ,private = True)
    else:
        _id = new_blog(blog_info['blog-title'] , blog_info['content'] , blog_info['user'] , blog_info['slug'])
    
    
    view_url  = '/blog/' + blog_info['slug'] + '/' + str(_id)
    return redirect(view_url)
    
    




# @desc     Blog Update
# @route    GET /blog-update/<string:slug>
# @route    POST /blog-update/<string:slug>
def blog_update(slug):
    if 'username' in session:
        if request.method == 'GET':
            return render_template('blog-edit.html' ,title='title' , content='blogcontent')
        return jsonify(request.form)
    url = '/auth?next=blog-update/'+slug 
    return redirect(url)


# @desc     Blog View Page
# @route    GET /blog/<string:slug>
def blog_view(slug):
    if 'username' in session:
        return render_template('blogview.html', title='title', content='blogcontent')
    url = '/auth?next=blog-view/'+slug 
    return redirect(url)



# @desc     Privacy Policy
# @route    GET /privacy-policy
def privacy_policy():
    return render_template('privacy-policy.html')
