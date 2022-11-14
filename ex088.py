# Faça um programa que ajude um jogador da MEGA SENA a criar palpites, O programa vai perguntar quantos
# jogos serão gerados e vai sortear 6 numeros entre 1 e 60 para cada jogo, cadastrando tudo em uma
# lista composta.
from random import randint
from time import sleep
numeros = list()
palpites = list()
cont = 0
print('-=-'*30)
print('Criador de Palpites para a Mega Sena')
print('-=-'*30)
quantidade = int(input('Quantos palpites você deseja? '))
print('-=-'*30)
print('Gerando palpites...')
sleep(quantidade)
print('-=-'*30)
for p in range(0, quantidade):
    cont = 0
    while cont < 6:
        n = (randint(1  , 60))
        if n not in numeros:
            cont += 1
            numeros.append(n)
    palpites.append(numeros[:])
    numeros.clear()
for p, pal in enumerate(palpites):
    palpites[p].sort()
    print(f'{p+1}° Palpite: ', pal)
    sleep(2)
print('-=-'*30)
