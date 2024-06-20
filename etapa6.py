categorias_disponiveis = ["Eletricista", "Encanador", "Pintor", "Marceneiro", "Pedreiro"]
clientes = []
profissionais = []


def exibir_categorias_disponiveis():
    print("Categorias Disponíveis:")
    for index, categoria in enumerate(categorias_disponiveis, start=1):
        print(f"{index}. {categoria}")


def cadastrar_profissional():
    print("\nCadastro de Profissional:")
    exibir_categorias_disponiveis()

    categorias = input("Digite o número da categoria (ou números separados por vírgula): ").split(',')
    categorias_escolhidas = []
    for numero in categorias:
        try:
            indice = int(numero) - 1
            if 0 <= indice < len(categorias_disponiveis):
                categorias_escolhidas.append(categorias_disponiveis[indice])
            else:
                print(f"Opção {numero} inválida.")
        except ValueError:
            print(f"Opção {numero} inválida.")

    if categorias_escolhidas:
        nome = input("Digite o nome do profissional: ")
        telefone = input("Digite o telefone do profissional: ")
        profissionais.append({"nome": nome, "categorias": categorias_escolhidas, "telefone": telefone})
        print(f"Profissional {nome} cadastrado com sucesso!")
    else:
        print("Nenhuma categoria válida selecionada.")


def cadastrar_cliente():
    print("\nCadastro de Cliente:")
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o email do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    clientes.append({"nome": nome, "email": email, "telefone": telefone})
    print(f"Cliente {nome} cadastrado com sucesso!")


def listar_profissionais():
    print("\nLista de Profissionais:")
    for profissional in profissionais:
        print(f"Nome: {profissional['nome']}")
        print(f"Telefones: {profissional['telefone']}")
        print(f"Categorias: {', '.join(profissional['categorias'])}")
        print()


def listar_clientes():
    print("\nLista de Clientes:")
    for cliente in clientes:
        print(f"Nome: {cliente['nome']}")
        print(f"Email: {cliente['email']}")
        print(f"Telefone: {cliente['telefone']}")
        print()


def buscar_cliente():
    nome_cliente = input("Digite o nome do cliente a ser buscado: ")
    for cliente in clientes:
        if cliente['nome'] == nome_cliente:
            print("\nCliente encontrado:")
            print(f"Nome: {cliente['nome']}")
            print(f"Email: {cliente['email']}")
            print(f"Telefone: {cliente['telefone']}")
            return
    print(f"Cliente com o nome '{nome_cliente}' não encontrado.")


def buscar_profissional():
    nome_profissional = input("Digite o nome do profissional a ser buscado: ")
    for profissional in profissionais:
        if profissional['nome'] == nome_profissional:
            print("\nProfissional encontrado:")
            print(f"Nome: {profissional['nome']}")
            print(f"Telefones: {profissional['telefone']}")
            print(f"Categorias: {', '.join(profissional['categorias'])}")
            return
    print(f"Profissional com o nome '{nome_profissional}' não encontrado.")


def exibir_menu_principal():
    print("Bem-vindo ao Sistema de Cadastro:")
    print("1. Cadastrar Cliente")
    print("2. Cadastrar Profissional")
    print("3. Listar Clientes")
    print("4. Listar Profissionais")
    print("5. Buscar Cliente")
    print("6. Buscar Profissional")
    print("7. Sair")


def main():
    while True:
        exibir_menu_principal()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_cliente()
        elif opcao == '2':
            cadastrar_profissional()
        elif opcao == '3':
            listar_clientes()
        elif opcao == '4':
            listar_profissionais()
        elif opcao == '5':
            buscar_cliente()
        elif opcao == '6':
            buscar_profissional()
        elif opcao == '7':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()
