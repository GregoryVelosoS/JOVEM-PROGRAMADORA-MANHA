print("Oi, boa noite...")

# Coletar informações
nome = input("Informe seu nome:")
salario_atual = float(input("Informe o valor do salário atual:"))
tempo_empresa = int(input("Digite seu tempo de empresa(em anos):"))

# Adicionando informação de porcentagem de aumento
porcentagem_aumento = 0
if ( tempo_empresa < 3):
    porcentagem_aumento = 3 / 100 # = 0.03
elif ( (tempo_empresa >= 3) and (tempo_empresa < 10) ):
    porcentagem_aumento = 0.125 # = 12.5 / 100
else:
    porcentagem_aumento = 0.2 # = 20 / 100

# Calculo do novo salário
# Descubro o quanto a mais ele vai ganhar
aumento = salario_atual * porcentagem_aumento

# Somo o aumento, com o salário atual
novo_salario = salario_atual + aumento

# Informa o salário novo pro usuário
print("Parabéns, seu novo salário é:", novo_salario)
print("💸🤑")