from frelance import cadastrar_profissional


class Cliente:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def __repr__(self):
        return f"Cliente(nome={self.nome}, email={self.email}, telefone={self.telefone})"


class SistemaCadastro:
    def __init__(self):
        self.clientes = []

    def cadastrar_cliente(self, nome, email, telefone):
        cliente = Cliente(nome, email, telefone)
        self.clientes.append(cliente)
        print(f"Cliente {nome} cadastrado com sucesso!")
        return cliente


# Instância do sistema de cadastro
sistema = SistemaCadastro()


# Função para interagir com o usuário e cadastrar cliente
def cadastrar_cliente():
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o email do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    sistema.cadastrar_cliente(nome, email, telefone)


# Chamada da função para cadastro de cliente
cadastrar_cliente()


# funcionalidade da listagem


class SistemaCadastro:
    def __init__(self):
        self.clientes = []

    def cadastrar_cliente(self, nome, email, telefone):
        cliente = Cliente(nome, email, telefone)
        self.clientes.append(cliente)
        print(f"Cliente {nome} cadastrado com sucesso!")
        return cliente

    def listar_clientes(self):
        if self.clientes:
            for cliente in self.clientes:
                print(cliente)
        else:
            print("Nenhum cliente cadastrado.")


# Instância do sistema de cadastro
sistema = SistemaCadastro()


# buscar cliente pelo nome e


class SistemaCadastro:
    def __init__(self):
        self.clientes = []

    def cadastrar_cliente(self, nome, email, telefone):
        cliente = Cliente(nome, email, telefone)
        self.clientes.append(cliente)
        print(f"Cliente {nome} cadastrado com sucesso!")
        return cliente

    def listar_clientes(self):
        if self.clientes:
            for cliente in self.clientes:
                print(cliente)
        else:
            print("Nenhum cliente cadastrado.")

    def buscar_cliente(self, termo_busca):
        resultados = [cliente for cliente in self.clientes if
                      termo_busca in (cliente.nome, cliente.email, cliente.telefone)]
        if resultados:
            for cliente in resultados:
                print(cliente)
        else:
            print(f"Nenhum cliente encontrado para o termo de busca: {termo_busca}")


# Instância do sistema de cadastro
sistema = SistemaCadastro()


# Função para interagir com o usuário e buscar cliente
def buscar_cliente():
    termo_busca = input("Digite o nome, email ou telefone do cliente que deseja buscar: ")
    sistema.buscar_cliente(termo_busca)


# Chamada das funções

cadastrar_cliente()
cadastrar_cliente()  # Você pode cadastrar mais clientes se necessário


def listar_clientes():
    cadastrar_cliente()
    cadastrar_cliente()  # Você pode cadastrar mais clientes se necessário
    listar_clientes()
    buscar_cliente()


# Função para interagir com o usuário e cadastrar cliente
def cadastrar_cliente():
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o email do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    sistema.cadastrar_cliente(nome, email, telefone)


# Função para listar clientes
def listar_clientes():
    print("Listando todos os clientes cadastrados:")
    sistema.listar_clientes()


# Chamada das funções
cadastrar_cliente()
listar_clientes()
