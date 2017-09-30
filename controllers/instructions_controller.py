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
    Recipe,
    Instruction,
)


class InstructionsController(MethodView):
    """ Controller for the instruction resource """
    def get(self, instruction_id):
        if instruction_id is None:
            instructions = Instruction.all()
            print('No instruction Id is being supplied')
            return 'We have content'
        else:
            table = Instruction.db.table('instructions')
            instruction = table.get(where('id') == instruction_id)
            if instruction is None:
                abort(404)
            else:
                print(instruction)
                return render_template('instructions/show.html', instruction=instruction)

    def post(self):
        user_id = request.form.get('user_id')
        recipe_id = request.form.get('recipe_id')
        title = request.form.get('title')
        description = request.form.get('description')

        if (user_id == '' or
            user_id is None or
            recipe_id == '' or
            recipe_id is None or
            title == ''):
            abort(status.HTTP_400_BAD_REQUEST)

        Instruction.create(recipe_id=recipe_id, title=title, description=description)
        print(request.form)
        res = status.HTTP_201_CREATED
        return redirect('/recipes/{}'.format(recipe_id))
