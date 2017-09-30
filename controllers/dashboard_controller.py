from flask import render_template
from flask.views import View

from models import Recipe

class DashboardController(View):
    def dispatch_request(self):
        recipes =  Recipe.all()
        return render_template(
            'dashboard.html',
            name='dashboard',
            recipes=recipes
        )
