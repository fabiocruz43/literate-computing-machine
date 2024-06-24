from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cadastro.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Exemplo de modelo SQLAlchemy para Profissional
class Profissional(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

# Exemplo de modelo SQLAlchemy para Cliente
class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)

# Formulário WTForms para Cadastro de Profissional
class CadastroProfissionalForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    confirmar_senha = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo('senha')])
    submit = SubmitField('Cadastrar')

# Formulário WTForms para Cadastro de Cliente
class CadastroClienteForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired()])
    telefone = StringField('Telefone', validators=[DataRequired()])
    submit = SubmitField('Cadastrar')

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html', title='Neral Agência Virtual')

# Rota para cadastrar um novo profissional
@app.route('/cadastrar_profissional', methods=['GET', 'POST'])
def cadastrar_profissional():
    form = CadastroProfissionalForm()
    if form.validate_on_submit():
        # Processamento do formulário
        profissional = Profissional(nome=form.nome.data, email=form.email.data, senha=form.senha.data)
        db.session.add(profissional)
        db.session.commit()
        flash('Profissional cadastrado com sucesso!', 'success')
        return redirect(url_for('index'))
    return render_template('cadastrar_profissional.html', form=form)

# Rota para cadastrar um novo cliente
@app.route('/cadastrar_cliente', methods=['GET', 'POST'])
def cadastrar_cliente():
    form = CadastroClienteForm()
    if form.validate_on_submit():
        # Processamento do formulário
        cliente = Cliente(nome=form.nome.data, email=form.email.data, telefone=form.telefone.data)
        db.session.add(cliente)
        db.session.commit()
        flash('Cliente cadastrado com sucesso!', 'success')
        return redirect(url_for('index'))
    return render_template('cadastrar_cliente.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
