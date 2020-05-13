import random

def jogar():
    print('\033[0;36m*******************************************')
    print('*****\033[mBem vindo ao jogo de adivinhação!\033[0;36m*****')
    print('*******************************************\033[m\n')

    numero_secreto = random.randint(1,100)
    total_tentativa = 1
    pontos = 1000

    print('Qual o nível de dificuldade?')
    print('[1] Fácil: 20 tentativas.\n'
          '[2] Intermediário: 10 tentativas.\n'
          '[3] Difícil: 5 tentativas.\n')

    while True:
        nivel = int(input('Digite o nível do jogo: '))
        if nivel in (1,2,3):
            break
        else:
            print(f'\033[0;31m[{nivel}] não é um nível válido!\033[m\n'
                  f'Tente novamente...')

    print('-'*43)
    if nivel == 1:
        print('\033[0;36m> Nível Fácil\033[m')
    if nivel == 2:
        print('\033[0;36m> Nível Intermediário\033[m')
    if nivel == 3:
        print('\033[0;36m> Nível Dificil\033[m')
    print('-' * 43)

    if nivel == 1:
        tent = 20
    elif nivel == 2:
        tent = 10
    elif nivel == 3:
        tent = 5

    for i in range(1,tent+1):
        print(f'> Tentativa nº{total_tentativa}/{tent}')
        total_tentativa += 1
        chute = int(input('Digite um número entre 1 e 100: '))
        print(f'Você digitou o número {chute}.')

        if chute<1 or chute>100:
            print('Erro! Você deve digitar um número entre 1 e 100!')
            continue

        #variáveis para os testes
        acertou = numero_secreto == chute
        maior = numero_secreto > chute
        menor = numero_secreto < chute

        if acertou:
            print('-' * 43)
            print('\033[0;32mVocê acertou!\033[m')
            print('-' * 43)
            break
        else:
            if maior:
                print('-' * 43)
                print(f'O número secreto é [maior] que \033[0;36m{chute}\033[m')
            elif menor:
                print('-' * 43)
                print(f'O número secreto é [menor] que \033[0;36m{chute}\033[m')
            if nivel == 1:
                pontos_perdidos = abs(numero_secreto - chute)
            elif nivel == 2:
                pontos_perdidos = 5*abs(numero_secreto-chute)
            elif nivel == 3:
                pontos_perdidos = 10*abs(numero_secreto-chute)
            pontos -= pontos_perdidos

        print('-'*43)

    print(f'Pontuação final = {pontos}.\n'
          f'O número secreto era: {numero_secreto}.')
    print('*'*43)
    print('Fim do jogo!')

if(__name__ == '__main__'):
    jogar()