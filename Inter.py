# Arquivo Inter.py
import tkinter as tk
from Cliente import Cliente
from Conta import Conta

class InterfaceGrafica:
    def __init__(self, master):
        self.master = master
        master.title("Sistema Bancário")

        self.label = tk.Label(master, text="Bem-vindo ao Sistema Bancário")
        self.label.pack()

        self.saldo_label = tk.Label(master, text="Saldo Atual: 0.00")
        self.saldo_label.pack()

        self.button_saque = tk.Button(master, text="Realizar Saque", command=self.realizar_saque)
        self.button_saque.pack()

        self.button_deposito = tk.Button(master, text="Realizar Depósito", command=self.realizar_deposito)
        self.button_deposito.pack()

        self.extrato_label = tk.Label(master, text="")
        self.extrato_label.pack()

        # Inicializa a conta com saldo 0.00
        self.c1 = Cliente("Olavo", "110222-2121")
        self.conta = Conta(self.c1.nome, 620, 0.00)

    def realizar_saque(self):
        valor_saque = 50  # Valor fixo para exemplo, você pode modificar conforme necessário
        self.conta.saque(valor_saque)
        extrato = self.conta.extrato()
        self.extrato_label.config(text=extrato)
        self.atualizar_saldo()

    def realizar_deposito(self):
        valor_deposito = 100  # Valor fixo para exemplo, você pode modificar conforme necessário
        self.conta.deposita(valor_deposito)
        extrato = self.conta.extrato()
        self.extrato_label.config(text=extrato)
        self.atualizar_saldo()

    def atualizar_saldo(self):
        saldo_atual = self.conta.get_saldo()
        self.saldo_label.config(text=f"Saldo Atual: {saldo_atual:.2f}")


root = tk.Tk()
app = InterfaceGrafica(root)
root.mainloop()
