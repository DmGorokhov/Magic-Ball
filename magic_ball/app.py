from flask import Flask, render_template, session, request
from magic_ball.settings import Configs
from flask_session import Session
from flask import redirect, url_for

from collections import namedtuple
from datetime import datetime

from .forms import QuestionForm
from magic_ball.services.answer_generator import get_answer

app = Flask(__name__)
configs = Configs()

app.config["SECRET_KEY"] = configs.secret_key
app.config["SESSION_PERMANENT"] = configs.session_permanent
app.config["SESSION_TYPE"] = configs.SESSION_TYPE

Session(app)

Prediction = namedtuple('Prediction', ['question', 'answer', 'date'])


@app.route("/", methods=["GET", "POST"])
def index():
    form = QuestionForm()
    return render_template('index.html',
                           form=form,
                           predictions=session.get('predictions', []))


@app.route('/submit-question', methods=['POST'])
def get_question():
    question = request.form.get('question')
    if question:
        clean_question = question.strip()
        return render_template('submit_input.html', question=clean_question)


@app.route('/answer', methods=['POST'])
def ask_answer():
    answer = get_answer()
    question = request.form.get('clean_question')
    prediction = Prediction(question, answer, datetime.now())
    session.setdefault('predictions', []).append(prediction)
    return redirect(url_for('index'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
