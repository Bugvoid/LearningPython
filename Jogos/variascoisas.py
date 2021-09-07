# from datas import Data
# print("Ola", "QUE", sep="/", end="\n+")


class Pessoa:
    tamanho_cpf = 11

    def __init__(self, cpf, nome):
        self.cpf = cpf
        self.nome = nome

    def valida_cpf(self):
        return True if len(self.cpf) == __class__.tamanho_cpf else False

pe = Pessoa('00000000001', 'Ruby')
print(pe.valida_cpf())

pe = Pessoa('0000000000', 'Cristal')
print(pe.valida_cpf())

class Pessoa:
    tamanho_cpf = 11

p = Pessoa()

print(p.tamanho_cpf)

p.tamanho_cpf = 12

print(p.tamanho_cpf)

print(Pessoa.tamanho_cpf)

numero = 123
titular = "Luan"
saldo = 155.00
limite = 1500.0

conta = {"numero": numero, "titular": titular,
         "saldo": saldo, "limite": limite}
conta["titular"]


# arquivo = open("nome_do_arquivo.txt", "m")
# arquivo.close()
# arquivo = open("nome_do_arquivo.txt", "a")
# arquivo.readline()

# for linha in arquivo:
#     print(linha)
# arquivo.close()
# palavra = "teste"
# palavra2 = palavra.capitalize().strip().lower()
# palavra.endswith("te")  # true
# palavra.strip()
# listaT = [1, 5, 8, 9, 6, "teste"]
# listaT.append(8)
# len(listaT)
# dias = ("S", "T", "Q", "Q", "S", "S", "D",)  # tuple

# p1 = (3, 5)
# p2 = (110, 8)
# p3 = (58, 9)

# line = [p1, p2, p3]
# line[0][0][0]

# lista = ["_" for letra in palavra]

# precos = [1525, 1120, 1464, 1200, 1330, 1356, 1312, 1531, 1232, 1234, 1250, 1114, 1553, 1147, 1303, 1296, 1309, 1404, 1479, 1376, 1152, 1440, 1038, 1018,
#           1291, 1388, 1577, 1115, 1488, 1494, 1254, 1230, 1122, 1396, 1208, 1356, 1549, 1116, 1443, 1075, 1536, 1542, 1036, 1015, 1020, 1217, 1484, 1032, 1390, 1026]
# print(min(precos))
# print(max(precos))
# num1 = 21
# num2 = 32

# num3 = abs(num1 - num2) / 3

# print(round(num3))
# print(3//2)

# nome = 'Luan'
# print(f'Meu nome é {nome.lower()}')
# print(f'Meu nome é {nome.upper()}')


# print("R$ {:6.1f}".format(1000.12))
# print("R$ {:07.2f}".format(4.11))

# print("R$ {:.2f}".format(1.59))
# print("R$ {:.2f}".format(50.59))
# print("R$ {:7.2f}".format(1243.59))
# print("R$ {:07.2f}".format(25.59))
# print("R$ {:7d}".format(25))
# print("Data {:02d}/{:02d}".format(5,11))
# print("Data {:02d}/{:02d}/{:02d}".format(19,11,1998))

# for rodada in range(1, 10):
#     print(rodada)


# for rodada in range(1, 10, 2):
#     print(rodada)

# dia_ini = 24
# dia_fim = 28
# mes = "fevereiro"
# ano = 2017


# print("Em {} o Carnaval acontece em {} do dia {} até o dia {}".format(
#     ano, mes, dia_ini, dia_fim))


# usuario = input("Informe o usuário do sistema!")

# if(usuario == "Flávio"):
#     print("Seja bem-vindo Flávio!")
# elif(usuario == "Douglas"):
#     print("Seja bem-vindo Douglas!")
# elif(usuario == "Nico"):
#     print("Seja bem-vindo Nico")
# else:
#     print("Usuário não identificado!")
