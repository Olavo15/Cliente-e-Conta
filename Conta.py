class Conta:
    def __init__(self, titular, numero, saldo):
        self.saldo = 1000.00
        self.numero = numero
        self.titular = titular

    def get_saldo(self):
        return self.saldo

    def set_saldo(self, saldo):
        if saldo < 0:
            print("O saldo não pode ser negativo")
        else:
            self.saldo = saldo

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print("Saque realizado com sucesso")
        else:
            print("Saldo insuficiente")

    def deposita(self, valor):
        self.saldo += valor

    def extrato(self):
        return f"Cliente: {self.titular}\nSaldo Atual: {self.saldo}"