# CADASTRO DE CLIENTES
print("Boas vindas ao meu incrível pograma")

# for - durante
# contador - conta quantas repetições já teve
# range - intervalo de valores
# (x,y,z) - x - começo, y - final, z - incremento
for contador in range(0,3,1):
    print("==================================")
    cliente = input("Nome da cliente:")
    cpf = input("Digite o CPF:")
    print(f"Seu nome é {cliente} e seu CPF é { cpf }")
    print("==================================")

# x - variavel contadora
# range(numero) - numero será a quantidade de repetições
for x in range(5):
    print("AOBA")