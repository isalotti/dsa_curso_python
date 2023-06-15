# Projeto 1 - Game em linguagem Python - Versão 1

#Import
import random
from os import system, name

# Função para limpar a tela a cada execução
def limpa_tela():
    #Windows
    if name == 'nt':   # Nome do sistema, não importa a versão
        _ = system('cls')   # O _ é utilizado quando não interessa mostrar o valor retornado pela função. Ela vai executa e o retorno é descartado.
    #Mac / Linux
    else:
        _ = system('clear')

def display_hangman(chances):
    stages = [
        # estágio 6
    """
        ------
        |    |
        |    O
        |  --|--
        |    |
        |   / \\
        |
    ------------
    """, 
    # estágio 5
    """
        ------
        |    |
        |    O
        |  --|
        |    |
        |   / \\
        |
    ------------
    """, 
    # estágio 4
    """
        ------
        |    |
        |    O
        |    |
        |    |
        |   / \\
        |
    ------------
    """ ,
    # estágio 3
    """
        ------
        |    |
        |    O
        |    |
        |    |
        |   /
        |
    ------------
    """,
    # estágio 2 
    """
        ------
        |    |
        |    O
        |    |
        |    |
        |
        |
    ------------
    """,
    # estágio 1
    """
        ------
        |    |
        |    O
        |
        |
        |
        |
    ------------
    """, 
    # estágio 0
    """
        ------
        |    |
        |
        |
        |
        |
        |
    ------------
    """]
    return stages[chances]

def game():
    limpa_tela()

    print("\nBem-vindo(a) ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")

    #Lista de palavras para o jogo
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']

    #Escolher randomicamente
    palavra = random.choice(palavras)

    lista_letras_palavras = [letra for letra in palavra]

    # Cria tabuleiro com caracteres _ multiplicando pelo comprimento da palavra
    tabuleiro = ["_"] * len(palavra)

    #List compehension
    letras_descobertas = ['_' for letra in palavra]

    #Num. de chances
    chances = 6

    letras_tentativas = []

    # Testar as letras informadas:
    while chances > 0:

        print(display_hangman(chances))
        print("\nPalavra: ", tabuleiro)
        print("\n")

        tentativa = input("\nDigite uma letra: ").lower() 

        if tentativa in letras_tentativas:
            print("Você já tentou essa letra. Escolha outra!")
            continue

        letras_tentativas.append(tentativa)

        if tentativa in lista_letras_palavras:
            
            print("Você acertou a letra!")

            for indice in range(len(lista_letras_palavras)):
                if lista_letras_palavras[indice] == tentativa:
                    tabuleiro[indice] = tentativa

            if "_" not in tabuleiro:
                print("\nVocê venceu! A palavra era: {}".format(palavra))
                break

        else:
            print("Ops... Essa letra não está na palavra!")
            chances -= 1

        continua_jogo = input("\nDeseja prosseguir (s/n)? ").lower()
        if continua_jogo == 'n':
            break
    
    if chances > 0:
        print("\nVocê DESISTIU! A palavra era: {}".format(palavra))
        return

    if "_" in letras_descobertas:
        print(display_hangman(chances))
        print("\nVocê PERDEU! A palavra era: {}".format(palavra))
            
    
#Bloco main
if __name__ == "__main__":
    game()
    print("\nParabéns! Você jogou o jogo da forca.\n")