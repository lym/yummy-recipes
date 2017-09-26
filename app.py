from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def landing_page():
    return render_template(
        'landing_page.html', name='landingpage-template'
    )
