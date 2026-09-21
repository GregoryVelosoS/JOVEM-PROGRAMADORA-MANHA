#Saudação 
print("Seja bem vindo ao Simulador de empréstimo")

# Informações
valor_desejado = float(input("Qual o valor desejado?:R$"))
qtd_parcelas   = int(input("Qual a quantidade de parcelas?"))

# Calcular o empréstimo
# valor_desejado * 20 / 100 ou valor_desejado * 0.2
# Calcula os juros
juros = valor_desejado * (20 / 100)
# Soma ao valor do empréstimo original
valor_final = valor_desejado + juros
# Calcula a parcela
valor_parcela = valor_final / qtd_parcelas

# Saída - Mostra as informações na tela 
print("Valor solicitado:", valor_desejado)
print("Total com juros:", valor_final)
print("Quantidade de parcelas:", qtd_parcelas)
print("Valor de cada parcela:", valor_parcela)