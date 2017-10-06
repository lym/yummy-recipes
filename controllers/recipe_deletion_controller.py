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
        recipe_id = request.args.get('recipe_id')
        if recipe_id is None:
            abort(400)
        Recipe.ds.delete_recipe(recipe_id)
        return redirect(url_for('recipes'))
