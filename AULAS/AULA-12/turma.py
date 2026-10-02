#Crie um código que receba o nome de 5 alunos e os armazene em um array, em seguida receba as notas dos alunos e os armazene em outro array. Ao final mostre os valores dos dois vetores separadamente.

# Criar os arrays
lista_alunos = ["Cristiano", "Maria", "McQueen", "JB", "Rumi"]
lista_notas =  [ 7, 10, 9, 5, 8] 

# Mostrar os valores
# Só os alunos
for item in range(5):
    print(f"O nome é: {lista_alunos[item]}")
    print(f"A nota é: {lista_notas[item]}")

