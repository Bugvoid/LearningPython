print("******************************")
print("Welcome to Game of adivinhacao!")
print("******************************")

num_secret = 42

chute =  int(input("Digite o seu numero: "))

print("Voce digitou ", chute)
print(type(chute))
print(type(num_secret))


if(num_secret == chute):
    print("Voce acertou!")
else:
    print("Voce errou!")

print("Fim Jogo")