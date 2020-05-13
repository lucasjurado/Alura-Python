import random

def jogar():
    apresentação()

    randomizar = carrega_txt(txt='palavras.txt')

    palavra_secreta = randomizar.lower()
    letras_acertadas = ['_' for letra in palavra_secreta]

    letras_erradas = []
    letras_certas = []

    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:

        chute = input(f'Escolha uma letra > {letras_acertadas}:  ').lower().strip()[0]
        if chute in palavra_secreta:
            if chute in letras_certas:
                print(f'A letra [{chute}] já foi informada!\n'
                      f'Tente novamente...')
                continue
            else:
                for pos, letra in enumerate(palavra_secreta):
                    if letra.lower() == chute:
                        letras_acertadas[pos] = letra
                msg_retorno('acerto')
                print('-' * 45)
            letras_certas.append(chute)
        else:
            if chute in letras_erradas:
                print(f'A letra [{chute}] já foi informada!\n'
                      f'Tente novamente...')
                continue
            else:
                erros+=1
                desenha_forca(erros)
                msg_retorno('erro')
                if chute not in letras_erradas:
                    letras_erradas.append(chute)
                print(f'Erros: {letras_erradas}')
                print(f'Faltam {7-erros} tentativas...')
                print('-' * 45)
                if erros == 7:
                    enforcou = True
        if '_' not in letras_acertadas:
            acertou = True

    if acertou:
        imprime_mensagem_vencedor(palavra_secreta)
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    print('-' * 45)
    print('*'*45)
    print(f'{"Fim do Jogo!":^45}')
    print('*' * 45)

def apresentação():
    print('\033[0;36m*******************************************')
    print('********\033[mBem vindo ao jogo da forca!\033[0;36m********')
    print('*******************************************\033[m')

def carrega_txt(txt = 'palavras.txt'):
    with open(txt,'w') as arquivo:
        arquivo.write('abacate\n'
                      'coco\n'
                      'abacaxi\n'
                      'açai\n'
                      'acerola\n'
                      'ameixa\n'
                      'banana\n'
                      'castanha\n'
                      'cranberry\n'
                      'damasco\n'
                      'framboesa\n'
                      'groselha\n'
                      'guarana\n'
                      'jabuticaba\n'
                      'kiwi\n'
                      'lichia\n'
                      'macadamia\n'
                      'pistache\n'
                      'tamarindo\n')

    with open('palavras.txt', 'r') as arquivo:
        palavras = []
        for linha in arquivo:
            palavras.append(linha.strip())
        randomizar = random.choice(palavras)
        return randomizar

def msg_retorno(msg):
    if msg == 'acerto':
        print('\033[0;32mxxxxxxxxxxxxxxxx')
        print('xxLetra certa!xx')
        print('xxxxxxxxxxxxxxxx\033[m')
    elif msg == 'erro':
        print('\033[0;31mxxxxxxxxxxxxxxxxx')
        print('xxLetra errada!xx')
        print('xxxxxxxxxxxxxxxxx\033[m')

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print(f'A palavra era: [{palavra_secreta}]')
    print("\033[0;31m    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           \033[m")

def imprime_mensagem_vencedor(palavra_secreta):
    print("Parabéns, você ganhou!")
    print(f'A palavra era: [{palavra_secreta}]')
    print("\033[0;35m       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       \033[m")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == '__main__'):
    jogar()
