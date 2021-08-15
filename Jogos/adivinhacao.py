import random


def jogar():

    print("******************************")
    print("Welcome to Game of adivinhacao!")
    print("******************************")

    num_secret = round(random.randrange(1))
    total_tentativas = 0
    pontos = 1000

    print("Qual Nivel de dificuldade voce quer?")
    print("(1) Facil (2)Médio (3)Dificil")
    nivel = int(input("Define o nivel: "))

    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

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
            print("Voce acertou e fez {} pontos".format(pontos))
            break
        else:
            if(isMaior):
                print("Voce errou! O seu chute foi maior do que o numero secreto")
            elif(isMenor):
                print("Voce errou! O seu chute foi menor do que o numero secreto")
            pontos_fail = abs(num_secret - chute)
            pontos = pontos - pontos_fail

    print("Fim Jogo")


if(__name__ == "__main__"):
    jogar()
