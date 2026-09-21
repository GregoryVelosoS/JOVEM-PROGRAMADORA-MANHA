print("SEJA BEM VINDA AO INCRÍVEL SHOW DO TWICE🍭👯‍♀️")

#Cria o laço de repetição
while True:
    #Coletar as informações
    nomeParticipante = input("Digite o nome da participante:")
    idadeParticipante = input("Digite a idade da participante:")
    cidadeParticipante = input("Digite a cidade da participante:")

    # Mostro o cadastro
    print(f"O nome dela é:{nomeParticipante}, tem {idadeParticipante} anos e mora em {cidadeParticipante} ")

    print("=======================================================")
    continuar = input("Deseja continuar? (1 - Sim/2 - Não):")
    if(continuar == "Sim" or continuar == "1"):
        print("Ok, vamos realizar um novo cadastro !!!")
    else:
        # BREAK - para a execução de uma laço de repetição
        break

print("FIM DE CADASTROS")