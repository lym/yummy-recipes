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


class RecipeUpdateController(MethodView):
    def post(self):
        user_id = request.form.get('user_id')
        title = request.form.get('title')
        description = request.form.get('description')
        fulfilled = request.form.get('fulfilled')

        if (user_id == '' or
            user_id is None
            or title == ''):
            abort(status.HTTP_400_BAD_REQUEST)

        recipe_id = request.form.get('recipe_id')
        if recipe_id is None:
            abort(400)
        Recipe.ds.update_recipe(
            recipe_id,
            user_id=user_id,
            title=title,
            description=description
        )
        return redirect(url_for('recipes') + recipe_id)
