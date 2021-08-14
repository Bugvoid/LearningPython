print("******************************")
print("Welcome to Game of adivinhacao!")
print("******************************")

num_secret = 42
total_tentativas = 3

for rodada in range(1, total_tentativas + 1):
    print("Tentativa: {} de {}".format(rodada, total_tentativas))
    chute = int(input("Digite o seu numero: "))
    print("Voce digitou ", chute)

    if(chute < 1 or chute > 100):
        print("Voce deve digitar um numero entre 1 e 100!")
        continue

    acertou = chute == num_secret
    isMaior = chute > num_secret
    isMenor = chute < num_secret

    if(acertou):
        print("Voce acertou!")
        break
    else:
        if(isMaior):
            print("Voce errou! O seu chute foi maior do que o numero secreto")
        elif(isMenor):
            print("Voce errou! O seu chute foi menor do que o numero secreto")


print("Fim Jogo")
