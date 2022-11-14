# Faça um programa que leia um numero inteiro e mostre seu antecessor e seu sucessor
n = int(input('\033[34mDigite um numero: '))
print('\033[35mSeu antecessor e {}'.format(n - 1), end=' ')
print('e seu sucessor e {}'.format(n + 1))
