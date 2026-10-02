# Cria as lista
lista_alunos =   ["Miguel", "Luana", "Sam"]
primeira_notas = [       7,       5,     9] 
segunda_notas  = [       2,      10,     7]
media =          []

# Crie um função que receba os dois valores de nota de um aluno e retorne sua média, após isso, informe a média junto com a mensagem final :)
def calcular_media(nota1, nota2):
    #Calcula a media atual do aluno
    media_final = (nota1 + nota2) / 2
    #Adiciona a media atual na lista de medias
    media.append(media_final)
    #retorna a media calculada
    return media_final

# Mostra o nome e a nota (JUNTOS)
for index in range(len(lista_alunos)):
    print(f"""O aluno(a) é {lista_alunos[index]} 
        e sua primeira nota foi: {primeira_notas[index]} 
        e sua segunda nota foi: {segunda_notas[index]}
        sua média foi: {calcular_media(primeira_notas[index],segunda_notas[index])} """)