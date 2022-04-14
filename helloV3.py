# exemplo de flask com bootstrap
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

# retornara uma pagina de erro caso de erro 404
@app.errorhandler(404)
def error(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def error500(e):
    return render_template('505.html'), 500