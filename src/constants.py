"""
env vars
"""

from os import environ

EMAIL = environ['EMAIL']

DATABASE_URL = environ['DATABASE_URL']

twitter_api_key = environ['TWITTER_API_KEY']
twitter_api_secret = environ['TWITTER_API_SECRET']

google_api_key = environ['GOOGLE_API_KEY']
google_api_secret = environ['GOOGLE_API_SECRET']

github_api_key = environ['GITHUB_API_KEY']
github_api_secret = environ['GITHUB_API_SECRET']
