from flask import (
    abort,
    redirect,
    request,
    session,
    url_for
)
from flask.views import MethodView

from models import (
    User,
    Recipe
)


class RecipeDeletionController(MethodView):
    def get(self):
        email = request.form.get('email')
        passw = request.form.get('password')

        recipe_id = request.args.get('recipe_id')
        if recipe_id is None:
            abort(400)
        Recipe.delete(recipe_id)
        return redirect(url_for('recipes'))
