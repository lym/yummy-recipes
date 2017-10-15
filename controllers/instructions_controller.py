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
    Recipe,
    Instruction,
)


class InstructionsController(MethodView):
    """ Controller for the instruction resource """
    def get(self, instruction_id):
        pass

    def post(self):
        user_id = int(request.form.get('user_id'))
        recipe_id = int(request.form.get('recipe_id'))
        title = request.form.get('title')
        description = request.form.get('description')

        if (user_id == '' or
            user_id is None or
            recipe_id == '' or
            recipe_id is None or
            title == ''):
            abort(status.HTTP_400_BAD_REQUEST)

        Instruction.ds.create_instruction(
            recipe_id=recipe_id,
            title=title,
            description=description
        )
        return redirect('/recipes/{}'.format(recipe_id))
