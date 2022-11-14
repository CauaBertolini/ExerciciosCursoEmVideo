#Crie um programa onde 4 jogadores joguem um dado e tenham
#resultados aleatórios. Guarde esses resultados em um dicionário.
#No final, coloque esse dicionário em ordem, sabendo que o vencedor
#tirou o maior número no dado.
from random import randint
from time import sleep
from operator import itemgetter
pos1 = pos2 = pos3 = pos4 = ''
partida = dict()
print('-=-'*30)
print('Bem vindo ao Jogue o Dado!')
print('-=-'*30)
for c in range(1, 5):
    partida[f"Jogador {c}"] = randint(1, 6)
for i, v in partida.items():
    sleep(2)
    print(f'{i} tirou {v}')
sleep(2)
ranking = list()
ranking = sorted(partida.items(), key=itemgetter(1), reverse=True)
print('-=-'*30)
print('Rank')
print('-=-'*30)
for i, v in enumerate(ranking):
    print(f'{i+1}° Lugar: {v[0]} com {v[1]} ')
