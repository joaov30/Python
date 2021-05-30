print("*********************************")
print("Bem vindo no jogo de adivinhação!")
print("*********************************")

numero_secreto = 50

chute_str = input("Digite o seu numero: ")

print("Você digitou ", chute_str)

chute = int(chute_str)

if(numero_secreto == chute):
    print("Você acertou!")
else:
    if(chute > numero_secreto):
        print("Você errou! O seu chute foi maior do que o número secreto.")
    if(chute < numero_secreto):
        print("Você errou! O seu chute foi menor do que o número secreto.")

print("Game over")