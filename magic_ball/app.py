from flask import Flask, render_template
from magic_ball.settings import Configs

app = Flask(__name__)
configs = Configs()

app.config["SECRET_KEY"] = configs.secret_key


@app.route("/")
def index():
    return render_template('index.html')
