import sqlite3


# Função para criar a tabela de clientes
def criar_tabela_clientes():
    # Conectar ao banco de dados
    conn = sqlite3.connect('cadastro.db')
    cursor = conn.cursor()

    # Criar a tabela de clientes
    cursor.execute('''CREATE TABLE IF NOT EXISTS clientes
                      (id INTEGER PRIMARY KEY,
                       nome TEXT NOT NULL,
                       email TEXT NOT NULL,
                       telefone TEXT NOT NULL)''')

    # Confirmar a transação
    conn.commit()

    # Fechar a conexão
    conn.close()


# Função para cadastrar um novo cliente no banco de dados
def cadastrar_cliente():
    # Capturar os detalhes do cliente
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o email do cliente: ")
    telefone = input("Digite o telefone do cliente: ")

    # Conectar ao banco de dados
    conn = sqlite3.connect('cadastro.db')
    cursor = conn.cursor()

    # Inserir os dados do cliente na tabela de clientes
    cursor.execute("INSERT INTO clientes (nome, email, telefone) VALUES (?, ?, ?)", (nome, email, telefone))

    # Confirmar a transação
    conn.commit()

    # Fechar a conexão
    conn.close()

    print("Cliente", nome, "cadastrado com sucesso!")


# Função para exibir o menu principal
def exibir_menu_principal():
    print("Bem-vindo ao Sistema de Cadastro:")
    print("1. Cadastrar Cliente")
    print("2. Cadastrar Profissional")
    print("3. Listar Clientes")
    print("4. Listar Profissionais")
    print("5. Buscar Cliente")
    print("6. Buscar Profissional")
    print("7. Pesquisa Avançada de Profissionais")
    print("8. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        cadastrar_cliente()  # Chamar a função para cadastrar cliente
    elif opcao == '2':
        print("Opção selecionada: Cadastrar Profissional")
        # Chamar a função para cadastrar profissional
    elif opcao == '3':
        print("Opção selecionada: Listar Clientes")
        # Chamar a função para listar clientes
    elif opcao == '4':
        print("Opção selecionada: Listar Profissionais")
        # Chamar a função para listar profissionais
    elif opcao == '5':
        print("Opção selecionada: Buscar Cliente")
        # Chamar a função para buscar cliente
    elif opcao == '6':
        print("Opção selecionada: Buscar Profissional")
        # Chamar a função para buscar profissional
    elif opcao == '7':
        pesquisar_profissionais_avancado()
    elif opcao == '8':
        print("Saindo do sistema. Até logo!")
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")


# Chamada para criar a tabela de clientes
criar_tabela_clientes()

# Chamada para exibir o menu principal
exibir_menu_principal()


# Função para cadastrar um novo profissional no banco de dados
def cadastrar_profissional():
    # Capturar os detalhes do profissional
    categorias_disponiveis = ["Eletricista", "Encanador", "Pintor", "Marceneiro", "Pedreiro"]
    print("Categorias Disponíveis:")
    for i, categoria in enumerate(categorias_disponiveis, 1):
        print(f"{i}. {categoria}")
    categorias_input = input("Digite o número da categoria (ou números separados por vírgula): ")
    categorias_indices = [int(idx) - 1 for idx in categorias_input.split(',')]
    categorias_escolhidas = [categorias_disponiveis[idx] for idx in categorias_indices]
    nome = input("Digite o nome do profissional: ")
    telefone = input("Digite o telefone do profissional: ")

    # Conectar ao banco de dados
    conn = sqlite3.connect('cadastro.db')
    cursor = conn.cursor()

    # Inserir os dados do profissional na tabela de profissionais
    cursor.execute("INSERT INTO profissionais (nome, telefone, categorias) VALUES (?, ?, ?)",
                   (nome, telefone, ', '.join(categorias_escolhidas)))

    # Confirmar a transação
    conn.commit()

    # Fechar a conexão
    conn.close()

    print("Profissional", nome, "cadastrado com sucesso!")
