import os

from flask import Flask, render_template, redirect, url_for, request
from data import db_session
from data.news import Jobs
from data.users import User
from data.department import Department
from datetime import datetime
from forms.loginform import LoginForm
from forms.user import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()
    for user in db_sess.query(Department).filter(Department.id == 1):
        for i in user.members.split(', '):
            t = 0
            for use in db_sess.query(Jobs).all():
                if str(i) in use.collaborators:
                    t += use.work_size
            if t >= 25:
                u = db_sess.query(User).filter(User.id == int(i))
                print(f'{u.surname} {u.name}')
    db_sess.commit()
    app.run()

@app.route("/")
def index():
    db_sess = db_session.create_session()
    news = db_sess.query(Jobs).all()
    return render_template("index.html", news=news)

@app.route("/table/<sex>/<age>")
def coloree(sex, age):
    if sex == 'male':
        if int(age) >= 21:
            return render_template("colore.html", im='https://papik.pro/uploads/posts/2023-03/1678454094_papik-pro-p-milii-prishelets-risunok-30.jpg', colore='#008cf0')
        else:
            return render_template("colore.html", im='https://papik.pro/uploads/posts/2021-11/1636522927_7-papik-pro-p-milii-inoplanetyanin-risunok-7.jpg', colore='#8aceff')
    else:
        if int(age) >= 21:
            return render_template("colore.html", im='https://papik.pro/uploads/posts/2023-03/1678454094_papik-pro-p-milii-prishelets-risunok-30.jpg', colore='#ff0000')
        else:
            return render_template("colore.html", im='https://papik.pro/uploads/posts/2021-11/1636522927_7-papik-pro-p-milii-inoplanetyanin-risunok-7.jpg', colore='#ffa799')





@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            surname=form.surname.data,
            name=form.name.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data,
            email=form.email.data,

        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)

@app.route('/distribution')
def distribution():
    return render_template('cauta.html', user_list=['Ридли Скотт', "Энди Уэт", "Марк Утони", "Винката Капур", "utgyuhiujiok"])

@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return render_template('form.html', t='')
    if request.method == 'POST':
        f = request.files['file']
        return render_template('form.html', t=f)

@app.route('/static')
def statice():
    return render_template('carusel.html')

if __name__ == '__main__':
    main()
