"""
Model for blog related data
"""

from .models import db
from datetime import datetime

def new_blog(user_id, title , content, slug):
    _id = db.blogs.insert(
            title=title,
            content=content,
            user=user_id,
            posted_on=datetime.now().date(),
            slug = slug
    )
    db.commit()
    return _id


def get_blog(blog_id , slug):
    blog_info = db((db.blogs.id == blog_id) & (db.blogs.slug == slug)).select(
                    db.users.title, db.users.content
                )
    return blog_info








def add_comment(user_id, blog_id, comment):
    db.comments.insert(
            comment=comment,
            commented_on=datetime.now(),
            user=user_id,
            blog=blog_id
    )
    db.commit()













def add_like(user_id, blog_id):
    db.likes.insert(user-user_id, blog=blog_id)
    db.commit()
