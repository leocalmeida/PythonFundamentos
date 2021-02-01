# -*- coding: utf-8 -*-
# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

    # Método Construtor
    def __init__(self, word):
        self.word = word
        self.erros = []
        self.acertos = []
        self.contador = 0

    # Método para adivinhar a letra
    def guess(self, letter):
        if letter in self.word:
            self.acertos.append(letter)
        else:
            self.erros.append(letter)
            self.contador +=1   

    # Método para verificar se o jogo terminou
    def hangman_over(self):
        if self.contador==6:
            self.print_game_status()
            return True
        else:
            return False

    # Método para verificar se o jogador venceu
    def hangman_won(self):
        return None
        

    # Método para não mostrar a letra no board
    # def hide_word(self):

    # Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        print(board[self.contador])
        print('letras erradas: ',self.erros)
        print('letras corretas: ',self.acertos)
        print('contador:',self.contador)
        

    

# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("arquivos/palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()


# Função Main - Execução do Programa
def main():

    # Objeto
    game = Hangman(rand_word())

    # Enquanto o jogo não tiver terminado,
    # print do status,
    # solicita uma letra e faz a leitura do caracter

    while not game.hangman_over():
        game.print_game_status()
        game.guess(input('Digite uma letra: '))
    else:
    # De acordo com o status, imprime mensagem na tela para o usuário
        if game.hangman_won():
        	print ('\nParabéns! Você venceu!!')
        else:
        	print ('\nGame over! Você perdeu.')
        	print ('A palavra era ' + game.word)

    print ('\nFoi bom jogar com você! Agora vá estudar!\n')

        


    # Verifica o status do jogo
    # game.print_game_status()



# Executa o programa
if __name__ == "__main__":
    main()
