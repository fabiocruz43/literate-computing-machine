import streamlit as st
import mercadopago
import os
import sqlite3
from dotenv import load_dotenv
from database import criar_tabelas

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configuração inicial do Mercado Pago
SEU_ACCESS_TOKEN = os.getenv("MERCADO_PAGO_ACCESS_TOKEN")
if not SEU_ACCESS_TOKEN:
    st.error("O token de acesso do Mercado Pago não foi encontrado. Certifique-se de definir a variável de ambiente corretamente.")
else:
    mp = mercadopago.SDK(SEU_ACCESS_TOKEN)

# Criar tabelas do banco de dados
criar_tabelas()

# Dados fictícios para simular o funcionamento do sistema
categorias = ['Domésticos', 'Construção e Reformas', 'Técnicos']
profissoes = {
    'Domésticos': ['Cozinheira', 'Passadeira', 'Babá', 'Cuidador de Idosos', 'Diarista', 'Faxineira'],
    'Construção e Reformas': ['Pedreiro', 'Pintor', 'Carpinteiro', 'Marceneiro', 'Gesseiro'],
    'Técnicos': ['Eletricista', 'Técnico em Informática', 'Técnico em Enfermagem', 'Técnico em Segurança do Trabalho', 'Técnico em Edificações']
}

# Função para gerar link de pagamento
def gerar_link_pagamento(titulo, descricao, preco):
    preference_data = {
        "items": [
            {
                "title": titulo,
                "description": descricao,
                "quantity": 1,
                "currency_id": "BRL",
                "unit_price": preco
            }
        ]
    }
    preference_response = mp.preference().create(preference_data)
    preference = preference_response["response"]
    return preference['init_point']

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
        if not nome or not cpf or not endereco ou not identidade_file ou not comprovante_residencia_file ou not whatsapp:
            st.error("Por favor, preencha todos os campos obrigatórios.")
        else:
            identidade = identidade_file.read()
            comprovante_residencia = comprovante_residencia_file.read()

            conn = sqlite3.connect('neral_agencia_virtual.db')
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO clientes (nome, cpf, endereco, identidade, comprovante_residencia, whatsapp)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (nome, cpf, endereco, identidade, comprovante_residencia, whatsapp))
            conn.commit()
            conn.close()
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
        if not nome ou not cpf ou not endereco ou not identidade_file ou not comprovante_residencia_file ou not whatsapp:
            st.error("Por favor, preencha todos os campos obrigatórios.")
        else:
            identidade = identidade_file.read()
            comprovante_residencia = comprovante_residencia_file.read()
            servicos = ', '.join([profissao for profissao, oferecido in servicos_oferecidos.items() if oferecido])

            conn = sqlite3.connect('neral_agencia_virtual.db')
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO profissionais (nome, cpf, endereco, identidade, comprovante_residencia, whatsapp, servicos)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (nome, cpf, endereco, identidade, comprovante_residencia, whatsapp, servicos))
            conn.commit()
            conn.close()
            st.success('Cadastro de profissional realizado com sucesso!')

# Função para gerar pagamento
def realizar_pagamento():
    st.subheader('Realizar Pagamento')
    conn = sqlite3.connect('neral_agencia_virtual.db')
    cursor = conn.cursor()
    cursor.execute('SELECT nome, servicos FROM profissionais')
    profissionais = cursor.fetchall()
    conn.close()

    profissional_selecionado = st.selectbox('Selecione o profissional:', [f"{nome} - {servicos}" for nome, servicos in profissionais])
    preco = st.number_input('Insira o valor do pagamento:', min_value=0.0, step=0.01)

    if st.button('Gerar link de pagamento'):
        titulo, descricao = profissional_selecionado.split(' - ')
        link_pagamento = gerar_link_pagamento(titulo, descricao, preco)
        st.markdown(f"[Clique aqui para pagar]({link_pagamento})")

# Interface principal usando Streamlit
def main():
    st.title('Neral Agência Virtual')
    st.write('Seja bem-vindo!')
    st.write('Antes de usar nossos serviços, precisamos que realize seu cadastro logo abaixo.')

    opcao = st.radio('Você é:', ['Cliente: Cadastre-se', 'Profissional: Cadastre-se', 'Realizar Pagamento'])

    if opcao == 'Cliente: Cadastre-se':
        cadastrar_cliente()

    elif opcao == 'Profissional: Cadastre-se':
        cadastrar_profissional()

    elif opcao == 'Realizar Pagamento':
        realizar_pagamento()

if __name__ == '__main__':
    main()
