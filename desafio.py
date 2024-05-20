menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
######################
"""

saldo = 0
LIMITE = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def deposito(valor):
    global saldo, extrato, numero_saques
    if(valor > 0):
        print("Depósito recebido com sucesso!")
        saldo += valor
        extrato += f"""
    Depósito recebido de R$ {valor:.2f}
----------------------------------------
"""
    else:
        print("Não é aceito operação com números negativos")

def saque(valor):
    global saldo, extrato, numero_saques

    if(valor <= saldo and valor <= 500 and numero_saques < LIMITE_SAQUES and valor > 0):
        saldo -= valor
        print("Saque realizado com sucesso!")
        numero_saques += 1
        extrato += f"""
    Saque realizado de R$ {valor:.2f}
----------------------------------------
"""
    
    elif(valor > saldo):
        print(f"O valor disponível é de R$ {saldo:.2f}")

    elif(valor > 500):
        print("O valor máximo de saque é de R$ 500.00")

    elif(valor < 0):
        print("Não é aceito operação com números negativos")

    else:
        print("Você já atingiu o limite de saques no dia")

def extrato_print():
    global saldo
    print(extrato)
    print(f"Valor em conta: R$ {saldo:.2f}")

while True:
    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        deposito(float(input()))

    elif opcao == "s":
        print("Saque")
        saque(float(input()))

    elif opcao == "e":
        print("Extrato")
        extrato_print()

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor, selecione novamente a opção desejada.")