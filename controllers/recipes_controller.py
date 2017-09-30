from flask import (
    abort,
    redirect,
    request,
    render_template,
    url_for,
)
from flask.views import MethodView
from flask_api import status

from tinydb import where

from models import (
    User,
    Recipe,
)

from controllers import BaseController

class RecipesController(MethodView):
    """ Controller for the recipe resource """
    def get(self, recipe_id):
        if not BaseController.logged_in():  # send guests to landing page
            # abort(401)
            return redirect(url_for('landing_page'))
        if recipe_id is None:
            recipes = Recipe.all()
            print('No recipe Id is being supplied')
            return 'We have content'
        else:
            table = Recipe.db.table('recipes')
            recipe = table.get(where('id') == recipe_id)
            if recipe is None:
                abort(404)
            else:
                print(recipe)
                return render_template('recipes/show.html', recipe=recipe)

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
