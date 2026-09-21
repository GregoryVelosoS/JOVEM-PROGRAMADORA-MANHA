print("I'm glad you came...🎵")
# Solicita a cor de camisa
cor_camisa = input("Informe a cor da camisa:")

# Troca o presente de acordo com a cor da camisa
if(cor_camisa == "Branca"):
    presente = "Labubu"
elif(cor_camisa == "Verde"):
    presente = "Casa Barbie"
elif(cor_camisa == "Amarelo"):
    presente = "Pista da HotWheels (Do tubarão🦈)"
else:
    presente = "Um abraço (a distância)"

# Devolve a informação do presente
print("PARABÉNS, VOCÊ GANHOU:", presente)