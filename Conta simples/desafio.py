menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] sair\n
"""

saldo = 0

limite = 500

extrato = ""

numero_saques = 3

LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao.lower() == "d":
        valor = float(input("Digite o valor a ser depositado: "))
        
        if valor >= 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            
        else:
            print ("Operação falhou! o valor informado é inválido.")
            
    elif opcao.lower() == "s":
        valor = int(input("Digite o valor a ser sacado: "))
        
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print  ("Operação falhou! Saldo insuficiente.")
        elif excedeu_limite:
            print  ("Operação falhou! Excedeu o limite de saques.")
        elif excedeu_saques:
            print  ("Operação falhou! número máximo de saques excedido.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print  ("Operação falhou! o valor informado é inválido.")

    elif opcao.lower() == "e":
        print("\n========== Extrato ==========")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("============================")
        
    elif opcao.lower() == "q":
        break
    
    else:
        print  (f"Opção inválida!, Por favor selecione novamente a operação desejada.")

