import forca
import adivinhacao

def escolher_jogo():
    print('*******************************************')
    print('************Escolha o seu jogo!************')
    print('*******************************************')

    print('[1] Forca\n'
          '[2] Adivinhação')

    jogo = int(input('Qual jogo? '))

    if jogo == 1:
        forca.jogar()
    if jogo == 2:
        adivinhacao.jogar()

while True:
    if(__name__ == '__main__'):
        escolher_jogo()
    again = int(input('Quer voltar ao menu de jogos? [1]= sim / [2]= não :'))
    if again == 1:
        continue
    else:
        break