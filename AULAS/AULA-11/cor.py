# importação da bibliotecas
import time

# Colorama - biblioteca de cor 
from colorama import Fore, Back, Style

# Trocar cor do texto
print(Fore.RED + "Texto top, em vermelho")
print(Fore.GREEN + "Texto top, agora em verde")
print(Fore.BLUE + "Texto top, agora em AZUL")

# Resetar estilo
print(Style.RESET_ALL)

# Trocar a cor de fundo
print(Back.CYAN + "Fundo muito top, em ciano")
print(Back.MAGENTA + "Fundo muito top, em magenta")
print(Back.YELLOW + "Fundo muito top, em amarelo")

# Deixar mais melhor 
print(Style.RESET_ALL)
print(Style.BRIGHT)
print(Back.LIGHTGREEN_EX)
print(Fore.YELLOW + "Você passou, parabéns")
print(Style.RESET_ALL)


