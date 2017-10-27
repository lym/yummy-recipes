from flask import session
from flask import render_template
from flask.views import View

from models import Recipe

class DashboardController(View):
    def dispatch_request(self):
        if session.get('user') is None:
            return render_template('login.html', name='login')
        recipe_coln =  Recipe.ds.storage.get('recipes')
        if (recipe_coln is None) or (len(recipe_coln)) == 0:
            recipes = []
        else:
            recipes = recipe_coln
        print('Dashboard Recipe is: {}'.format(recipes))
        return render_template(
            'dashboard.html',
            name='dashboard',
            recipes=recipes
        )
