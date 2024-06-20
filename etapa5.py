import json


class SistemaCadastro:
    def __init__(self):
        self.clientes = []

    def cadastrar_cliente(self, nome, email, telefone):
        cliente = Cliente(nome, email, telefone)
        self.clientes.append(cliente)
        print(f"Cliente {nome} cadastrado com sucesso!")
        self.salvar_dados()  # Salvando os dados após cada cadastro
        return cliente

    def salvar_dados(self):
        with open("clientes.json", "w") as arquivo:
            json.dump([cliente.__dict__ for cliente in self.clientes], arquivo)

    # Outros métodos da classe SistemaCadastro...


class GetNinjas:
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
        self.salvar_dados()  # Salvando os dados após cada cadastro

    def salvar_dados(self):
        with open("profissionais.json", "w") as arquivo:
            json.dump(self.profissionais, arquivo)

    # Outros métodos da classe GetNinjas...

# Restante do código...
