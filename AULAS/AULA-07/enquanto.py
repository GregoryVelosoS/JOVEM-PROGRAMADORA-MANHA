# Laço de repetição - repete um trecho de código
# while = enquanto uma condição for verdadeira
# while(condição)
# Dentro do while, precisa ter algo para finalizar a repetição
# se não tiver, ele fica infinito

escolha = ""

while(escolha != 2):
    nomeTop = input("Digite um nome de um famoso top:")
    print(f"O {nomeTop} é top")
    print()
    escolha = input("Deseja continuar (1 - Sim/ 2 - Não)?:")