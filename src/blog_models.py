"""
Model for blog related data 
"""

from .models import db
from datetime import datetime

def new_blog(title , content , user , slug , blog_date = datetime.now()):
    _id = db.blogs.insert(title = title ,  content = content , posted_on = blog_date , author = user , slug = slug)
    db.commit() 
    
    return _id 
    
