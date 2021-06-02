import random

print("******************************")
print("Bem vindo ao Jogo da advinhação")
print("******************************")

numero_secreto = random.randrange(1, 101)
contador = 3

print(numero_secreto)


for rodada in range(1, contador + 1):
    print("Tentativa {} de {}".format( rodada, contador))
    palpite_str = input("Digite o seu palpite entre 1 e 100: ")
    print("Você digitou ", palpite_str)
    palpite = int(palpite_str)

    if(palpite < 1 or palpite > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue

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




