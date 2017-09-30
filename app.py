from flask import (
    Flask,
    redirect,
    session,
    url_for,
)
from flask import render_template

from models import Recipe

from controllers import (
        LoginController,
        UsersController,
        RecipesController,
        InstructionsController,
)

app = Flask(__name__)

@app.route("/")
def landing_page():
    return render_template(
        'landing_page.html', name='landingpage-template'
    )

@app.route("/register")
def register():
    return render_template('register.html', name='registration')

@app.route("/login")
def login():
    return render_template('login.html', name='login')

@app.route("/logout")
def logout():
    session.pop('email', None)
    return redirect(url_for('landing_page'))

@app.route("/dashboard")
def dashboard():
    recipes =  Recipe.all()
    return render_template('dashboard.html', name='dashboard', recipes=recipes)

@app.route("/new_recipe")
def new_recipe():
    return render_template('recipes/new.html', name="new_recipe")

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

app.secret_key = 'K5A34_zr=sdfjgq29kd'
