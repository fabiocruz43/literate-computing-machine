import stripe


class GetNinjas:
    categorias_disponiveis = ("Eletricista", "Encanador", "Pintor", "Marceneiro", "Pedreiro")

    def _init_(self):
        print("Inicializando GetNinjas")
        self.profissionais = []
        print(f"Profissionais inicializados: {self.profissionais}")

    def cadastrar_profissional(self, nome, categorias, telefone):
        profissional = {
            'nome': nome,
            'categorias': categorias,
            'telefone': telefone
        }
        self.profissionais.append(profissional)
        print(f"Profissional {nome} cadastrado com sucesso!")
        print(f"Estado atual de profissionais: {self.profissionais}")

    def buscar_profissionais(self, categoria):
        resultados = [p for p in self.profissionais if categoria in p['categorias']]
        return resultados


# Instância de GetNinjas
print("Criando instância de GetNinjas")
getninjas = GetNinjas()
print(f"Estado inicial do objeto getninjas: {getninjas._dict_}")  # Verifique se 'profissionais' está inicializado


# Função para cadastrar um profissional
def cadastrar_profissional():
    try:
        nome = input("Digite o nome do profissional: ")
        print("Categorias disponíveis:")
        for index, categoria in enumerate(GetNinjas.categorias_disponiveis):
            print(f"{index + 1}. {categoria}")
        categorias = []
        while len(categorias) < 3:
            try:
                opcao = int(input("Digite o número da categoria: ")) - 1
                if opcao >= 0 and opcao < len(GetNinjas.categorias_disponiveis):
                    categoria = GetNinjas.categorias_disponiveis[opcao]
                    if categoria not in categorias:
                        categorias.append(categoria)
                    else:
                        print("Categoria já selecionada. Escolha outra categoria.")
                else:
                    print("Opção inválida. Digite novamente.")
            except ValueError:
                print("Por favor, digite um número válido.")
        telefone = input("Digite o telefone do profissional: ")
        print(f"Tentando cadastrar o profissional: Nome={nome}, Categorias={categorias}, Telefone={telefone}")
        getninjas.cadastrar_profissional(nome, categorias, telefone)
        print(f"Estado do objeto getninjas após cadastrar: {getninjas._dict_}")  # Verifique o estado após cadastrar
    except Exception as e:
        print(f"Ocorreu um erro ao cadastrar o profissional: {e}")


# Função para buscar profissionais por categoria
def buscar_profissionais():
    try:
        print("Categorias disponíveis:")
        for index, categoria in enumerate(GetNinjas.categorias_disponiveis):
            print(f"{index + 1}. {categoria}")
        try:
            opcao = int(input("Digite o número da categoria que deseja buscar: "))
            if opcao >= 1 and opcao <= len(GetNinjas.categorias_disponiveis):
                categoria = GetNinjas.categorias_disponiveis[opcao - 1]
                print(f"Buscando profissionais na categoria: {categoria}")
                resultados = getninjas.buscar_profissionais(categoria)
                print(f"Resultados da busca por {categoria}:")
                if resultados:
                    for index, profissional in enumerate(resultados):
                        print(
                            f"{index + 1}. Nome: {profissional['nome']}, Categoria: {', '.join(profissional['categorias'])}, Telefone: {profissional['telefone']}")
                else:
                    print("Nenhum profissional encontrado para esta categoria.")
            else:
                print("Opção inválida. Digite novamente.")
        except ValueError:
            print("Por favor, digite um número válido.")
    except Exception as e:
        print(f"Ocorreu um erro ao buscar profissionais: {e}")


# Teste as funções diretamente no terminal ou em um script Python.
# Aqui, adicionamos uma chamada de teste para cada função:

# Exemplo de uso de cadastrar_profissional
print("Vamos cadastrar um profissional.")
cadastrar_profissional()

# Exemplo de uso de buscar profissionais
print("\nVamos buscar profissionais.")
buscar_profissionais()
