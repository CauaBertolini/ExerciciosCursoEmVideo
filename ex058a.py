# Melhore o jogo do desafio ex028 onde o computador vai pensar em um numero entre 0 e 10. So que agora o jogador vai tentar advinhar ate acertar, mostrando no final quantos palpites foram necessarios para vencer.
from random import randint
from time import sleep
acertou = False
tentativas = 0
print('\033[33m-=-'*26)
print('\033[32mBem vindo ao Advinhe o Numero!')
print('\033[33m-=-'*26)
computador = randint(0, 10)
print('\033[35mEstou pensando em um numero entre 0 e 10, que numero voce acha que e?')
print('\033[33m-=-' * 26)
while not acertou:
    jogador = int(input('\033[34mDigite sua resposta: '))
    print('\033[33m-=-'*26)
    if jogador == computador:
        acertou = True
        print('\033[36mAcertou! O numero era mesmo {}'.format(computador))
        if tentativas == 0:
            print('\033[33m-=-' * 26)
            print('\033[36mVoce acertou de primeira!')
    elif jogador != computador:
        tentativas += 1
        if computador > jogador:
            print('\033[35mNao era bem esse numero! E mais...')
        elif computador < jogador:
            print('\033[35mNao era bem esse numero! E menos...')
        print('\033[33m-=-' * 26)
        print('\033[35mTente Novamente!')
    print('\033[33m-=-'*26)
print('\033[36mVoce tentou {} vezes ate acertar!'.format(tentativas))