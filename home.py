from Cliente import Cliente
from Conta import Conta
from Inter import InterfaceGrafica

print('Teste 1 do projeto')

c1 = Cliente("Olavo", "110222-2121")
conta = Conta(c1.nome, 620, 1220)
conta.saque(300)
extrato = conta.extrato()


print(f"Proprietário da conta: {c1.nome}\nNúmero da conta: {conta.numero}\nSaldo: {conta.get_saldo()}\n")

conta.saque(300)
conta.extrato()