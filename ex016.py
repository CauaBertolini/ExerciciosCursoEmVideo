# Crie um programa que leia um numero real inteiro qualquer pelo teclado e mostre na tela sua porçao inteira.
from math import trunc
nr = float(input('\033[35mDigite um numero real: '))
print('\033[36mA porçao inteira de {} e {}'.format(nr, trunc(nr)))
