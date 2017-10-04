from flask import (
    render_template,
    session,
)
from flask.views import View

from models import Recipe

class LandingPageController(View):
    def dispatch_request(self):
        current_user = session.get('user')
        if current_user is None:
            # If there's no user currently logged-in
            return render_template(
                'landing_page.html', name='landingpage-template'
            )
        else:
            recipe_coln =  Recipe.ds.storage.get('recipes')
            if (recipe_coln is None) or (len(recipe_coln)) == 0:
                recipes = []
            else:
                recipes = recipe_coln
            return render_template(
                'dashboard.html',
                name='dashboard',
                recipes=recipes
            )
