# Criar uma lista vazia
lista_nomes = ["Ana", "Lahra"]

# repete o processo 3 vezes
for x in range(3):
    # Pedir o nome pro usuário
    nome_atual = input("Informe um nome top:")
    #Adicionar o nome na lista
    lista_nomes.append(nome_atual)

# Mostrar os nomes
# len() = Retorna o tamanho da lista
print("----- Lista de nomes geral ------")
for item in range(len(lista_nomes)):
    print(f"O nome do index {item} é {lista_nomes[item]}")

print("---------------------------------")
print("----- ó o reverse... ------")
# range(X,Y,Z)
for pessoa in range(len(lista_nomes) - 1 , -1, -1):
    print(f"O nome do index {pessoa} é {lista_nomes[pessoa]}")

# Mostra a lista toda, só que ao contrário
print(lista_nomes.reverse())