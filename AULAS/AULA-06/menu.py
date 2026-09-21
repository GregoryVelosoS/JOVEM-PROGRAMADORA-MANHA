print("Buenos días, arriba 🎩")

# Menu
print("--- CALCULADORA TOP ---")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

# Escolhe a operação
operacao = int(input("Escolha uma das operações:"))

#Escolher os números
num1 = float(input("Escolha um número:"))
num2 = float(input("Escolha outro número:"))

resultado = "INVÁLIDO"
# Faz a conta
match operacao:
    case 1:
        print("Somando...")
        resultado = num1 + num2
    case 2:
        print("Diminuindo...")
        resultado = num1 - num2
    case 3:
        print("Multiplicando...")
        resultado = num1 * num2
    case 4:
        print("Dividindo...")
        resultado = num1 / num2
    case _:
        print("OPÇÃO INVÁLIDA !!!")

# Mostrar o resultado
print("O Resultado da operação é:", resultado)