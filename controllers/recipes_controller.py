from flask import (
    abort,
    redirect,
    request,
    render_template,
    url_for,
)
from flask.views import MethodView
from flask_api import status

from models import (
    User,
    Recipe,
)


class RecipesController(MethodView):
    """ Controller for the user resource """
    def post(self):
        user_id = request.form.get('user_id')
        title = request.form.get('title')
        description = request.form.get('description')
        fulfilled = request.form.get('fulfilled')

        if (user_id == '' or
            user_id is None
            or title == ''):
            abort(status.HTTP_400_BAD_REQUEST)

        Recipe.create(user_id=user_id, title=title, description=description)
        print(request.form)
        res = status.HTTP_201_CREATED
        return redirect(url_for('dashboard'))
