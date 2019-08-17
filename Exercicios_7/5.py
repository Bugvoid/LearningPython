alt = float(input("Digite a sua altura"))
sex = input("Digite o seu sexo")

if sex == 'm' or sex == 'M':
    print("O seu peso ideal: ", (72.7*alt)-58)
elif sex == 'f' or sex == 'M':
    print("O seu peso ideal: ", (62.1*alt)-44.7)
else:
    print("Sexo invalido")
