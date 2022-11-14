# Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou nao formar um triangulo
from time import sleep
print('\033[33;1m-=-'*8)
print('\033[36mAnalisador de Triangulos')
print('\033[33;1m-=-'*8)
a = float(input('\033[35mDigite o tamanho do primeiro segmento : '))
b = float(input('Digite o tamanho do segundo segmento: '))
c = float(input('Digite o tamanho do terceiro segmento: '))
print('\033[34mCalculando...')
sleep(6)
if a < (b + c) and b < (a + c) and c < (a + b):
    print('\033[32mSim! E possivel criar um triangulo com esses segmentos!')
else:
    print('\033[31mNao! Nao e possivel criar um triangulo com esses segmentos!')