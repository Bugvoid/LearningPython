valor = float(input("Digite o valor a ser depositado"))
ti = int(input("Digite o tipo de investimento:\n 1 - poupança \n 2 - fundos renda fixa"))

if ti == 1:
    print("O valor corrigido: ", valor + ((valor*3)/100))
elif ti == 2:
    print("O valor corrigido: ", valor + ((valor*4)/100))
else:
    print("O tipo de investimento não existe")
    
