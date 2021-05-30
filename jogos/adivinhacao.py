print("******************************")
print("Bem vindo aoJogo da advinhação")
print("******************************")

numero_secreto = 30
contador = 3

while (contador > 0):
    print("Tentativa: ", contador)
    palpite_str = input("Digite o seu palpite: ")
    print("Você digitou ", palpite_str)
    palpite = int(palpite_str)

    acertou = palpite == numero_secreto
    maior   = palpite  > numero_secreto
    menor   = palpite  < numero_secreto

    if (acertou):
        print("Você acertou")
    else:
        if (maior):
            print("Seu palpite ultrapassou o numero secreto")
        elif (menor):
            print("Seu palpite foi menor do que o numero secreto")

    contador = contador -1


