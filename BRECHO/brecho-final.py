# =========================================
# FUNÇÕES
# =========================================

def calcular_produto(preco, quantidade, percentual):
    valor_sem_desconto = preco * quantidade

    valor_desconto = (
        valor_sem_desconto * percentual / 100
    )

    valor_final = (
        valor_sem_desconto - valor_desconto
    )

    return valor_final


def obter_desconto_cliente(tipo):

    if tipo == "Novo":
        return 5

    elif tipo == "VIP":
        return 15

    else:
        return 0


# =========================================
# INÍCIO DO PROGRAMA
# =========================================

print("================================")
print("        SISTEMA DO BRECHÓ")
print("================================")


# DADOS DA CLIENTE

nome_cliente = input(
    "\nNome da cliente: "
)

tipo_cliente = input(
    "Tipo da cliente (Novo/VIP): "
)


# LISTAS DO PEDIDO

produtos = []
valores_produtos = []


# ACUMULADOR

subtotal = 0


# CONTROLE DO WHILE

continuar = "S"


# =========================================
# CADASTRO DOS PRODUTOS
# =========================================

while continuar == "S":

    print("\n----------------------------")
    print("NOVO PRODUTO")
    print("----------------------------")

    produto = input(
        "Nome do produto: "
    )

    quantidade = int(
        input("Quantidade: ")
    )

    preco = float(
        input("Preço unitário: R$ ")
    )

    desconto_produto = float(
        input("Desconto do produto (%): ")
    )


    # CÁLCULO DO PRODUTO

    valor_produto = calcular_produto(
        preco,
        quantidade,
        desconto_produto
    )


    # GUARDA O PRODUTO NAS LISTAS

    produtos.append(produto)

    valores_produtos.append(
        valor_produto
    )


    # ACUMULA NO SUBTOTAL

    subtotal = (
        subtotal + valor_produto
    )


    print(
        "Valor do produto após desconto: R$",
        valor_produto
    )


    # VERIFICA SE EXISTE OUTRO PRODUTO

    continuar = input(
        "\nDeseja adicionar outro produto? S/N: "
    )


# =========================================
# DESCONTO DA CLIENTE
# =========================================

desconto_cliente = (
    obter_desconto_cliente(
        tipo_cliente
    )
)


valor_desconto_cliente = (
    subtotal * desconto_cliente / 100
)


valor_final = (
    subtotal - valor_desconto_cliente
)


# =========================================
# RESUMO DO PEDIDO
# =========================================

print("\n================================")
print("        RESUMO DO PEDIDO")
print("================================")

print(
    "Cliente:",
    nome_cliente
)

print(
    "Tipo:",
    tipo_cliente
)

print("\nProdutos:")


for posicao in range(
    len(produtos)
):

    print(
        posicao + 1,
        "-",
        produtos[posicao],
        "- R$",
        valores_produtos[posicao]
    )


print(
    "\nSubtotal: R$",
    subtotal
)

print(
    "Desconto da cliente:",
    desconto_cliente,
    "%"
)

print(
    "Valor do desconto: R$",
    valor_desconto_cliente
)

print(
    "VALOR FINAL: R$",
    valor_final
)

print("\nPedido finalizado.")
