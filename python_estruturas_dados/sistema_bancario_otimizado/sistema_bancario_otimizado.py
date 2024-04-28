def criar_usuario(usuarios):

  cpf = input("Informe o CPF (somente número): ")
  usuario = filtrar_usuario(cpf, usuarios)

  if usuario:
      print("Já existe usuário com esse CPF!")
      return

  nome = input("Informe o nome completo: ")
  data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
  endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

  usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

  print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
  for usuario in usuarios:
    if usuario["cpf"] == cpf:
      return usuario
    else:
      return None

def criar_conta(agencia, numero_conta, usuarios):
  cpf = input("Informe o CPF (somente números): ")
  usuario = filtrar_usuario(cpf, usuarios)

  if usuario:
    conta = {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("Conta criada com sucesso!")
    return conta     
  else:
    print("Usuário não encontrado!")
    
def listar_contas(contas):
  for conta in contas:
      linha = f"""\
          Agência:\t{conta['agencia']}
          C/C:\t\t{conta['numero_conta']}
          Titular:\t{conta['usuario']['nome']}
      """
      print(linha)

def depositar(saldo, valor, extrato, /):
  if valor > 0:
    saldo += valor
    print("Deposito realizado com sucesso! \n")

    extrato += f"Depósito: R$ {valor:.2f}\n"

  else:
    print("Não foi possivel realizar o depósito. \n")

  return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
  if valor > 0:
    if valor <= saldo and valor <= limite:
      saldo -= valor
      print("Saque realizado com sucesso! \n")
      print(f"Valor de saque: R$ {valor:.2f}")
      extrato += f"Saque: R$ {valor:.2f}\n"
      numero_saques += 1

    elif valor > saldo:
      print("Saldo insuficiente! \n")

    elif numero_saques > limite_saques:
      print("Número de saques excedido! \n")

    elif valor > limite:
      print("Limite de saque excedido! \n")

    else:
      print("Não foi possivel realizar o saque. \n")

  return saldo, extrato  

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
      print("Não foram realizadas movimentações.")
    else: 
      print(extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def main():
  saldo = 0
  limite = 500
  extrato = ""
  numero_saques = 0
  contas = []
  usuarios = []
  
  AGENCIA = "0001"
  LIMITE_SAQUES = 3

  while True:
      menu = """

      [n] Nova conta
      [u] Novo usuário
      [l] Listar contas
      [d] Depositar
      [s] Sacar
      [e] Extrato
      [q] Sair

      Selecione uma opção:  """
      opcao = input(menu)

      if opcao == "n":
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)

      elif opcao == "u":
        criar_usuario(usuarios) 
        
      elif opcao == "l":
        listar_contas(contas) 

      elif opcao == "d":
          valor = float(input("Informe o valor do depósito: "))

          saldo, extrato = depositar(saldo, valor, extrato)

      elif opcao == "s":
          valor = float(input("Informe o valor do saque: "))

          saldo, extrato = sacar(
              saldo=saldo,
              valor=valor,
              extrato=extrato,
              limite=limite,
              numero_saques=numero_saques,
              limite_saques=LIMITE_SAQUES,
          )

      elif opcao == "e":
          exibir_extrato(saldo, extrato=extrato)

      elif opcao == "q":
          break

      else:
          print("Operação inválida, por favor selecione novamente a operação desejada.")

main()