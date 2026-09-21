# Saudação
print("Bem vindo a minha loja :) ")

# Entrada
# Primeira Versão
# Solicita
print("Digite o código do produto: ")

#Armazena na memória
cod_prod = 0
cod_prod = input() 

# Segunda Versão
print("Digite o nome do produto:")
nome_prod = input()

# Terceira versão 
cat_prod = input("Digite a categoria: ")
qtd_prod = input("Digite a quantidade disponível: ")
preco_prod = input("Digite o preço do produto: ")

# Mostrar a confirmação
# "\n" = pula a linha
print("\n")
print("--- PRODUTO CADASTRADO ---")
print("Código:", cod_prod)
print("O produto:", nome_prod, "da categoria:", cat_prod)
print("Quantidade:", qtd_prod, "e tem o preço de:R$", preco_prod)
print("\n")