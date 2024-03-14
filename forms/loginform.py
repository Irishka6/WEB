from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Id астранафта', validators=[DataRequired()])
    password = PasswordField('Пароль астранафта', validators=[DataRequired()])
    username2 = StringField('Id капитана', validators=[DataRequired()])
    password2 = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')