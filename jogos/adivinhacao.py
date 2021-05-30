print("******************************")
print("Bem vindo ao Jogo da advinhação")
print("******************************")

numero_secreto = 30
contador = 3

while (contador > 0):
    print("Tentativas: ", contador)
    palpite_str = input("Digite o seu palpite: ")
    print("Você digitou ", palpite_str)
    palpite = int(palpite_str)

    acertou = palpite == numero_secreto
    maior   = palpite  > numero_secreto
    menor   = palpite  < numero_secreto

    if (acertou):
        print("*************")
        print("Você acertou!")
        print("*************")
        break
    else:
        if (maior):
            print("Seu palpite ultrapassou o numero secreto")
        elif (menor):
            print("Seu palpite foi menor do que o numero secreto")

    contador = contador -1
    if contador == 0:
        print("*****************************************************")
        print("Você excedeu o numero de tentativas, tente mais tarde")


