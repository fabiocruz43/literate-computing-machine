# empresa.py

class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.servicos_escolhidos = []

    def escolher_servico(self, categoria, servico):
        self.servicos_escolhidos.append(f"{categoria}: {servico}")

    def get_servicos_escolhidos(self):
        return self.servicos_escolhidos
