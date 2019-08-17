valor = float(input("Digite o valor do produto"))
n = int(input("Digite a condição de pagamento: \n 1 - A vista ou cheque \n",
              "2 - A vista no cartão de crédito \n",
              "3 - Em 2 vezes no crédito \n 4 -Em 3 vezes no crédito"))

if  n == 1 :
    print("O valor a ser pago: ",valor - ((valor*10)/100))
elif n == 2:
    print("O valor a ser pago: ",valor - ((valor*5)/100))
elif n == 3:
    print("O valor a ser pago: ",valor)
elif n == 4:
    print("O valor a ser pago: ",valor + ((valor*10)/100))
else:
    print("Condição de pagamento inválida")
