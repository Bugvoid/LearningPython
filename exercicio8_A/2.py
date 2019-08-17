i=0
resp = 2
maior = 0
soma = 0
while resp == 2:
    n = float(input("Digite um numero"))
    if(n>maior):
        maior = n
    soma = soma + n
    i= i + 1
    resp = int(input("Desejar encerrar?\n 1-Sim 2-Não"))
print("A media desses valores é ", (soma/i) ,"\nO Maior numero desses valores é ", maior)
