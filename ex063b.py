# Escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos de uma SEQUENCIA FIBONACCI.
n = int(input('Digite um numero para ver sua fibonacci: '))
t1 = 0
t2 = 1
count = 3
print('{} -> {}'.format(t1, t2), end='')
while count <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end=' ')
    t1 = t2
    t2 = t3
    count += 1