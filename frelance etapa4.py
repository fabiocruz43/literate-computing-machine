import json


class Cliente:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def to_dict(self):
        return {
            'nome': self.nome,
            'email': self.email,
            'telefone': self.telefone
        }


class SistemaCadastro:
    def __init__(self):
        self.clientes = []
        self.carregar_dados()

    def cadastrar_cliente(self, nome, email, telefone):
        cliente = Cliente(nome, email, telefone)
        self.clientes.append(cliente)
        print(f"Cliente {nome} cadastrado com sucesso!")
        self.salvar_dados()  # Salvando os dados após cada cadastro
        return cliente

    def salvar_dados(self):
        try:
            with open("clientes.json", "w") as arquivo:
                json.dump([cliente.to_dict() for cliente in self.clientes], arquivo, indent=4)
        except Exception as e:
            print("Erro ao salvar dados dos clientes:", e)

    def carregar_dados(self):
        try:
            with open("clientes.json", "r") as arquivo:
                dados = json.load(arquivo)
                self.clientes = [Cliente(**cliente) for cliente in dados]
        except Exception as e:
            print("Erro ao carregar dados dos clientes:", e)

    # Outros métodos da classe SistemaCadastro...


class GetNinjas:
    def __init__(self):
        self.profissionais = []
        self.carregar_dados()

    def cadastrar_profissional(self, nome, categorias, telefone):
        profissional = {
            'nome': nome,
            'categorias': categorias,
            'telefone': telefone
        }
        self.profissionais.append(profissional)
        print(f"Profissional {nome} cadastrado com sucesso!")
        self.salvar_dados()  # Salvando os dados após cada cadastro

    def salvar_dados(self):
        try:
            with open("profissionais.json", "w") as arquivo:
                json.dump(self.profissionais, arquivo, indent=4)
        except Exception as e:
            print("Erro ao salvar dados dos profissionais:", e)

    def carregar_dados(self):
        try:
            with open("profissionais.json", "r") as arquivo:
                self.profissionais = json.load(arquivo)
        except Exception as e:
            print("Erro ao carregar dados dos profissionais:", e)

    # Outros métodos da classe GetNinjas...


# Restante do código...

# Testando o SistemaCadastro
sistema = SistemaCadastro()
sistema.cadastrar_cliente("João", "joao@email.com", "123456789")
