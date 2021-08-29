class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Contruindo objecto ...{0}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def sacar(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print("O valor {} passou do limite".format(valor))

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def set_limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_banco():
        return {"BB": "001", "Caixa": "104", "Bradesco": "237"}


conta = Conta(111, "Luan", 100.00, 1000.00)
conta2 = Conta(550, "Luana", 0.00, 1000.00)

conta.codigo_banco()

conta.codigos_banco()

conta.deposita(500)

conta.transferir(500, conta2)
