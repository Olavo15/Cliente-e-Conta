class Main:
    pass
print('Teste 1 do projeto')

from cliente import Cliente
from conta import Conta

c1 = Cliente("Olavo", "110222-2121")

conta = Conta(c1.nome, 620, 1000)

print(f"Proprietario da conta: {c1.nome}\nNumero da conta: {conta.numero}\nsaldo:{conta.saldo}")