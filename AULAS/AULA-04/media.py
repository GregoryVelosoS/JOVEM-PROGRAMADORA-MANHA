print("Olá, bem vindo ao meu programa :)")

# Pegar as informações
aluno = input("Informe seu nome:")
media = float(input("Informe o valor da sua média:"))

# Fazer a verificação
if (media >= 6):
    print("Parabéns, você foi aprovado")
elif (media >=5):
    print("Você está de recuperação")
else:
    print("Puxa, não foi dessa vez que você conseguiu")

