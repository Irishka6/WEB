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
@app.route('/results/<nickname>/<int:level>/<float:rating>')
def image(nickname, level, rating):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Результат</title>
                  </head>
                  <body>
                    <h1>Результаты отбора</h1>
                  </body>
                  <body>
                    <h2>Претендента на участие в мисси {nickname}:</h2>
                  </body>
                    <div class="alert alert-success" role="alert">
                      Поздравляем! Ваш рейтинг после {level} этапа отбора
                    </div>
                    <body>
                      <h3>составляет {rating}!</h3>
                    </body>
                    <div class="alert alert-warning" role="alert">
                      Желаем удачи!
                    </div>
                </html>'''
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')