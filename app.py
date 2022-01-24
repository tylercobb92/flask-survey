from flask import Flask, redirect, render_template, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "onomatopoeia"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)


RESPONSES_KEY = 'responses'


@app.route('/')
def get_started():
    return render_template('start_survey.html', survey=survey)


@app.route('/start', methods=['POST'])
def start_survey():
    session[RESPONSES_KEY] = []

    return redirect('/questions/0')


@app.route('/answer', methods=["POST"])
def get_answer():
    choice = request.form['choice']

    responses = session[RESPONSES_KEY]
    responses.append(choice)
    session[RESPONSES_KEY] = responses

    if(len(responses) == len(survey.questions)):
        res = session.get(RESPONSES_KEY)
        print(res)
        return redirect('/complete')

    else:
        return redirect(f'/questions/{len(responses)}')


@app.route('/questions/<int:question_id>')
def show_question(question_id):
    responses = session.get(RESPONSES_KEY)

    if (responses is None):
        return redirect('/')

    if(len(responses) == len(survey.questions)):
        return redirect('/complete')

    if(len(responses) != question_id):
        flash(f'Question ID {question_id} is invalid')
        return redirect(f'/questions/{len(responses)}')

    question = survey.questions[question_id]
    return render_template('question.html', question_id=question_id, question=question)


@app.route('/complete')
def finished_survey():
    return render_template('complete.html')
