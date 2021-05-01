"""
View related route controllers
"""

from flask import render_template

# @desc     Home Page
# @route    GET /
def index():
    return render_template('index.html')
