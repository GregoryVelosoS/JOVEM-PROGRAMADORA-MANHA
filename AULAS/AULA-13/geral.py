# Lista de princesas
lista_princesas = ["Bela", "Tiana", "Elsa", "Ariel"]
print(lista_princesas)

# Adicionar no final = append()
lista_princesas.append("Mulan")
print(lista_princesas)

# Adicionar em posição específica = insert()
lista_princesas.insert(1, "Pocahontas")
print(lista_princesas)

# Remover alguém específico = remove()
lista_princesas.remove("Ariel")
print(lista_princesas)

# Remove pelo numero do indice = pop()
removido = lista_princesas.pop(2)
print(f'Removida: {removido}')
print(lista_princesas)

# Retorna o índice de alguém = index()
lugar = lista_princesas.index("Elsa")
print(f"O lugar da Elsa na lista: {lugar}")

# Deixa a lista em ordem reversa = reverse
lista_contraria = lista_princesas.reverse()
print(lista_contraria)

# Ordena a lista = sort()
lista_ordenada = lista_princesas.sort()
print(lista_ordenada)

# Retorna o valor da quantidade de itens da lista = len()
print(f"Quantidade de itens: {len(lista_princesas)}")

