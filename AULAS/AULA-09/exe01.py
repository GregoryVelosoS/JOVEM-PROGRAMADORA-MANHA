# Criei a função
def gerador(mensagem):
    print("-----------")
    print(mensagem)
    print("-----------")

# Pede pra pessoa
texto = input("Digite a mensagem:")

#chama a função 
gerador(texto)

##################################
# EXERCÍCIO 2
def maior(num1,num2):
    if (num1 > num2):
        print(num1)
    elif (num1 < num2):
        print(num2)
    else:
        print("São iguais")

primeiro = int(input("Digite o primeiro número:"))
segundo = int(input("Digite o segundo número:"))

maior(primeiro, segundo)