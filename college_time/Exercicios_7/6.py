sex = input("Digite o seu sexo ")
idade = int(input("Digite a sua idade "))

if sex == 'f' or sex == 'F':
    if idade == 12:
        print("O preço da diaria: 21,50")
    elif idade > 12 or idade <=55:
        print("O preço da diaria: 53,99")
    elif idade > 55:
        print("O preço da diaria: 40,00")
elif sex == 'm' or sex == 'M':
    if idade == 12:
        print("O preço da diaria: 19,50")
    elif idade > 12 or idade <=55:
        print("O preço da diaria: 60,30")
    elif idade > 55:
        print("O preço da diaria: 45,50")
else:
    print("Sexo invalido")
