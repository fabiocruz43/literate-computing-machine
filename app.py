import streamlit as st
from streamlit_wtf import st_form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

# Configuração básica do Streamlit
st.set_page_config(page_title="Aplicativo de Serviços", layout="wide")

# Serviços disponíveis
servicos = {
    'Técnicos': {
        'Eletricista': ['Instalação de fiação', 'Reparo de curto-circuito', 'Manutenção elétrica'],
        'Técnico em Informática': ['Reparo de computadores', 'Instalação de software', 'Configuração de rede'],
        'Técnico em Enfermagem': ['Cuidados de saúde', 'Administração de medicamentos', 'Acompanhamento hospitalar'],
        'Técnico em Segurança do Trabalho': ['Avaliação de riscos', 'Treinamento de segurança', 'Inspeção de EPI'],
        'Técnico em Edificações': [
            'Supervisão de obras', 'Leitura e interpretação de projetos', 'Execução de obras',
            'Orçamento de materiais', 'Desenho técnico', 'Planejamento de obras',
            'Acompanhamento de cronogramas', 'Controle de qualidade', 'Topografia',
            'Fiscalização de obras', 'Gestão de equipes', 'Análise de solos',
            'Manutenção predial', 'Regularização de imóveis', 'Projeto de fundações',
            'Elaboração de relatórios técnicos', 'Cálculo estrutural', 'Consultoria técnica'
        ],
        'Gesseiro': ['Aplicação de gesso', 'Reparos em gesso', 'Decoração em gesso'],
        'Pedreiro': ['Construção de paredes', 'Reboco', 'Assentamento de pisos e azulejos'],
        'Pintor': ['Pintura interna', 'Pintura externa', 'Pintura decorativa'],
        'Carpinteiro': ['Confecção de estruturas de madeira', 'Instalação de portas e janelas', 'Marcenaria'],
        'Marceneiro': ['Fabricação de móveis', 'Reparos em móveis', 'Instalação de móveis']
    },
    'Domésticos': {
        'Cozinheira': ['Preparação de refeições', 'Organização da cozinha', 'Compras de mercado'],
        'Passadeira': ['Passar roupas', 'Organização de guarda-roupa'],
        'Babá': ['Cuidado de crianças', 'Atividades educativas'],
        'Cuidador de Idosos': ['Acompanhamento', 'Administração de medicamentos'],
        'Diarista': ['Limpeza geral', 'Arrumação de casa'],
        'Faxineira': ['Limpeza pesada', 'Limpeza de janelas']
    }
}

# Classe para formulário de cliente
class ClienteForm:
    def __init__(self):
        self.nome = st.text_input("Nome")
        self.email = st.text_input("Email")
        self.telefone = st.text_input("Telefone")
        self.endereco = st.text_input("Endereço")
        self.submit_button = st.button("Cadastrar")

# Renderiza a página inicial
def renderiza_pagina_inicial():
    st.title("Página Inicial")
    st.write("Selecione uma opção no menu lateral para começar.")

# Renderiza a página de escolha de categoria
def renderiza_escolha_categoria():
    st.title("Escolha uma Categoria")
    categorias = ['Técnicos', 'Domésticos']
    categoria_escolhida = st.selectbox("Selecione uma categoria:", categorias)
    if st.button("Próximo"):
        st.session_state.categoria = categoria_escolhida
        st.session_state.pagina_atual = "Escolha de Profissão"

# Renderiza a página de escolha de profissão
def renderiza_escolha_profissao():
    st.title("Escolha uma Profissão")
    categoria = st.session_state.categoria
    if categoria == 'Técnicos':
        profissoes = list(servicos['Técnicos'].keys())
    elif categoria == 'Domésticos':
        profissoes = list(servicos['Domésticos'].keys())

    profissao_escolhida = st.selectbox("Selecione uma profissão:", profissoes)
    if st.button("Próximo"):
        st.session_state.profissao = profissao_escolhida
        st.session_state.pagina_atual = "Resumo"

# Renderiza a página de resumo
def renderiza_resumo():
    st.title("Resumo da Seleção")
    categoria = st.session_state.categoria
    profissao = st.session_state.profissao
    st.write(f"Categoria escolhida: {categoria}")
    st.write(f"Profissão escolhida: {profissao}")
    if st.button("Confirmar"):
        st.session_state.pagina_atual = "Página Final"

# Renderiza a página final
def renderiza_pagina_final():
    st.title("Página Final")
    st.write("Obrigado por usar nosso aplicativo!")

# Função principal para controlar a navegação entre páginas
def main():
    st.sidebar.title("Menu de Navegação")
    paginas = {
        "Página Inicial": renderiza_pagina_inicial,
        "Escolha de Categoria": renderiza_escolha_categoria,
        "Escolha de Profissão": renderiza_escolha_profissao,
        "Resumo": renderiza_resumo,
        "Página Final": renderiza_pagina_final
    }

    if 'pagina_atual' not in st.session_state:
        st.session_state.pagina_atual = "Página Inicial"

    pagina_atual = st.session_state.pagina_atual
    paginas[pagina_atual]()

    pagina_selecionada = st.sidebar.selectbox("Selecione uma página:", list(paginas.keys()))
    if pagina_selecionada != pagina_atual:
        st.session_state.pagina_atual = pagina_selecionada
        st.experimental_rerun()

# Executa o aplicativo
if __name__ == "__main__":
    main()
