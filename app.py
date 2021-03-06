from flask import (
    Flask,
    redirect,
    request,
    session,
    url_for,
)
from flask import render_template

from models import Recipe

from controllers import (
        LandingPageController,
        DashboardController,
        LoginController,
        UsersController,
        RecipesController,
        InstructionsController,
        RecipeDeletionController,
        RecipeUpdateController,
        NewRecipeController,
)

app = Flask(__name__)

@app.route("/register")
def register():
    return render_template('register.html', name='registration')

@app.route("/login")
def login():
    return render_template('login.html', name='login')

@app.route("/logout")
def logout():
    if session.get('user'):
        session.pop('user')
    if session.get('email'):
        session.pop('email', None)
    return redirect(url_for('landing_page'))

@app.route("/edit_recipe")
def edit_recipe():
    recipe_id = int(request.args.get('recipe'))
    recipe = Recipe.ds.find_recipe(recipe_id)

    return render_template(
        'recipes/edit.html',
        name="new_recipe",
        user=session.get('user'),
        recipe=recipe
    )

@app.route("/new_instruction")
def new_instruction():
    return render_template(
        'instructions/new.html',
        name="new_instruction",
        user=session.get('user'),
        recipe_id=request.args.get('recipe')
    )

app.add_url_rule('/', view_func=LandingPageController.as_view('landing_page'))

app.add_url_rule(
    '/new_recipe', view_func=NewRecipeController.as_view('new_recipe')
)

app.add_url_rule(
    '/dashboard',
    view_func=DashboardController.as_view('dashboard')
)

app.add_url_rule('/returning/', view_func=LoginController.as_view('returning'))

app.add_url_rule(
    '/users/',
    view_func=UsersController.as_view('user-registration')
)

recipes_url = RecipesController.as_view('recipes')
instructions_url = InstructionsController.as_view('instructions')

app.add_url_rule(
    '/recipes/',
    defaults={'recipe_id': None},
    view_func=recipes_url,
    methods=['GET',]
)
app.add_url_rule(
    '/recipes/',
    view_func=recipes_url,
    methods=['POST',]
)
app.add_url_rule(
    '/recipes/<int:recipe_id>',
    view_func=recipes_url,
    methods=['GET', 'PUT', 'DELETE']
)

app.add_url_rule(
    '/instructions/',
    defaults={'instruction_id': None},
    view_func=instructions_url,
    methods=['GET',]
)
app.add_url_rule(
    '/instructions/',
    view_func=instructions_url,
    methods=['POST',]
)
app.add_url_rule(
    '/instructions/<int:instruction_id>',
    view_func=instructions_url,
    methods=['GET', 'PUT', 'DELETE']
)

app.add_url_rule(
    '/delete_recipe',
    view_func=RecipeDeletionController.as_view('delete_recipe'),
    methods=['POST']
)

app.add_url_rule(
    '/update_recipe',
    view_func=RecipeUpdateController.as_view('update_recipe'),
    methods=['POST']
)

app.secret_key = 'K5A34_zr=sdfjgq29kd'
