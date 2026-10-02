# Criando a lista vazia
carrinho = [] 

# Repete a interação com usuário 3 vezes
for x in range(3):
    # Usuário escolhe um item pra adicionar
    # compra_atual = "Pikachu"
    compra_atual = input("Digite qual produto deseja adicionar:")

    # Append - adiciona valor a uma lista
    carrinho.append(compra_atual)

    print("-----------------------------")

#Mostra agora a lista completa de compras (com for)
# len() - tamanho da lista 
print(f"O tamanho da lista atual é {len(carrinho)}")

for item in range(len(carrinho)):
    print(f"O item atual é:{carrinho[item]}")