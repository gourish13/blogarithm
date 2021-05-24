"""
OAuth routes controllers
"""

from flask import (
    request,
    session,
    url_for,
    flash,
    redirect,
    jsonify,
)
from flask_oauthlib.client import OAuth

oauth = OAuth()

from .constants import (
    twitter_api_key,
    twitter_api_secret,
    google_api_key,
    google_api_secret,
    github_api_key,
    github_api_secret,
)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~Twitter~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

twitter = oauth.remote_app(
    'twitter',
    consumer_key=twitter_api_key,
    consumer_secret=twitter_api_secret,
    base_url='https://api.twitter.com/1.1/',
    request_token_url='https://api.twitter.com/oauth/request_token',
    access_token_url='https://api.twitter.com/oauth/access_token',
    authorize_url='https://api.twitter.com/oauth/authorize'
)


def twitter_login():
    callback = url_for('twitter_authorize', next=request.args['next'], _external=True)
    return twitter.authorize(callback = callback)


def twitter_authorize():
    resp = twitter.authorized_response()
    return jsonify(resp)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~Google~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

google = oauth.remote_app(
    'google',
    consumer_key=google_api_key,
    consumer_secret=google_api_secret,
    base_url='https://www.googleapis.com/oauth2/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    request_token_params={'scope': 'profile email'},
)


def google_login():
    callback = url_for('google_authorize', _external=True)
    session['next'] = request.args['next']
    return google.authorize(callback = callback)


def google_authorize():
    resp = google.authorized_response()
    session['token'] = (resp['access_token'], '')
    next_url = session['next']
    print(next_url)
    return jsonify(google.get('userinfo').data)


@google.tokengetter
def get_google_oauth_token():
    return session.get('token')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~Github~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

github = oauth.remote_app(
    'github',
    consumer_key=github_api_key,
    consumer_secret=github_api_secret,
    request_token_params={'scope': 'user:email'},
    base_url='https://api.github.com/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://github.com/login/oauth/access_token',
    authorize_url='https://github.com/login/oauth/authorize'
)


def github_login():
    callback = url_for('github_authorize', next=request.args['next'], _external=True)
    return github.authorize(callback = callback)


def github_authorize():
    resp = github.authorized_response()
    session['token'] = (resp['access_token'], '')
    return jsonify(github.get('user').data)


@github.tokengetter
def get_github_oauth_token():
    return session.get('token')
