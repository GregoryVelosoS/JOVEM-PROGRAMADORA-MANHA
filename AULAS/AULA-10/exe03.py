# Criar função
def aplicar_desconto(valor,percentual):
    print("Estou calculando...")
    # Calcula apenas o valor de desconto
    desc = valor * (percentual / 100)
    # Diminuir o valor de desconto, do valor original
    preco_final = valor - desc
    # retornar o preco final
    return preco_final

#Pede as informações pra pessoa
valorPedido = float(input("Digite o valor do pedido:"))
desconto = int(input("Digite o valor de desconto:"))

#Chamo/executo a função 
resultado_final = aplicar_desconto(valorPedido, desconto)
print(f"O valor do pedido é: { resultado_final }")