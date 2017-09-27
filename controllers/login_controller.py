from flask import (
    abort,
    redirect,
    request,
    session,
    url_for
)
from flask.views import MethodView

from models import User


class LoginController(MethodView):
    def post(self):
        email = request.form.get('email')
        passw = request.form.get('password')
        if User.valid_user(email, passw):
            # res = {'email': email, 'status': 'OK'}
            session['email'] = email
            return redirect(url_for('dashboard'))

        print('Email: {}\nPass: {}'.format(email, passw))
        abort(401)
