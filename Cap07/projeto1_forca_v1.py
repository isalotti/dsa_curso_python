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

def game():
    limpa_tela()

    print("\nBem-vindo(a) ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")

    #Lista de palavras para o jogo
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']

    #Escolher randomicamente
    palavra = random.choice(palavras)

    #List compehension
    letras_descobertas = ['_' for letra in palavra]

    #Num. de chances
    chances = 6

    # Lista para letras erradas
    letras_erradas = []

    # Testar as letras informadas:
    while chances > 0:

        print(" ".join(letras_descobertas))
        print("\nChances restantes:", chances)
        print("Letras erradas:", " ".join(letras_erradas))

        tentativa = input("\nDigite uma letra: ").lower() 

        if tentativa in palavra:
            index = 0

            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)

        if "_" not in letras_descobertas:
            print("\nVocê venceu! A palavra era:", palavra)
            break
    
    if "_" in letras_descobertas:
        print("\nVocê PERDEU! A palavra era:", palavra)
            
    
#Bloco main
if __name__ == "__main__":
    game()
    print("\nParabéns! Você jogou o jogo da forca.\n")