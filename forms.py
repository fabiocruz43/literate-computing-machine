# Exemplo fictício
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CadastroProfissionalForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    senha = StringField('Senha', validators=[DataRequired()])
    confirmar_senha = StringField('Confirmar Senha', validators=[DataRequired()])
    submit = SubmitField('Cadastrar')
