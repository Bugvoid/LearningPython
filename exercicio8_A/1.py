number = int(input("Digite a quantidade de valores"))
soma = 0.0
for i in range(number):
    n=float(input("Digite o numero"))
    soma = soma + n
    
print("A media desses valores é",(soma/number))

