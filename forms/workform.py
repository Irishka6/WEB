from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, EmailField, IntegerField, BooleanField
from wtforms.validators import DataRequired


class WorkForm(FlaskForm):
    team_leader = IntegerField('Тим-лид', validators=[DataRequired()])
    job = StringField('Название работы', validators=[DataRequired()])
    work_size = IntegerField('Длительность работы', validators=[DataRequired()])
    collaborators = StringField("Команда", validators=[DataRequired()])
    is_finished = BooleanField("Закончена", default=0)
    submit = SubmitField('Войти')