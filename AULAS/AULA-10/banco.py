# MYBANK 
# IMPORTAÇÃO DE BIBLIOTECAS
import os
import time

# Criar função para esperar um tempo
def esperar(segundos):
    time.sleep(segundos)

# Criar função de transição nas telas
def animacaoCarregamento(mensagem = "Processando", ciclos = 3, intervalo = 0.4 ):
    #Mostra a mensagem
    print(mensagem, end="", flush=True)
    #Mostra os pontinhos
    for _ in range(ciclos):
        time.sleep(intervalo)
        print(".", end="",flush=True)
    print()


# Criar função para limpar a tela do usuário
def apagarTela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Coletar as informações pessoais
usuario = input("Informe seu nome: ")
meuSaldo = float(input("Informe seu saldo atual:R$"))

#ÁREA DAS FUNÇÕES
# Função Mensagem Bem vindo
def bemVindo():
    apagarTela()
    print("----------------------------------")
    print("--- SEJA BEM VINDO AO MYBANK+ ----")
    print(f"{usuario}, temos prazer em ajudar")
    print("--- AGRADEÇEMOS A PREFERÊNCIA ----")
    print("----------------------------------")
    animacaoCarregamento("Iniciando sistema", 10, 0.5)

#ANTES DA FUNÇÃO DE MENU !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# Função de sacar dinheiro
def sacarDinheiro(valorSaque):
    global meuSaldo
    animacaoCarregamento("Validando saque", 10, 0.5)
    #Verifica se tem saldo pra fazer a operação
    if (valorSaque > meuSaldo):
        print("SALDO INSUFICIENTE PARA OPERAÇÃO")
    else:
        # Meu saldo, atualiza dimunindo o valor sacado
        meuSaldo = meuSaldo - valorSaque
        print("OPERAÇÃO CONCLUÍDA COM SUCESSO")

# Função de depositar dinheiro
def depositarDinheiro(valorDeposito):
    global meuSaldo
    animacaoCarregamento("Depositando", 10, 0.5)
    # meuSaldo = meuSaldo + valorDeposito
    meuSaldo += valorDeposito
    print("OPERAÇÃO CONCLUÍDA COM SUCESSO")

#Função de menu do programa
def menu():
    global meuSaldo
    while True: 
        apagarTela()
        # Opções 
        print("MENU")
        print("1 - SACAR DINHEIRO")
        print("2 - DEPOSITAR DINHEIRO")
        print("3 - VER SALDO")
        print("0 - SAIR")

        escolhaMenu = int(input("Escolha uma opção:"))

        #Verificar se é válido
        if(escolhaMenu < 0 or escolhaMenu > 3):
            print("OPÇÃO INVÁLIDA")
            print("*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/")
        else:
            # Decide qual função chamar, de acordo com a opção escolhida
            match(escolhaMenu):
                case 1:
                    # Chama a função de sacar
                    valor = float(input("Informe o valor de saque:"))
                    sacarDinheiro(valor)
                case 2:
                    # Chama a função de depositar
                    valor = float(input("Informe o valor de depósito:"))
                    depositarDinheiro(valor)
                case 3:
                    # Mostra o saldo
                    # PASS - executa o próximo comando 
                    animacaoCarregamento("Consultado saldo", 15, 0.5)
                    pass
                case 0:
                    # Fecha o programa
                    # BREAK - Para o laço de repetição
                    animacaoCarregamento("Encerrando", 20, 0.5)
                    print("FIM DO PROGRAMA >)")
                    break
            print(f"Seu saldo atual é {meuSaldo}")
            esperar(5)
                


# ÁREA DO PROGRAMA
# Chamar as funções
bemVindo()
menu()