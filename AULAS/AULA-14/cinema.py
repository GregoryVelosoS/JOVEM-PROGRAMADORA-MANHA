# Senemma🤌 - Top+

# Importação das bibliotecas
import os
import time

# Funções auxiliares
def esperar(segundos):
    time.sleep(segundos)

def limparTela():
    os.system("cls" if os.name == "nt" else "clear") 

# Variáveis do usuário
nome = ""
idade = 0

# Função de cadastro do usuário
def cadastrar_usuario():
    global nome, idade
    
    limparTela()

    # Solicita as informações ao usuário
    nome = input("Informe seu nome:")
    idade = int(input("Informe sua idade:"))

# Função de saudação
def bem_vindo():
    limparTela()

    print("-------------------------------------------")
    print("---- 🎟️📽️ BEM VINDO AO SENEMMA 🎟️📽️ -----")
    print("-------------------------------------------")
    print(f"Usuário: {nome}")
    print(f"Idade: {idade}")
    print()

# Listas de filmes
filmesKids = [ "Galinha Pintadinha: O filme", "Turma da Mônica: O filme"]
filmesTeen = [ "Jogos Vorazes", "Crepúsculo"]
filmesAdultos = [ "Pânico 7", "Resident Evil" ]

# Funções para mostrar filmes
def ver_filmes_Kids():
    print(" ======= FILMES PARA CRIANÇAS ====== ")
    # Repetição pra mostrar todos os filmes
    for filme in range(len(filmesKids)):
        print(filme + 1, " - ", filmesKids[filme])

    print()

def ver_filmes_Teens():
    print(" ======= FILMES PARA TEENS ====== ")
    # Repetição pra mostrar todos os filmes
    for filme in range(len(filmesTeen)):
        print(filme + 3, " - ", filmesTeen[filme])

    print()

def ver_filmes_Adultos():
    print(" ======= FILMES PARA ADULTOS ====== ")
    # Repetição pra mostrar todos os filmes
    for filme in range(len(filmesAdultos)):
        print(filme + 5, " - ", filmesAdultos[filme])

    print()

# Função para mostrar filmes de acordo com a idade do usuário
def ver_filmes():
    limparTela()

    print(" ======== FILMES DISPONÍVEIS ============= ")
    print()

    # Chama funções, de acordo com a idade do usuário 
    if idade < 11:
        ver_filmes_Kids()
    elif idade < 18:
        ver_filmes_Kids()
        ver_filmes_Teens()
    else:
        ver_filmes_Kids()
        ver_filmes_Teens()     
        ver_filmes_Adultos()

# CRIANDO AS SALAS DE CINEMA
sala1 = [ 
         ["O","O","O","O","O"], 
         ["O","O","O","O","O"], 
         ["O","O","O","O","O"], 
         ["O","O","O","O","O"] 
        ]
sala2 = [ ["O","O","O","O","O"], ["O","O","O","O","O"], ["O","O","O","O","O"], ["O","O","O","O","O"] ]

# MOSTRAR CADEIRAS
def mostrarCadeiras(sala):
    print()
    print("========== POLTRONAS ==========")
    print()

    print("    0  1  2  3  4")

    for fileira in range(len(sala)):
        print (fileira, end=(" | "))
        for poltrona in range(5):
            print(sala[fileira][poltrona], end="  ")
        print()
    print()
    print("O = Livre")
    print("X = Ocupado")
    print()

