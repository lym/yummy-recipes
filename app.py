from flask import Flask
from flask import render_template

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
