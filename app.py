from flask import Flask, redirect, render_template, request, flash
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "onomatopoeia"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)


responses = []


@app.route('/')
def start_survey():
    return render_template('start_survey.html', survey=survey)


@app.route('/questions/<int:question_id>')
def show_question(question_id):
    if (responses is None):
        return redirect('/')

    if(len(responses) == len(survey.questions)):
        return redirect('/complete')

    if(len(responses) != question_id):
        flash(f'Question ID {question_id} is invalid')
        return redirect(f'/questions/{len(responses)}')

    question = survey.questions[question_id]
    return render_template('question.html', question_id=question_id, question=question)


@app.route('/answer', methods=["POST"])
def get_answer():
    answer = request.form['choice']
    responses.append(answer)

    if(len(responses) == len(survey.questions)):
        return redirect('/complete')

    else:
        return redirect(f'/questions/{len(responses)}')


@app.route('/complete')
def finished_survey():
    return render_template('complete.html')
