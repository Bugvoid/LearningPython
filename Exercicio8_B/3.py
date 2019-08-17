pos=0
neg=0
soma=0
resp = 2
i=0
menor = 0
while resp== 2:
    n = float(input("Digite um numero"))
    
    if(n<0):
        neg+= 1
    else:
        pos+= 1
    if(n<menor):
        menor = n
    soma =soma + n
    i+= 1
    resp = int(input("Deseja encerrar?\n 1-Sim 2-Não"))
print("A Media desses valores é " ,(soma/i),"\nO menor numero desses valores é ",menor,"\nOs numeros positivos são: ",pos,"\nOs numeros negativos são: ",neg)
