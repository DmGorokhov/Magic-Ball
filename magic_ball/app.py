from flask import Flask, render_template, session
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
    answer = ''
    if form.validate_on_submit():
        question = form.question.data.strip()
        answer = get_answer()
        prediction = Prediction(question, answer, datetime.now())
        session.setdefault('predictions', []).append(prediction)
        return redirect(url_for('index'))

    return render_template('index.html',
                           form=form,
                           answer=answer,
                           predictions=session.get('predictions', []))
