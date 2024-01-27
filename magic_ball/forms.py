from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class QuestionForm(FlaskForm):
    question = StringField(
        label='', validators=[DataRequired()],
        render_kw={"placeholder": "Напишите здесь Ваш вопрос"})
    submit = SubmitField('Найти ответ')
