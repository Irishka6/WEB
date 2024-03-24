import os
import string
from random import choice

from flask import Flask, render_template, redirect, url_for, request, session
from data import db_session
from data.news import Jobs
from data.users import User
from data.department import Department
from datetime import datetime
from forms.loginform import LoginForm
from forms.workform import WorkForm
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from forms.user import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)
app.secret_key = ''.join(choice(string.ascii_letters) for _ in range(30))



def main():
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()
    db_sess.commit()
    app.run()

@app.route("/", methods=['GET', 'POST'])
def index1():
    try:
        db_sess = db_session.create_session()
        news = db_sess.query(Jobs).all()
        if request.method == 'POST':
            button_name = request.form['button']
            if button_name == 'wok':
                return redirect("/work")
        return render_template("index.html", news=news, name=session["guest"])
    except KeyError:
        db_sess = db_session.create_session()
        news = db_sess.query(Jobs).all()
        if request.method == 'POST':
            if request.form['wok'] == 'Добавить работу':
                return redirect("/work")
            if request.form['reg'] == 'Регистрация':
                return redirect("/register")
        return render_template("index.html", news=news, name='')


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
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            session['guest'] = user.name
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)

@app.route("/work", methods=['GET', 'POST'])
def work():
    form = WorkForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        print(form.team_leader.data, form.job.data, form.work_size.data, form.collaborators.data, datetime.now())
        worke = Jobs(team_leader=form.team_leader.data,
                     job=form.job.data,
                     work_size=form.work_size.data,
                     collaborators=str(form.collaborators.data),
                     start_date=datetime.now(),
                     end_date=datetime.now(),
                     is_finished=form.is_finished.data)

        db_sess.add(worke)
        db_sess.commit()
        return redirect("/")
    return render_template('work.html', form=form)

@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")

@app.route('/news/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_news(id):
    form = WorkForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        news = db_sess.query(Jobs).filter(Jobs.id == id
                                          ).first()
        if news:
            print(news.team_leader)
            form.team_leader.data = news.team_leader
            form.job.data = news.job
            form.work_size.data = news.work_size
            form.collaborators.data = news.collaborators
            form.is_finished.data = news.is_finished
        else:
            os.abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        news = db_sess.query(Jobs).filter(Jobs.id == id
                                          ).first()
        if news:
            news.team_leader = form.team_leader.data
            news.job = form.job.data
            news.collaborators = form.collaborators.data
            news.work_size = form.work_size.data
            news.is_finished = form.is_finished.data
            db_sess.commit()
            return redirect('/')
        else:
            os.abort(404)
    return render_template('work.html',
                           title='Редактирование новости',
                           form=form
                           )

@app.route('/news_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def news_delete(id):
    db_sess = db_session.create_session()
    news = db_sess.query(Jobs).filter(Jobs.id == id).first()
    if news:
        db_sess.delete(news)
        db_sess.commit()
    else:
        os.abort(404)
    return redirect('/')

if __name__ == '__main__':
    main()
