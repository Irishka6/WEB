from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, EmailField, IntegerField, BooleanField
from wtforms.validators import DataRequired


class WorkForm(FlaskForm):
    team_leader = StringField('Тим-лид')
    job = StringField('Название работы')
    work_size = IntegerField('Длительность работы')
    collaborators = StringField("Команда")
    is_finished = BooleanField("Закончена", default=0)
    submit = SubmitField('Войти')