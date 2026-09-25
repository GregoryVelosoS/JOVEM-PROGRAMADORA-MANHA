#FUNÇÃO NORMAL
def abandonar_lugar():
    print("/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")
    print("----- SAIA IMEDIATAMENTE --------")
    print("-- ISSO NÃO É UM TREINAMENTO ----")
    print("----- SAI DAQUI AGORA, VAI ------")
    print("/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")

# CHAMA A FUNÇÃO NORMAL
abandonar_lugar()

# FUNÇÃO COM PARÂMETRO
def comprar_pao(dinheiro, qtd):
    valor_pao = 1.5
    preco_pago = qtd * valor_pao
    troco = dinheiro - preco_pago
    print(f"Você comprou {qtd} pães e sobrou R${troco}")
    print("-------------------------------------------")

# CHAMA A FUNÇÃO COM PARÂMETRO, PASSANDO VALORES
comprar_pao(10,6)

# Deixar interativo
dindin = float(input("Informe a quantidade de dinheiro:"))
paes = int(input("Informe a quantidade de pães:"))
comprar_pao(dindin, paes)