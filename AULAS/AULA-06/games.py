print("Bem vindo a meu mundo")
print("Quer café?")

# Mostrar as opções
print("*** UTILIZE APENAS NÚMEROS PARA NAVEGAÇÃO ***")
print("-----------------------------")
print("Opções de atendimento:")
print("1 - Comprar jogo")
print("2 - Suporte técnico")
print("3 - Acompanhar pedido")
print("4 - Cancelar Assinatura")
print("5 - Falar com atendente")
print("0 - Encerrar contato")

#Pessoa escolhe a opcao
opcao = int( input("Escolha uma opção:") )

match opcao: 
    case 1:
        print("Direcionando ao setor de vendas...")
    case 2:
        print("Indo pro suporte...")
    case 3:
        print("Rastreando pedido...")
    case 4:
        print("Transferindo para o setor de cancelamento")
    case 5:
        print("Buscando um atendente para você...")
    case 0:
        pass
    case _:
        print("OPÇÃO INVÁLIDA")

#Finalizar o programa
print("FIM DE PROGRAMA")