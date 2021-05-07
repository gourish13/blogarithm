from flask import (
    render_template,
    request,
    redirect,
    url_for,
    session,
    jsonify,
)


def auth():
    if request.method == 'GET' :
        return render_template('auth.html')

