# SAUDAÇÕES 
print("======= BRECHÓ TOP =======")

# DADOS DA CLIENTE
nome_cliente = input("Nome da cliente:")
tipo_cliente = input("Tipo (Novo ou Vip):")

#ÁREA DE PRODUTOS
# Pergunta a quantidade de produtos
qtd_produtos = int(input("Quantos produtos diferentes serão adicionados ao pedido?"))

# Variável que guarda o preço geral
total_pedido = 0

# Repetição para comprar vários produtos
for item in range(qtd_produtos):
    print()
    print(f'=== PRODUTO:{item + 1} ===')

    # Informações do produto atual
    cod_prod = input("Código:")
    nome_prod = input("Nome:")
    cat_prod = input("Categoria:")
    qtd_atual = int(input("Quantidade:"))
    preco_prod = float(input("Preço do produto:"))
    desconto_prod = int(input("Desconto do produto:"))

    # Cálculo de desconto
    valor_sem_desconto = preco_prod * qtd_atual
    valor_desconto = valor_sem_desconto * (desconto_prod / 100)
    subtotal = valor_sem_desconto - valor_desconto

    # Guardar o valor do pedido atual, na variável geral
    total_pedido = total_pedido + subtotal

    # Mostra o pedido na tela
    print(f'Produto: {nome_prod}, Código: {cod_prod}')
    print(f'Categoria:{cat_prod},Quantidade: {qtd_atual}')
    print(f'Valor sem desconto: {valor_sem_desconto}, Desconto:{valor_desconto}')
    print(f'Subtotal: {subtotal}')

# Calcula o valor do pedido, dependendo do tipo da cliente
# decide o desconto pelo tipo
if( tipo_cliente == "Novo"):
    desconto_cliente = 5
else:
    desconto_cliente = 15

# faz o cálculo da porcentagem do desconto
valor_desconto_cliente = desconto_cliente / 100

# usa a porcentagem no preço geral
valor_final = total_pedido - (total_pedido * valor_desconto_cliente)

# MOSTRA AS INFORMAÇÕES PRINCIPAIS NA TELA
print()
print("=== TOTAL DO PEDIDO ===")
print(f"Cliente: {nome_cliente}")
print(f"Tipo: {tipo_cliente}")
print(f"Total final: R${valor_final}")