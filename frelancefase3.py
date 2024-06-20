class Cliente:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def __str__(self):
        return f"Nome: {self.nome}, Email: {self.email}, Telefone: {self.telefone}"


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

    def remover_cliente(self, termo_busca):
        cliente_a_remover = None
        for cliente in self.clientes:
            if termo_busca in (cliente.nome, cliente.email, cliente.telefone):
                cliente_a_remover = cliente
                break
        if cliente_a_remover:
            self.clientes.remove(cliente_a_remover)
            print(f"Cliente {cliente_a_remover.nome} removido com sucesso!")
        else:
            print(f"Nenhum cliente encontrado para o termo de busca: {termo_busca}")


class GetNinjas:
    categorias_disponiveis = ["Eletricista", "Encanador", "Pintor", "Marceneiro", "Pedreiro"]

    def __init__(self):
        self.profissionais = []

    def cadastrar_profissional(self, nome, categorias, telefone):
        profissional = {
            'nome': nome,
            'categorias': categorias,
            'telefone': telefone
        }
        self.profissionais.append(profissional)
        print(f"Profissional {nome} cadastrado com sucesso!")

    def listar_profissionais(self):
        if self.profissionais:
            for profissional in self.profissionais:
                print(profissional)
        else:
            print("Nenhum profissional cadastrado.")

    def buscar_profissional(self, termo_busca):
        resultados = [
            profissional for profissional in self.profissionais
            if termo_busca in profissional['nome'] or termo_busca in profissional['categorias']
        ]
        if resultados:
            for profissional in resultados:
                print(profissional)
        else:
            print(f"Nenhum profissional encontrado para o termo de busca: {termo_busca}")

    def remover_profissional(self, termo_busca):
        profissional_a_remover = None
        for profissional in self.profissionais:
            if termo_busca in (profissional['nome'], *profissional['categorias']):
                profissional_a_remover = profissional
                break
        if profissional_a_remover:
            self.profissionais.remove(profissional_a_remover)
            print(f"Profissional {profissional_a_remover['nome']} removido com sucesso!")
        else:
            print(f"Nenhum profissional encontrado para o termo de busca: {termo_busca}")


# Instância do sistema de cadastro
sistema = SistemaCadastro()

# Instância de GetNinjas
getninjas = GetNinjas()


# Funções para interagir com o usuário

def cadastrar_cliente():
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o email do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    sistema.cadastrar_cliente(nome, email, telefone)


def listar_clientes():
    print("Listando todos os clientes cadastrados:")
    sistema.listar_clientes()


def buscar_cliente():
    termo_busca = input("Digite o nome, email ou telefone do cliente que deseja buscar: ")
    sistema.buscar_cliente(termo_busca)


def remover_cliente():
    termo_busca = input("Digite o nome, email ou telefone do cliente que deseja remover: ")
    sistema.remover_cliente(termo_busca)


def cadastrar_profissional():
    nome = input("Digite o nome do profissional: ")
    print("Categorias disponíveis:")
    for index, categoria in enumerate(GetNinjas.categorias_disponiveis):
        print(f"{index + 1}. {categoria}")
    categorias = []
    while len(categorias) < 3:
        opcao = int(input("Digite o número da categoria: ")) - 1
        if opcao >= 0 and opcao < len(GetNinjas.categorias_disponiveis):
            categoria = GetNinjas.categorias_disponiveis[opcao]
            if categoria not in categorias:
                categorias.append(categoria)
            else:
                print("Categoria já selecionada. Escolha outra categoria.")
        else:
            print("Opção inválida. Digite novamente.")
    telefone = input("Digite o telefone do profissional: ")
    getninjas.cadastrar_profissional(nome, categorias, telefone)


def listar_profissionais():
    print("Listando todos os profissionais cadastrados:")
    getninjas.listar_profissionais()


def buscar_profissional():
    termo_busca = input("Digite o nome ou categoria do profissional que deseja buscar: ")
    getninjas.buscar_profissional(termo_busca)


def remover_profissional():
    termo_busca = input("Digite o nome ou categoria do profissional que deseja remover: ")
    getninjas.remover_profissional(termo_busca)


# Chamada das funções
cadastrar_cliente()
cadastrar_cliente()  # Você pode cadastrar mais clientes se necessário
listar_clientes()
buscar_cliente()
remover_cliente()

cadastrar_profissional()
listar_profissionais()
buscar_profissional()
remover_profissional()
