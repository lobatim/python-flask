from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    # retorna a pagina index.html no navegador, index.html precisa existir na pasta templates
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    #retorna a pagina user.html com argumento name, user.html precisa existir na pasta templates
    return render_template('user.html', name=name)
