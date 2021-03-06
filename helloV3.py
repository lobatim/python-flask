# exemplo de flask com bootstrap
from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# adicionando configuraçao de banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# adicionando uma chave secreta
app.config['SECRET_KEY'] = 'amigos para sempre'
# inicializando a database
db = SQLAlchemy(app)

@app.route('/')
def index():
    # apresenta uma mensagem de boas vindas
    return render_template('index.html')


@app.route('/user/add', methods=['GET', 'POST'])
def add_user():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user is None:
            user = Users(name=form.name.data, email=form.email.data)
            db.session.add(user)
            db.session.commit()
        name = form.name.data
        form.name.data = ''
        form.email.data = ''
        flash('usuario adicionado com suceso')
    our_users = Users.query.order_by(Users.date_add)
    return render_template('user_add.html', name=name,form=form,our_users=our_users)


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

# criando uma rota com metodo get e post, esses metodos servem para obter dados de um site e passar dados para esse
# site novamente.
@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NameForm()

    # essa condiçao verifica se o botao submit foi pressionado
    if form.validate_on_submit():
        # atribuindo os dados de form para name
        name = form.name.data
        # definindo os dados do form para nenhum, para que esse seja capaz de receber novos dados.
        form.name.data=''
        flash(" Seus dados foram carregados com sucesso !")
    return render_template('name.html',
                           name=name,
                           form=form)

# retornara uma pagina de erro caso de erro 404
@app.errorhandler(404)
def error(e):
    return render_template('404.html'), 404

# retornara uma pagina de erro caso de erro 500
@app.errorhandler(500)
def error500(e):
    return render_template('500.html'), 500


# criando uma classe form, essa classe ira gerenciar a entrada de textos na form da pagina
class NameForm(FlaskForm):
    name = StringField("Qual e o seu nome?", validators=[DataRequired()])
    email = StringField("Qual e o seu e-mail?", validators=[DataRequired()])
    submit = SubmitField("Entrar")



# criando uma classe que ira gerenciar a database
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False, unique=True)
    date_add = db.Column(db.DateTime, default=datetime.utcnow)


    def __repr__(self):
        return '<Name %r>' % self.name