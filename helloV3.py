# exemplo de flask com bootstrap
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'amigos para sempre'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data=''
    return render_template('name.html',
                           name=name,
                           form=form)

# retornara uma pagina de erro caso de erro 404
@app.errorhandler(404)
def error(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def error500(e):
    return render_template('500.html'), 500

# criando uma classe form para receber os dados no site
class NameForm(FlaskForm):
    name = StringField("Qual e o seu nome?", validators=[DataRequired()])
    submit = SubmitField("Entrar")