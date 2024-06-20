# Função para exibir o menu principal
def exibir_menu_principal():
    while True:
        print("\nBem-vindo ao Sistema de Cadastro:")
        print("1. Cadastrar Cliente")
        print("2. Cadastrar Profissional")
        print("3. Listar Clientes")
        print("4. Listar Profissionais")
        print("5. Buscar Cliente")
        print("6. Buscar Profissional")
        print("7. Pesquisa Avançada de Profissionais")
        print("8. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_cliente()
        elif opcao == '2':
            cadastrar_profissional()
        elif opcao == '3':
            print("Opção selecionada: Listar Clientes")
            listar_clientes()
        elif opcao == '4':
            print("Opção selecionada: Listar Profissionais")
            listar_profissionais()
        elif opcao == '5':
            print("Opção selecionada: Buscar Cliente")
            buscar_cliente_por_nome()
        elif opcao == '6':
            print("Opção selecionada: Buscar Profissional")
            buscar_profissional()
        elif opcao == '7':
            print("Opção selecionada: Pesquisa Avançada de Profissionais")
            pesquisa_avancada_profissionais_por_categoria()
        elif opcao == '8':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
