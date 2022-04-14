import flask
from flask import Flask
app = Flask(__name__)


#retorna o texto ola mundo quando for acessado o site
@app.route('/')
def index():
    return '<h1> Ola mundo </h1>'


# esta funçao retorna uma pagina dizendo hello e o nome que for escrito em <name>
@app.route('/user/<name>')
def user(name):
    return '<h1> hello {} </h1>'.format(name)


#ira redirecionar para a pagina do tribalwars
@app.route('/jogo')
def jogo():
    return flask.redirect('https://www.tribalwars.com.br')


# caso o usuario acesse a pagina /testando/id e o numero de id nao esteja no servidor ele retorna um erro 404
@app.route('/testando/id')
def get_user(id):
    user = flask.abort.load_user(id)
    if not user:
        flask.abort(404)
    return '<h1> Hello, {} </h1>'.format(user.name)