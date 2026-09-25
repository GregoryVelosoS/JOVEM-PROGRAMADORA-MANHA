# FUNÇÃO NORMAL
def mostrar():
    print("OI")

# chama a função
mostrar()

# FUNÇÃO COM RETORNO
def dobro(numero):
    resultado = numero * 2 
    return resultado

# Guarda o retorno da função em uma variável
retorno = dobro(5)

# Mostra na tela o retorno da função
# que está guardado em uma variável
print(f"O dobro é {retorno}")