def main():
    while True:
        entrada = input("Digite algo: ")
        if entrada.lower() == 'sair':
            break
        print(f"Você digitou: {entrada}")


if __name__ == "__main__":
    main()
