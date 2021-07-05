n= int(input("Digite a quantidade de pessoas no grupo"))
mediam = 0
mediah = 0
x= 0
y= 0
for i in range(n):
    altura = float(input("Digite a estatura da pessoa"))
    sexo = input("Digite o sexo da pessoa ")
    if(sexo == 'F' or sexo == 'f'):
        mediam += altura
        x+= 1
    else:
        mediah += altura
        y+= 1
print("A estatura media das mulheres:",(mediam/x),
      "A estatura media dos homens:",(mediah /y))
