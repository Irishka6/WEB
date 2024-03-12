from flask import Flask, render_template, request, url_for, redirect


app = Flask(__name__)
t = {'acc': 'No', 'about':''}
@app.route('/auto_answer')
def index():
    return render_template('auto_answer.html', surname=t['famil'], name=t['name'], obr=t['class'], prof=t['accept'], sex=t['sex'], mot=t['about'], mur= t['acc'])

@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    global t
    if request.method == 'GET':
        return render_template('index.html', u=url_for('static', filename='css/style.css'))
    elif request.method == 'POST':
        t['famil'] = request.form['famil']
        t['name'] = request.form['name']
        t['email'] = request.form['email']
        t['class'] = request.form['class']
        t['accept'] = request.form['accept']
        t['sex'] = request.form['sex']
        t['about'] = '' if '' == request.form['about'] else request.form['about']
        t['acc'] = request.form['acc']
        print(t)
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')