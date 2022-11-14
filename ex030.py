# Crie um programa que leia um numero inteiro e mostre na tela se ele e Par ou Impar.
numero = int(input('\033[35mDigite um numero inteiro: '))
pi = numero % 2
if pi == 0:
    print('\033[31m{} e Par'.format(numero))
else:
    print('\033[34m{} e Impar'.format(numero))