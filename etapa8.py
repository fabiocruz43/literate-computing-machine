class Profissional:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
        self.servicos = []

    def adicionar_servico(self, servico):
        self.servicos.append(servico)

    def listar_servicos(self):
        if self.servicos:
            for idx, servico in enumerate(self.servicos, start=1):
                print(f"Serviço {idx}:")
                print(servico)
        else:
            print("Este profissional não oferece nenhum serviço ainda.")

    def buscar_servico(self, nome_servico):
        for servico in self.servicos:
            if servico.nome == nome_servico:
                return servico
        return None
