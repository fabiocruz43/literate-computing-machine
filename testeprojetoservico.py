from twilio.rest import Client

class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.servicos_contratados = []

    def escolher_pacote_servicos(self, pacote):
        self.servicos_contratados.append(pacote)

    def escolher_forma_pagamento(self, forma_pagamento):
        return forma_pagamento

    def pagar_com_cartao(self, dados_cartao):
        # Processar pagamento com dados do cartão
        return "Pagamento realizado com sucesso"

    def receber_alerta_nova_contratacao(self):
        # Enviar alerta por WhatsApp
        self.enviar_mensagem_whatsapp("Nova contratação realizada")

    def receber_notificacao_antecipada(self, mensagem):
        # Implementação para receber notificação antecipada
        print(mensagem)

    def confirmar_visualizacao_servicos(self):
        # Implementação para confirmar visualização dos serviços
        print("Visualização dos serviços confirmada")

    def enviar_mensagem_whatsapp(self, mensagem):
        # Implementação para enviar mensagem via WhatsApp
        account_sid = 'AC4b42764815b2eb776be03e26810c2d93'  # Substitua por seu account SID
        auth_token = '67269bbcc691806eaef2e6786eedcfe2'  # Substitua por seu auth token
        client = Client(account_sid, auth_token)

        try:
            message = client.messages.create(
                from_='whatsapp:+14155238886',
                body=mensagem,
                to='whatsapp:+5511948822408'  # Substitua pelo seu número de telefone
            )
            print("Mensagem enviada via WhatsApp:", mensagem)
        except Exception as e:
            print("Erro ao enviar mensagem via WhatsApp:", e)

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.servicos_agendados = []

    def confirmar_servicos(self, servicos):
        self.servicos_agendados.extend(servicos)

    def escolher_dias_manutencao(self, dias):
        return dias

    def receber_alerta_manutencao(self, mensagem):
        # Implementação para receber alerta de manutenção
        print(mensagem)

    def receber_alerta_renovacao_plano(self):
        # Implementação para receber alerta de renovação do plano
        print("Alerta de renovação do plano recebido")

    def renovar_plano(self):
        # Implementação para renovar o plano de serviços
        print("Plano renovado com sucesso")

class Sistema:
    def __init__(self):
        self.dados_privados = []

    def criptografar_dados_sensiveis(self, dados):
        # Implementação para criptografar dados sensíveis
        return "Dados criptografados"

    def gerar_relatorio(self, dados):
        # Implementação para gerar relatórios e estatísticas
        relatorio = "Relatório de Desempenho:\n"
        for dado in dados:
            relatorio += f"{dado}\n"
        return relatorio

# Função para testar todas as funcionalidades
def testar_funcionalidades():
    # Instanciando objetos
    empresa = Empresa("Minha Empresa")
    cliente = Cliente("Meu Cliente")
    sistema = Sistema()

    # Teste de escolha de pacote de serviços
    print("Teste: Escolher Pacote de Serviços")
    empresa.escolher_pacote_servicos("Pacote de Manutenção Premium")
    print("Pacote escolhido:", empresa.servicos_contratados)

    # Teste de escolha de forma de pagamento
    print("\nTeste: Escolher Forma de Pagamento")
    forma_pagamento = empresa.escolher_forma_pagamento("Cartão de Crédito")
    print("Forma de pagamento escolhida:", forma_pagamento)

    # Teste de pagamento com cartão
    print("\nTeste: Pagamento com Cartão")
    if forma_pagamento == "Cartão de Crédito":
        dados_cartao = {"numero": "1234 5678 9012 3456", "validade": "12/23", "cvv": "123"}
        mensagem_pagamento = empresa.pagar_com_cartao(dados_cartao)
        print(mensagem_pagamento)

    # Teste de alerta de nova contratação
    print("\nTeste: Alerta de Nova Contratação")
    empresa.receber_alerta_nova_contratacao()

    # Teste de notificação antecipada
    print("\nTeste: Notificação Antecipada")
    empresa.receber_notificacao_antecipada("Serviços agendados para amanhã.")

    # Teste de confirmação de visualização de serviços
    print("\nTeste: Confirmação de Visualização de Serviços")
    empresa.confirmar_visualizacao_servicos()

    # Teste de confirmação de serviços pelo cliente
    print("\nTeste: Confirmação de Serviços pelo Cliente")
    cliente.confirmar_servicos(["Limpeza", "Reparo Elétrico"])
    print("Serviços confirmados:", cliente.servicos_agendados)

    # Teste de escolha de dias de manutenção
    print("\nTeste: Escolha de Dias de Manutenção")
    dias_manutencao = cliente.escolher_dias_manutencao(["15/10/2024", "25/10/2024"])
    print("Dias escolhidos para manutenção:", dias_manutencao)

    # Teste de alerta de manutenção
    print("\nTeste: Alerta de Manutenção")
    mensagem_alerta_manutencao = f"Serviços agendados para os dias: {', '.join(dias_manutencao)}"
    cliente.receber_alerta_manutencao(mensagem_alerta_manutencao)

    # Teste de alerta de renovação de plano
    print("\nTeste: Alerta de Renovação de Plano")
    cliente.receber_alerta_renovacao_plano()

    # Teste de renovação de plano
    print("\nTeste: Renovação de Plano")
    cliente.renovar_plano()

    # Teste de criptografia de dados sensíveis
    print("\nTeste: Criptografia de Dados Sensíveis")
    dados_sensiveis = {"informacoes_pagamento": "1234 5678 9012 3456"}
    dados_criptografados = sistema.criptografar_dados_sensiveis(dados_sensiveis)
    print(dados_criptografados)

    # Teste de geração de relatório
    print("\nTeste: Geração de Relatório")
    relatorio = sistema.gerar_relatorio(["Desempenho excelente", "Aumento de clientes"])
    print(relatorio)

# Executar testes
testar_funcionalidades()
