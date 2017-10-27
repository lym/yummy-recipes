from flask import (
    render_template,
    session,
)
from flask.views import MethodView

class NewRecipeController(MethodView):
    """ Renders the New Recipe view """
    def get(self):
        user = session.get('user')
        if user is None:
            return render_template(
                'landing_page.html', name='landingpage-template'
            )
        return render_template(
            'recipes/new.html',
            name="new_recipe",
            user=user
        )
