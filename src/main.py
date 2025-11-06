def steak():

    while True:

        entrada = (
            input("Digite a temperatura da carne ou 'sair' para encerrar: ")
            .strip()
            .lower()
        )

        if entrada == "sair":
            print("Encerrando o programa...")
            break

        try:
            temperatura = int(entrada)
        except ValueError:

            print("Entrada inválida! Digite um numero inteiro ou 'sair' para encerrar.")
            continue

        if temperatura < 48:
            print(
                "A carne está quase pronta para ser consumida, cozinhe por mais alguns minutos."
            )
        elif 48 <= temperatura < 54:
            print("A carne está Selada (Rare) e quase pronta para ser consumida.")
        elif 54 <= temperatura < 60:
            print(
                "A carne está ao ponto para mal passada (Medim Rare) e pronta para ser consumida."
            )
        elif 60 <= temperatura < 65:
            print("A carne está ao ponto (Medium) e pronta para ser consumida.")
        elif 65 <= temperatura < 71:
            print(
                "A carne está ao ponto para bem passada (Medium well) e pronta para ser consumida."
            )
        elif temperatura > 71:
            print(
                "Cuidado, acima de 71 graus a carne pode queimar e ficará ruim para consumo."
            )


if __name__ == "__main__":

    steak()
