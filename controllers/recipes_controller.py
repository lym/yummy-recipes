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

from controllers import BaseController

class RecipesController(MethodView):
    """ Controller for the recipe resource """
    def get(self, recipe_id):
        if not BaseController.logged_in():  # send guests to landing page
            return redirect(url_for('landing_page'))
        if recipe_id is None:  # No specific id so return all
            recipe_coln =  Recipe.ds.storage.get('recipes')
            if (recipe_coln is None) or (len(recipe_coln)) == 0:
                recipes = []
            else:
                recipes = recipe_coln
            return render_template('recipes/index.html', recipes=recipes)
        else:  # Dealing with a particular recipe
            recipe = Recipe.ds.find_recipe(recipe_id)
            if recipe is None:  # Invalid recipe_id requested
                abort(404)
            else:
                return render_template(
                    'recipes/show.html',
                    recipe=recipe,
                    )

    def post(self):
        user_id = request.form.get('user_id')
        title = request.form.get('title')
        description = request.form.get('description')
        fulfilled = request.form.get('fulfilled')

        if (user_id == '' or
            user_id is None
            or title == ''):
            abort(status.HTTP_400_BAD_REQUEST)

        Recipe.ds.create_recipe(
            user_id=user_id,
            title=title,
            description=description
        )
        print(request.form)
        res = status.HTTP_201_CREATED
        return redirect(url_for('dashboard'))
