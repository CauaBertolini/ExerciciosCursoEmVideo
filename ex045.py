# Crie um programa que faça o computador jogar Jokenpo com voce
import random
import time
print('\033[33m-=-'*30)
print('\033[32mBem Vindo ao Jogo de Jokenpo!')
print('\033[33m-=-'*30)
print('\033[35mEscolha Um:')
print('\033[33m-=-'*30)
print('''\033[34m[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
print('\033[33m-=-'*30)
n1 = 'Pedra'
n2 = 'Papel'
n3 = 'Tesoura'
lista = [n1, n2, n3]
escolha = int(input('\033[35mDigite sua escolha: '))
computador = random.choice(lista)
print('\033[33m-=-'*30)
print('\033[32mJO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!')
print('\033[33m-=-'*30)
if escolha == 1:# O Jogador escolheu Pedra
    if computador == n1:
        print('\033[34mEmpate! O computador tambem escolheu Pedra!')
    elif computador == n2:
        print('\033[31mPerdeu! O computador escolheu Papel!')
    elif computador == n3:
        print('\033[36mGanhou! O computador escolheu Tesoura!')
elif escolha == 2:# O Jogador escolheu Papel
    if computador == n1:
        print('\033[36mGanhou! O computador escolheu Pedra!')
    elif computador == n2:
        print('\033[34mEmpate! O computador tambem escolheu Papel!')
    elif computador == n3:
        print('\033[31mPerdeu! O computador escolheu Tesoura!')
elif escolha == 3:# O Jogador escolheu Tesoura
    if computador == n1:
        print('\033[31mPerdeu! O computador escolheu Pedra!')
    elif computador == n2:
        print('\033[36mGanhou! O computador escolheu Papel!')
    elif computador == n3:
        print('\033[34mEmpate! O computador tambem escolheu Tesoura!')
else:
    print('\033[31mVoce nao escolheu nenhuma opçao valida. Tente novamente!')
print('\033[33m-=-\033[31m'*30)
time.sleep(3)
# Outra meneira de sortear:
print('Mesma coisa programado de maneira diferente para teste')
itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0, 2)
print('''Suas Opçoes: 
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Digite sua escolha: '))
print('Computador jogou {} e Jogador {}'.format(itens[computador], itens[jogador])) # Ele escolhe um numero entre 0 e 2 entao esse numero vai para os colcehtes e se torna o valor da lista sorteado: Pedra[0] Papel[1] Tesoura[2]
