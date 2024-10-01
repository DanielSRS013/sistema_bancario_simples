print("----------BANCO DO DN----------")
print("-----------Operações-----------")
print("1 - Sacar")
print("2 - Depositar")
print("3 - Ver Extrato")
print("4 - Encerrar")
print("OBS.: Limite de saques diários é 3 e R$ 500,00")


#Variáveis utilizadas para guardas as operações
depositos = 0.0
saques = 0.0
extrato = 0.0
historico_transacoes = []
NUMERO_SAQUES = 3


#faz depositos

def faz_deposito(valor):
  valor = float(input("Digite o valor que quer depositar: "))
  if valor <0 or valor ==0:
    print("valor inválido")
  else:
    print(f"Deposito de R${valor} realizado com sucesso")
  return valor

#faz saque

def faz_saque(valor):
  valor = float(input("Digite o valor que deseja sacar: "))
  if(valor > extrato):
    print("Saldo insuficiente")
  elif valor == 0:
    print("Você não pode sacar R$ 0,00")
  else:
    print("Saque realizado com sucesso")
  return valor


#FOR onde serão postos os inputs solicitando as operações a seres realizadas
for operacao in range(1, 100, 1):
  operacao = int(input("Digite o que deseja fazer: "))
  
  #Tratamento caso digite uma transação inválida
  if operacao != 1 and operacao != 2 and operacao != 3 and operacao != 4:
    print("Transação inválida. Tente Novamente")
    continue

  #Operação Saque
  if operacao == 1:
    if NUMERO_SAQUES ==0:
      print("Você atingiu o limite diário de saques")
    else:
      saque = faz_saque(0)
      historico_transacoes.append(f'Saque:  R$ {saque}')
      if saque > 500:
        print("O limite de saque é R$ 500")
      else:
        extrato -= saque
        NUMERO_SAQUES-=1

  #Operação Depósito
  elif operacao == 2:
    deposito =faz_deposito(0)
    extrato += deposito
    historico_transacoes.append(f'Depósito:  R$ {deposito}')
    
  #Operação Ver Extrato
  elif operacao == 3:
    print("\n")
    print(f"Seu extrato atual: {extrato}")
    print("Histórico de transações")
    #For onde será mostrada a lista de operações realiazadas
    for transacoes in historico_transacoes:
      print(transacoes)
  elif operacao == 4:
    print("Encerrando")
    break