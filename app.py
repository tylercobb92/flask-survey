from cgitb import html
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SECRET_KEY'] = "onomatopoeia"

debug = DebugToolbarExtension(app)


@app.route('/')
def home_page():
    return """<h1> Home Page </h1>"""
