# Escreva um programa que leia dois numeros inteiros e compare-os. Mostrando na tela um mensagem:
# O primeiro valor e maior
# O segundo valor e maior
# Nao existe valor maior, os dois sao iguais.
n1 = int(input('\033[34mDigite um Numero: '))
n2 = int(input('Digite Outro Numero: '))
if n1 > n2:
    print('\033[36m{} e o numero maior!'.format(n1))
elif n2 > n1:
    print('\033[36m{} e o numero maior!'.format(n2))
elif n1 == n2:
    print('\033[33mNao ha numero maior pois os dois sao iguais!')
