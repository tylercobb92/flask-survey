from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "onomatopoeia"

debug = DebugToolbarExtension(app)


responses = []


@app.route('/')
def start_survey():
    return render_template('start_survey.html', survey=survey)
