# class ContaCorrente:
#     def __init__(self, codigo):
#         self.codigo = codigo
#         self.saldo = 0

#     def deposita(self, valor):
#         self.saldo += valor

#     def __str__(self):
#         return f"[>>Codigo: {self.codigo} Saldo: {self.saldo}<<]"


# conta_luan = ContaCorrente(15)
# conta_luan.deposita(500)
# print(conta_luan)


# conta_ana = ContaCorrente(17689)
# conta_ana.deposita(1000)
# print(conta_ana)

# contas = [conta_luan, conta_ana]
# print(contas)

# for conta in contas:
#     print(conta)

# contas = [conta_luan, conta_ana]


# def deposita_para_todas(contas):
#     for conta in contas:
#         conta.deposita(100)


# print(contas[0], contas[1])
# deposita_para_todas(contas)
# print(contas[0], contas[1])

# conta_luan = (15,8) #tupla


from abc import ABCMeta, abstractmethod


class Conta(metaclass=ABCMeta):
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    @abstractmethod
    def passa_o_mes(self):
        pass

    def __str__(self):
        return f"[>>Codigo: {self._codigo} Saldo: {self._saldo}<<]"


class ContaCorrente(Conta):
    def passa_o_mes(self):
        self._saldo -= 2


class ContaPoupanca(Conta):
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3


conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta16.passa_o_mes()
print(conta16)

conta30 = ContaPoupanca(30)
conta30.deposita(1000)
conta30.passa_o_mes()
print(conta30)

contas = [conta16, conta30]

for conta in contas:
    conta.passa_o_mes()  # duck typing
    print(conta)
