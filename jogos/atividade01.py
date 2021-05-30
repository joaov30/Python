print("Jogo da advinhação")
print("******************")

numero_secreto = 30

palpite_str = input("Digite o seu palpite: ")

palpite = int(palpite_str)

maior = palpite > numero_secreto

menor = palpite < numero_secreto

if palpite == numero_secreto:
    print("Você acertou!")
elif maior:
    print("Seu palpite ultrapassou o numero secreto")
elif menor:
    print("Seu palpite foi menor do que o numero secreto")

print("Game Over")