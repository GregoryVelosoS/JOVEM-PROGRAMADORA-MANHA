# Declaração da variável e atribuição
c = 0

# Laço enquanto
while c < 5:
    print("O valor de C é:", c)
    c += 1

# adivinhe um número
numero = 0
while (numero != 7):
    print(" ----------------------------------- ")
    print("Tente adivinhar um número de 0 até 10")
    numero = int(input("Digite um número?:"))
    meuNumero = 7

    if(numero == meuNumero):
        print("Você acertou :)")
    else:
        print("ERROOOOOUUUUUU")