# ÁREA DE COMPRAR INGRESSO
def escolherFilme():
    ver_filmes()

    escolha = int( input("Escolha o filme (Apenas números):"))

    filmeEscolhido = ""

    # Só deixa ele escolher, se estiver na faixa dele
    if idade < 11:
        if escolha == 1:
            filmeEscolhido = filmesKids[0]
        elif escolha == 2:
            filmeEscolhido = filmesKids[1]
        else:
            print("FILME INVÁLIDO PARA SUA IDADE")
            esperar(3)
            return None
    #Se a idade for de adolescente
    elif idade < 18:
        if escolha == 1:
            filmeEscolhido = filmesKids[0]
        elif escolha == 2:
            filmeEscolhido = filmesKids[1]
        elif escolha == 3:
            filmeEscolhido = filmesTeen[0]
        elif escolha == 4:
            filmeEscolhido = filmesTeen[1]
        else:
            print("FILME INVÁLIDO PARA SUA IDADE")
            esperar(3)
            return None
    # Se a idade for adulto
    else:
        if escolha == 1:
            filmeEscolhido = filmesKids[0]
        elif escolha == 2:
            filmeEscolhido = filmesKids[1]
        elif escolha == 3:
            filmeEscolhido = filmesTeen[0]
        elif escolha == 4:
            filmeEscolhido = filmesTeen[1]
        elif escolha == 5:
            filmeEscolhido = filmesAdultos[0]
        elif escolha == 6:
            filmeEscolhido = filmesAdultos[1]
        else:
            print("FILME INVÁLIDO")
            esperar(3)
            return None

    print(f'Filme escolhido: {filmeEscolhido}')
    esperar(3)
    return filmeEscolhido

# ESCOLHER A SALA
def escolherSala():
    limparTela()
    print(" =========== SALAS ===========")
    print("1 - Sala 1")
    print("2 - Sala 2")
    print()
    escolhaSala = int(input("Escolha qual sala deseja (Apenas números):"))
    if escolhaSala == 1:
        return sala1
    elif escolhaSala == 2:
        return sala2
    else:
        print("SALA INVÁLIDA !!!!!")
        esperar(2)
        return None

# RESERVAR CADEIRA
def reservarCadeira(sala):
    mostrarCadeiras(sala)

    #Escolhe o lugar
    fileiraEscolhida = int(input("Digite o número da fileira escolhida:"))
    poltronaEscolhida = int(input("Digite a poltrona escolhida:"))

    #Verifica a validade das escolhas
    #Verifica a fileira
    if fileiraEscolhida < 0 or fileiraEscolhida >= 4:
        print("FILEIRA INVÁLIDA")
        return

    #Verifica a poltrona
    if poltronaEscolhida < 0 or poltronaEscolhida >=5:
        print("POLTRONA INVÁLIDA")
        return
    # Fazer a reserva
    if sala[fileiraEscolhida][poltronaEscolhida] != "X":
        # Troco o valor da poltrona
        sala[fileiraEscolhida][poltronaEscolhida] = "X"
        print()
        print("Reserva feita com sucesso :)")
        print(f"Fileira: {fileiraEscolhida} e poltrona {poltronaEscolhida}")
        esperar(5)
    #Porém, se estiver ocupada....
    else:
        print()
        print("ESTA CADEIRA ESTÁ OCUPATION")
        esperar(5)        
    
def comprarIngresso():
    # Escolher o filme 
    filme = escolherFilme()
    if filme == None:
        return
    # Escolher a Sala de cinema 
    sala = escolherSala()
    if sala == None:
        return
    # Escolher a cadeira
    limparTela()
    print(f"Filme: {filme}")
    reservarCadeira(sala)

# ANTES DO MENU PRINCIPAL

# MENU PRINCIPAL
def mostrarMenu():
    bem_vindo()

    print("1 - VER FILMES")
    print("2 - COMPRAR INGRESSOS")
    print("3 - VER CADEIRAS NA SALA 1")
    print("4 - VER CADEIRAS NA SALA 2")
    print("0 - SAIR")
    print()

def menu():
    while True:
        mostrarMenu()
        opcaoEscolhida = int(input("Escolha uma opção:"))
        match opcaoEscolhida:
            case 1:
                ver_filmes()
                input("Pressione qualquer tecla para continuar....")
            case 2:
                comprarIngresso()
            case 3:
                limparTela()
                print(" ============ SALA 1 ==============")
                mostrarCadeiras(sala1)
                input("Pressione qualquer tecla para continuar....")
            case 4:
                limparTela()
                print(" ============ SALA 2 ==============")
                mostrarCadeiras(sala2)
                input("Pressione qualquer tecla para continuar....")
            case 0:
                print()
                print("Encerrando o sistema .......")
                esperar(3)
                print("Agradecemos por utilizar o Senemma Top+")
                break

            case _:
                print("OPÇÃO INVÁLIDA :(")

                esperar(3)

# PROGRAMA PRINCIPAL
cadastrar_usuario()
bem_vindo()
esperar(3)
menu()