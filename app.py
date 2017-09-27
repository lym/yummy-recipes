from flask import Flask
from flask import render_template

from controllers import (
        LoginController,
        UsersController,
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

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html', name='dashboard')


app.add_url_rule('/returning/', view_func=LoginController.as_view('returning'))

app.add_url_rule(
    '/users/',
    view_func=UsersController.as_view('user-registration')
)

app.secret_key = 'K5A34_zr=sdfjgq29kd'
