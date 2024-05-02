from datetime import datetime, timezone

class ContasIterador:
  def __init__(self, contas):
      self.contas = contas
      self._index = 0

  def __iter__(self):
      return self

  def __next__(self):
      try:
          conta = self.contas[self._index]
          return f"""\
          Agência:\t{conta.agencia}
          Número:\t\t{conta.numero}
          Titular:\t{conta.cliente.nome}
          Saldo:\t\tR$ {conta.saldo:.2f}
      """
      except IndexError:
          raise StopIteration
      finally:
          self._index += 1

class Usuario:

  def __init__(self, endereco):
    self.endereco = endereco
    self.contas = []
    self.indice_conta = 0

  def realizar_transacao(self, conta, transacao):
    if len(conta.historico.transacoes_do_dia()) >= 2:
      print("Você excedeu o número de transações para hoje!")
      return
    transacao.registrar(conta)

  def adicionar_conta(self, conta):
    self.contas.append(conta)

class PessoaFisica(Usuario):

  def __init__(self, nome, data_nascimento, cpf, endereco):
    super().__init__(endereco)
    self.nome = nome
    self.data_nascimento = data_nascimento
    self.cpf = cpf

class Conta:
  def __init__(self, numero, usuario):
    self._agencia = "0001"
    self._numero = numero
    self._saldo = 0
    self._usuario = usuario
    self._historico = Historico()

  @classmethod
  def nova_conta(cls, numero, usuario):
    return cls(numero, usuario)

  @property
  def agencia(self):
    return self._agencia

  @property
  def numero(self):
    return self._numero

  @property
  def saldo(self):
    return self._saldo

  @property
  def usuario(self):
    return self._usuario

  @property
  def historico(self):
    return self._historico

  def sacar(self, valor):
    saldo = self.saldo
    valor_excedido = valor > saldo

    if valor_excedido:
      print("Operação falhou! Saldo insuficiente.")
    elif valor > 0:
      self._saldo -= valor
      print("Operação realizada com sucesso!")
      return True

      # self._historico.transacoes.append(f"Saque: R$ {valor:.2f}")

    else:
      print(f"Operação falhou! Valor informado ({valor}) é inválido.")
    return False

  def depositar(self, valor):
    if valor > 0:
      self._saldo += valor
      print("Operação realizada com sucesso!")

      # self._historico.transacoes.append(f"Deposito: R$ {valor:.2f}")

    else:
      print("Operação falhou! Valor informado é inválido.")
      return False

    return True

class ContaCorrente(Conta):

  def __init__(self, numero, usuario, limite=500, limite_saque=3):
    super().__init__(numero, usuario)
    self.limite = limite
    self.limite_saque = limite_saque
    
  @classmethod
  def nova_conta(cls, numero, usuario, limite=500, limite_saque=3):
    return cls(numero, usuario, limite, limite_saque)

  def sacar(self, valor):
    numero_saques = len([
        transacao for transacao in self.historico.transacoes
        if transacao["tipo"] == "Saque"
    ])
    limite_excedido = valor > self.limite
    excedeu_limite_saque = numero_saques >= self.limite_saque

    if limite_excedido:
      print("Operação falhou! Limite de saque excedido.")
    elif excedeu_limite_saque:
      print(
          f"Operação falhou! Número máximo de saques excedido ({self.limite_saque}"
      )
    else:
      return super().sacar(valor)
    return False
    
  def __str__(self):
    return f"""\
        Agência:\t{self.agencia}
        C/C:\t\t{self.numero}
        Titular:\t{self.usuario.nome}
    """    

class Historico:
  def __init__(self):
    self._transacoes = []
    
  @property
  def transacoes(self):
    return self._transacoes
    
  def adicionar_transacao(self, transacao):
    self._transacoes.append(
      {
        "tipo": transacao.__class__.__name__,
        "valor": transacao.valor,
        "data": datetime.utcnow().strftime("%d-%m-%Y %H:%M:%S"),
      }
    )

  def gerar_relatorio(self, tipo_transacao=None):
    for transacao in self.transacoes:
      if(tipo_transacao is None or transacao["tipo"].lower() == tipo_transacao.lower()):
        yield transacao

  def transacoes_do_dia(self):
    data_atual = datetime.now().date()
    transacoes =[]
    for transacao in self._transacoes:
      data_transacao = datetime.strptime(transacao["data"], "%d-%m-%Y %H:%M:%S").date()
      if data_transacao == data_atual:
        transacoes.append(transacao)
    return transacoes

