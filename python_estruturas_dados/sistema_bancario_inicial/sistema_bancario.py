menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
          saldo += valor
          print("Deposito realizado com sucesso! \n")

          extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
          print("Não foi possivel realizar o depósito. \n")
      
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
      
        if valor > 0:
          if valor <= saldo and valor <= limite:
            saldo -= valor
            print("Saque realizado com sucesso! \n")
            print(f"Valor de saque: R$ {valor:.2f}")
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            
          elif valor > saldo:
            print("Saldo insuficiente! \n")
            
          elif numero_saques > LIMITE_SAQUES:
            print("Número de saques excedido! \n")
            
          elif valor > limite:
            print("Limite de saque excedido! \n")
            
          else:
            print("Não foi possivel realizar o saque. \n")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        if not extrato:
          print("Não foram realizadas movimentações.")
        else: 
          print(extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")