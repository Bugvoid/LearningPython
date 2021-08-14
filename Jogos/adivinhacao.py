print("******************************")
print("Welcome to Game of adivinhacao!")
print("******************************")

num_secret = 42

chute = int(input("Digite o seu numero: "))

print("Voce digitou ", chute)

acertou = chute == num_secret
isMaior = chute > num_secret
isMenor = chute < num_secret
if(acertou):
    print("Voce acertou!")
else:
    if(isMaior):
        print("Voce errou! O seu chute foi maior do que o numero secreto")
    elif(isMenor):
        print("Voce errou! O seu chute foi menor do que o numero secreto")


print("Fim Jogo")