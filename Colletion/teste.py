# import array as arr
# # import numpy as np

# arr.array('d', [1, 3.5])
# print(arr)

# from Colletion.objetoProprio import ContaCorrente


# class ContaSalario:
#     def __init__(self, codigo, saldo):
#         self._codigo = codigo
#         self._saldo = saldo

#     def deposita(self, valor):
#         self._valor = valor

#     def __eq__(self, outro):
#         if type(outro) != ContaSalario:
#             return False
#         return self._codigo == outro

#     def __str__(self):
#         return f"[>>Codigo {self._codigo} Saldo {self._saldo}<<]"


# conta1 = ContaSalario(256, 1000)
# conta2 = ContaSalario(256, 1000)

# print(conta1 == conta2)
# print(isinstance(ContaCorrente))


# idades = [20, 55, 56, 78, 98, 45, 33]

# for i in range(len(idades)):
#     print(i, idades[i])

# enumerate(idades)

# list(range(len(idades)))

# list(enumerate(idades))


# for indice, valor in enumerate(idades):
#     print(indice," x ", valor)


# usuarios = [("Luan", 22, 1981), ("Luana", 23, 1988), ("Paulo", 39, 2000)]

# for nome,idade,nascimento in usuarios:
#     print(nome)

# idades = [20, 55, 56, 78, 98, 45, 33]
# sorted(idades)
# reversed(idades)
# sorted(idades, reverse=True)
# list(reversed(sorted(idades)))


# idades.sort()


from operator import attrgetter
from functools import total_ordering


@total_ordering
class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo = valor

    def __lt__(self, other):
        if self._saldo != other._saldo:
            return self._saldo < other._saldo
        return self._saldo < other._saldo

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False
        return self._codigo == outro._codigo and self._saldo == outro._saldo

    def __str__(self):
        return f"[>>Codigo {self._codigo} Saldo {self._saldo}<<]"


conta_ana = ContaSalario(10)
conta_ana.deposita(2000)
conta_Paulo = ContaSalario(11)
conta_Paulo.deposita(1000)
conta_Luan = ContaSalario(12)
conta_Luan.deposita(1000)

contas = [conta_ana, conta_Paulo, conta_Luan]


def extrai_saldo(conta):
    return conta._saldo


# for conta in sorted(contas, key=extrai_saldo):
#     print(conta)

for conta in sorted(contas, key=attrgetter("_saldo")):
    print(conta)

print(conta_ana < conta_Luan)


for conta in sorted(contas):
    print(conta)

print(conta_Luan == conta_Luan)
