# Escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos de uma SEQUENCIA FIBONACCI.
# Ex.:
# 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
print('-=-'*30)
print('Sequencia de FIBONACCI: ')
print('-=-'*30)
n = int(input('Quantos termos voce quer ver?  '))
t1 = 0
t2 = 1
cont = 3
print('{} -> {}'.format(t1, t2), end='')
while cont <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> Fim ')