class Transacao:
  @property
  def valor(self):
      pass

  @classmethod
  def registrar(self, conta):
      pass

class Deposito(Transacao):
  def __init__(self, valor):
    self._valor = valor

  @property
  def valor(self):
    return self._valor
    
  def registrar(self, conta):
    sucesso_transacao = conta.depositar(self.valor)

    if sucesso_transacao:
        conta.historico.adicionar_transacao(self)
    
class Saque(Transacao):
  def __init__(self, valor):
      self._valor = valor

  @property
  def valor(self):
      return self._valor

  
  def registrar(self, conta):
      sucesso_transacao = conta.sacar(self.valor)

      if sucesso_transacao:
          conta.historico.adicionar_transacao(self)

# Funções para visualização 

def log_transacao(funcao):
  def wrapper(*args, **kwargs):
    resultado = funcao(*args, **kwargs)
    print(f"{datetime.now()}: {funcao.__name__.upper()}")
    return resultado
  return wrapper

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario.cpf == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def recuperar_conta_cliente(usuario):
    if not usuario.contas:
        print("Cliente não possui conta!")
        return

    # TO DO: permitir cliente escolher a conta
    return usuario.contas[0]

@log_transacao
def depositar(usuarios):
    cpf = input("Informe o CPF do cliente: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("Usuario não encontrado!")
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor=valor)

    conta = recuperar_conta_cliente(usuario)
    if not conta:
        return

    usuario.realizar_transacao(conta, transacao)

@log_transacao
def sacar(usuarios):
    cpf = input("Informe o CPF do cliente: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("Cliente não encontrado!")
        return

    valor = float(input("Informe o valor do saque: "))
    print(f"Valor de saque: R$ {valor:.2f}")
    transacao = Saque(valor=valor)

    conta = recuperar_conta_cliente(usuario)
    if not conta:
        return

    usuario.realizar_transacao(conta, transacao)

@log_transacao
def exibir_extrato(usuarios):
    cpf = input("Informe o CPF do cliente: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("Cliente não encontrado!")
        return

    conta = recuperar_conta_cliente(usuario)
    if not conta:
        return

    print("\n================ EXTRATO ================")
    transacoes = conta.historico.transacoes

    extrato = ""
    existe_transacao = False
    for transacao in conta.historico.gerar_relatorio():
      existe_transacao = True
      extrato += f"\n{transacao['data']}\n{transacao['tipo']}:\n\tR${transacao['valor']:.2f}"
    if not existe_transacao:
        extrato = "Não foram realizadas movimentações."

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")

@log_transacao
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_usuario(cpf, usuarios)

    if cliente:
        print("\nJá existe cliente com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    usuarios.append(cliente)

    print("\n=== Usuário criado com sucesso! ===")

@log_transacao
def criar_conta(numero_conta, usuarios, contas):
    cpf = input("Informe o CPF do cliente: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("Usuário não encontrado, fluxo de criação de conta encerrado!")
        return

    conta = ContaCorrente.nova_conta(usuario=usuario, numero=numero_conta)
    contas.append(conta)
    usuario.contas.append(conta)

    print("\n=== Conta criada com sucesso! ===")

def listar_contas(contas):
    for conta in contas:
        print("=" * 10)
        print(str(conta))

def main():
    usuarios = []
    contas = []

    while True:
        menu = """
        ================ MENU ================
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
          criar_conta(numero_conta, usuarios, contas)

        elif opcao == "u":
          criar_usuario(usuarios)

        elif opcao == "l":
          listar_contas(contas)
      
        elif opcao == "d":
          depositar(usuarios)
          
        elif opcao == "s":
          sacar(usuarios)
          
        elif opcao == "e":
          exibir_extrato(usuarios)  

        elif opcao == "q":
          break

        else:
          print("Operação inválida, por favor selecione novamente a operação desejada.")

main()