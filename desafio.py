menu = """

[d] - Depositar
[s] - Sacar
[e] - Extrato
[q] - Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == "d":
        valor = float(input("informe o valor do depósito: R$"))
        if valor > 0:
            saldo += valor
            extrato += f"    Depósito: R${valor:.2f}\n"
        else:
            print("    Operação falhou! o valor informado é invalido.")
    
    elif opcao == "s":
        valor = float(input("informe o valor do saque: R$"))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        if excedeu_saldo:
            print("    Operação falhou! Você não tem saldo suficiente para essa operação.")
        elif excedeu_limite:
            print("    Operação falhou! O valor do saque excede o seu limite.")
        elif excedeu_saques:
            print("    Operação falhou! Número de saques diários foi excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"    Saque: R${valor:.2f}\n"
            numero_saques += 1
        else:
            print("    Operação falhou! Valor informado é invalido.")
    
    elif opcao == "e":
        print("\n========================= EXTRATO =========================")
        print("\n================ BEM VINDOS AO BANCO REAL =================")
        print("\n    Não foram realizadas movimentações no período." if not extrato else extrato)
        print(f"\n    Saldo: R$ {saldo:.2f}")
        print("===========================================================")
    
    elif opcao == "q":
        break

    else:
        print("\n    Operação invalida! Selecione novamente a operação desejada.")