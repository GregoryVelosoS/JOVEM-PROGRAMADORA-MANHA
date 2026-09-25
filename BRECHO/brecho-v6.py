def calcular_produto(preco, quantidade, percentual):
    valor_sem_desconto = preco * quantidade
    desconto = valor_sem_desconto * percentual / 100
    valor_final = valor_sem_desconto - desconto
    return valor_final


def obter_desconto_cliente(tipo):
    if tipo == "Novo":
        return 5
    elif tipo == "VIP":
        return 15
    else:
        return 0


print("=== BRECHÓ ===")

nome_cliente = input("Nome da cliente: ")
tipo_cliente = input("Tipo da cliente (Novo/VIP): ")

subtotal = 0
continuar = "S"

while continuar == "S":
    print("\n--- PRODUTO ---")

    produto = input("Produto: ")
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço: "))
    desconto_produto = float(input("Desconto do produto (%): "))

    valor_produto = calcular_produto(
        preco,
        quantidade,
        desconto_produto
    )

    subtotal = subtotal + valor_produto

    print("Valor do produto: R$", valor_produto)

    continuar = input("Deseja adicionar outro produto? S/N: ")

desconto_cliente = obter_desconto_cliente(tipo_cliente)

valor_desconto_cliente = subtotal * desconto_cliente / 100
valor_final = subtotal - valor_desconto_cliente

print("\n=== RESUMO ===")
print("Cliente:", nome_cliente)
print("Tipo:", tipo_cliente)
print("Subtotal: R$", subtotal)
print("Desconto:", desconto_cliente, "%")
print("Valor final: R$", valor_final)
