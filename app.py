import streamlit as st
import mercadopago
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configuração inicial do Mercado Pago
SEU_ACCESS_TOKEN = os.getenv("MERCADO_PAGO_ACCESS_TOKEN")
if not SEU_ACCESS_TOKEN:
    st.error("O token de acesso do Mercado Pago não foi encontrado. Certifique-se de definir a variável de ambiente corretamente.")
else:
    mp = mercadopago.SDK(SEU_ACCESS_TOKEN)

# Dados fictícios para simular o funcionamento do sistema
categorias = ['Domésticos', 'Construção e Reformas', 'Técnicos']
profissoes = {
    'Domésticos': ['Cozinheira', 'Passadeira', 'Babá', 'Cuidador de Idosos', 'Diarista', 'Faxineira'],
    'Construção e Reformas': ['Pedreiro', 'Pintor', 'Carpinteiro', 'Marceneiro', 'Gesseiro'],
    'Técnicos': ['Eletricista', 'Técnico em Informática', 'Técnico em Enfermagem', 'Técnico em Segurança do Trabalho', 'Técnico em Edificações']
}

# Função para o cadastro de cliente
def cadastrar_cliente():
    st.subheader('Cadastro de Cliente')
    nome = st.text_input('Nome:')
    cpf = st.text_input('CPF:')
    endereco = st.text_input('Endereço:')
    identidade_file = st.file_uploader('Envie uma cópia do documento de identidade (RG ou CNH):', type=['pdf', 'jpg', 'png', 'jpeg'])
    comprovante_residencia_file = st.file_uploader('Envie uma cópia do comprovante de residência:', type=['pdf', 'jpg', 'png', 'jpeg'])
    whatsapp = st.text_input('Telefone (WhatsApp):')

    if st.button('Confirmar cadastro'):
        st.success('Cadastro de cliente realizado com sucesso!')

# Função para o cadastro de profissional
def cadastrar_profissional():
    st.subheader('Cadastro de Profissional')
    nome = st.text_input('Nome:')
    cpf = st.text_input('CPF:')
    identidade_file = st.file_uploader('Envie uma cópia do documento de identidade (RG ou CNH):', type=['pdf', 'jpg', 'png', 'jpeg'])
    endereco = st.text_input('Endereço:')
    comprovante_residencia_file = st.file_uploader('Envie uma cópia do comprovante de residência:', type=['pdf', 'jpg', 'png', 'jpeg'])
    whatsapp = st.text_input('Telefone (WhatsApp):')

    st.subheader('Selecione os serviços que você oferece:')
    servicos_oferecidos = {}

    for categoria in categorias:
        st.write(f"### Categoria: {categoria}")
        profissoes_categoria = profissoes.get(categoria, [])
        for profissao in profissoes_categoria:
            servicos_oferecidos[profissao] = st.checkbox(f"{profissao}")

    if st.button('Confirmar cadastro'):
        st.success('Cadastro de profissional realizado com sucesso!')

# Interface principal usando Streamlit
def main_streamlit():
    st.title('Neral Agência Virtual')
    st.write('Seja bem-vindo!')
    st.write('Antes de usar nossos serviços, precisamos que realize seu cadastro logo abaixo.')

    opcao = st.radio('Você é:', ['Cliente: Cadastre-se', 'Profissional: Cadastre-se'])

    if opcao == 'Cliente: Cadastre-se':
        cadastrar_cliente()

    elif opcao == 'Profissional: Cadastre-se':
        cadastrar_profissional()

from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'mysecret')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///cadastro.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Modelo de usuário
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

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

# Formulário WTForms para Login de Usuário
class LoginForm(FlaskForm):
    username = StringField('Nome de usuário', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Login')

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html', title='Neral Agência Virtual')

# Rota para cadastrar um novo profissional
@app.route('/cadastrar_profissional', methods=['GET', 'POST'])
def cadastrar_profissional_flask():
    form = CadastroProfissionalForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.senha.data, method='sha256')
        profissional = Profissional(nome=form.nome.data, email=form.email.data, senha=hashed_password)
        db.session.add(profissional)
        db.session.commit()
        flash('Profissional cadastrado com sucesso!', 'success')
        return redirect(url_for('index'))
    return render_template('cadastrar_profissional.html', form=form)

# Rota para cadastrar um novo cliente
@app.route('/cadastrar_cliente', methods=['GET', 'POST'])
def cadastrar_cliente_flask():
    form = CadastroClienteForm()
    if form.validate_on_submit():
        cliente = Cliente(nome=form.nome.data, email=form.email.data, telefone=form.telefone.data)
        db.session.add(cliente)
        db.session.commit()
        flash('Cliente cadastrado com sucesso!', 'success')
        return redirect(url_for('index'))
    return render_template('cadastrar_cliente.html', form=form)

# Rota para login
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Login bem-sucedido!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Credenciais inválidas. Tente novamente.', 'danger')
    return render_template('login.html', form=form)

# Rota para logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout realizado com sucesso.', 'info')
    return redirect(url_for('index'))

# Rota protegida
@app.route('/minha_rota_protegida')
@login_required
def minha_rota_protegida():
    return render_template('rota_protegida.html')

if __name__ == '__main__':
    app.run(debug=True)