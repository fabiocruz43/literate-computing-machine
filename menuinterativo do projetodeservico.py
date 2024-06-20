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
        # Simula o processamento do pagamento com os dados do cartão
        return "Pagamento realizado com sucesso"

    def receber_alerta_nova_contratacao(self):
        # Envia alerta por WhatsApp
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


def menu():
    print("\nMenu de Opções:")
    print("1. Inscrever Empresa")
    print("2. Inscrever Cliente")
    print("3. Escolher Pacote de Serviços")
    print("4. Escolher Forma de Pagamento")
    print("5. Pagar com Cartão")
    print("6. Receber Alerta de Nova Contratação")
    print("7. Receber Notificação Antecipada")
    print("8. Confirmar Visualização dos Serviços")
    print("9. Confirmar Serviços pelo Cliente")
    print("10. Escolher Dias de Manutenção")
    print("11. Receber Alerta de Manutenção")
    print("12. Receber Alerta de Renovação de Plano")
    print("13. Renovar Plano")
    print("14. Criptografar Dados Sensíveis")
    print("15. Gerar Relatório")
    print("16. Sair")


def main():
    empresa = None
    cliente = None
    sistema = Sistema()

    while True:
        menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome_empresa = input("Nome da Empresa: ")
            empresa = Empresa(nome_empresa)
            print(f"Empresa {nome_empresa} inscrita com sucesso.")

        elif escolha == '2':
            nome_cliente = input("Nome do Cliente: ")
            cliente = Cliente(nome_cliente)
            print(f"Cliente {nome_cliente} inscrito com sucesso.")

        elif escolha == '3' and empresa:
            pacote = input("Nome do Pacote de Serviços: ")
            empresa.escolher_pacote_servicos(pacote)
            print(f"Pacote {pacote} escolhido com sucesso.")

        elif escolha == '4' and empresa:
            forma_pagamento = input("Forma de Pagamento (Ex: Cartão de Crédito): ")
            forma_escolhida = empresa.escolher_forma_pagamento(forma_pagamento)
            print(f"Forma de pagamento escolhida: {forma_escolhida}")

        elif escolha == '5' and empresa:
            dados_cartao = {
                "numero": input("Número do Cartão: "),
                "validade": input("Validade (MM/AA): "),
                "cvv": input("CVV: ")
            }
            mensagem_pagamento = empresa.pagar_com_cartao(dados_cartao)
            print(mensagem_pagamento)

        elif escolha == '6' and empresa:
            empresa.receber_alerta_nova_contratacao()

        elif escolha == '7' and empresa:
            mensagem = input("Mensagem de Notificação Antecipada: ")
            empresa.receber_notificacao_antecipada(mensagem)

        elif escolha == '8' and empresa:
            empresa.confirmar_visualizacao_servicos()

        elif escolha == '9' and cliente:
            servicos = input("Serviços a Confirmar (separados por vírgula): ").split(", ")
            cliente.confirmar_servicos(servicos)
            print(f"Serviços confirmados: {cliente.servicos_agendados}")

        elif escolha == '10' and cliente:
            dias = input("Dias de Manutenção (separados por vírgula): ").split(", ")
            dias_escolhidos = cliente.escolher_dias_manutencao(dias)
            print(f"Dias escolhidos para manutenção: {dias_escolhidos}")

        elif escolha == '11' and cliente:
            mensagem = input("Mensagem de Alerta de Manutenção: ")
            cliente.receber_alerta_manutencao(mensagem)

        elif escolha == '12' and cliente:
            cliente.receber_alerta_renovacao_plano()

        elif escolha == '13' and cliente:
            cliente.renovar_plano()

        elif escolha == '14':
            dados = input("Dados Sensíveis a Criptografar (Ex: {\"chave\": \"valor\"}): ")
            dados_criptografados = sistema.criptografar_dados_sensiveis(eval(dados))
            print(dados_criptografados)

        elif escolha == '15':
            dados = input("Dados para Relatório (separados por vírgula): ").split(", ")
            relatorio = sistema.gerar_relatorio(dados)
            print(relatorio)

        elif escolha == '16':
            print("Saindo...")
            break

        else:
            print("Opção inválida ou operação não permitida sem inscrição prévia.")


if __name__ == "__main__":
    main()
