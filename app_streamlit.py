import streamlit as st
import mercadopago
import os

# Configuração inicial do Mercado Pago
SEU_ACCESS_TOKEN = os.getenv("MERCADO_PAGO_ACCESS_TOKEN")
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

# Função para a seleção de serviços pelo cliente
def selecionar_servicos():
    st.subheader('Selecione os serviços desejados')
    categoria_selecionada = st.selectbox('Selecione a categoria:', categorias, key='cliente_categoria')

    if categoria_selecionada:
        profissoes_categoria = profissoes.get(categoria_selecionada, [])
        profissao_selecionada = st.selectbox('Selecione a profissão:', profissoes_categoria, key='cliente_profissao')

        if profissao_selecionada:
            preco_servico = 100.0  # Preço pré-definido para simplificação
            st.write(f'Preço do serviço selecionado: R$ {preco_servico:.2f}')
            if st.button('Confirmar contratação'):
                preference_data = {
                    "items": [
                        {
                            "title": f"Serviço de {profissao_selecionada}",
                            "quantity": 1,
                            "currency_id": "BRL",
                            "unit_price": float(preco_servico)
                        }
                    ]
                }

                try:
                    preference_response = mp.preference().create(preference_data)
                    if 'init_point' in preference_response['response']:
                        payment_url = preference_response['response']['init_point']
                        st.markdown(f"### Realize o pagamento [aqui]({payment_url})")
                        st.success("Pagamento confirmado! Agora podemos prosseguir com as etapas seguintes.")
                    else:
                        st.error("Erro ao processar pagamento: resposta inválida do Mercado Pago")
                except Exception as e:
                    st.error(f"Erro ao processar pagamento: {str(e)}")

# Interface principal usando Streamlit
def main():
    st.title('Neral Agência Virtual')
    st.write('Seja bem-vindo!')

    # Autenticação simples (a ser substituída por um sistema de autenticação real)
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        usuario = st.text_input('Usuário')
        senha = st.text_input('Senha', type='password')
        if st.button('Login'):
            if usuario == 'admin' and senha == 'password':  # Substituir por validação real
                st.session_state.authenticated = True
                st.success('Login realizado com sucesso!')
            else:
                st.error('Usuário ou senha incorretos')
        return

    st.write('Antes de usar nossos serviços, precisamos que realize seu cadastro logo abaixo.')
    opcao = st.radio('Você é:', ['Cliente: Cadastre-se', 'Profissional: Cadastre-se'])

    if opcao == 'Cliente: Cadastre-se':
        cadastrar_cliente()
        if st.button('Continuar para escolha de serviços'):
            selecionar_servicos()
    elif opcao == 'Profissional: Cadastre-se':
        cadastrar_profissional()

if __name__ == '__main__':
    main()
