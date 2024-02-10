from flask import Flask, url_for, request


app = Flask(__name__)






@app.route('/')

def return_sample_page():
    return 'Миссия Колонизация Марса'

@app.route('/index')
def countdown():
    return 'И на Марсе будут яблони цвести!'

@app.route('/promotion')
def promotion():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <h1>Человечество вырастает из детства.</h1>
                  </body>
                  <body>
                    <h1>Человечеству мала одна планета.</h1>
                  </body>
                  <body>
                    <h1>Мы сделаем обитаемыми безжизненные пока планеты.</h1>
                  </body>
                  <body>
                    <h1>И начнем с Марса!</h1>
                  </body>
                  <body>
                    <h1>Присоединяйся!</h1>
                  </body>
                </html>"""
@app.route('/image_mars')
def image():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                  </body>
                  <img src="{url_for('static', filename='img/MARS-2.png')}" 
                    alt="здесь должна была быть картинка, но не нашлась">
                    <div class="alert alert-dark" role="alert">
                      Человечество вырастает из детства.
                    </div>
                    <div class="alert alert-success" role="alert">
                      Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-warning" role="alert">
                      И начнем с Марса!
                    </div>
                    <div class="alert alert-danger" role="alert">
                      Присоединяйся!
                    </div>
                </html>'''


@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1>Анкета претендента</h1>
                            <h2>На участие в миссии</h2>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="famil" class="form-control" id="famil" aria-describedby="emailHelp" placeholder="Введите фамилию" name="famil">
                                    <input type="name" class="form-control" id="name" placeholder="Введите имя" name="name">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Средне-техническое</option>
                                          <option>Вышее</option>
                                        </select>
                                     </div>
                                     <div class="form-group">
                                        <label for="classSelect">Какие у вас есть професии?</label>
                                        <div class="form-check">
                                          <input type="checkbox" class="form-check-input" id="a" name="accept">
                                          <label class="form-check-label" for="a">Инженер-иследователь</label>
                                        </div>
                                        <div class="form-check">
                                        <input type="checkbox" class="form-check-input" id="a" name="accept">
                                          <label class="form-check-label" for="a">Инженер-строитель</label>
                                        </div>
                                        <div class="form-check">
                                          <input type="checkbox" class="form-check-input" id="a" name="accept">
                                          <label class="form-check-label" for="a">Пилот</label>
                                        </div>
                                        <div class="form-check">
                                          <input type="checkbox" class="form-check-input" id="a" name="accept">
                                          <label class="form-check-label" for="a">Врач</label>
                                        </div>
                                        <div class="form-check">
                                          <input type="checkbox" class="form-check-input" id="a" name="accept">
                                          <label class="form-check-label" for="a">инженер жизнеобеспечения</label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в мисии?</label>
                                        <textarea class="form-con" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="acc">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе? </label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['famil'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['class'])
        print(request.form['accept'])
        print(request.form['sex'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['acc'])
        return "Форма отправлена"
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')