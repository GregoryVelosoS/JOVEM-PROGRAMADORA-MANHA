print("I'm glad you came...🎵")
# Solicita a cor de camisa
cor_camisa = input("Informe a cor da camisa:").upper()

# Troca o presente de acordo com a cor da camisa
match cor_camisa:
    case "BRANCO":
        presente = "Garrafinha Stan Lee"
    case "AMARELO":
        presente = "Disco de Vinil do RC"
    case "VERDE":
        presente = "Anão de Jardim"
    case _:
        presente = "NADA, VAI PRA CASA"
# Devolve a informação do presente
print("PARABÉNS, VOCÊ GANHOU:", presente)