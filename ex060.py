# Faça um programa que leia um numero qualquer e mostre o seu fatorial.
# ex:
# 5! = 5x4x3x2x1 = 120
# Faça com WHILE e com o FOR
'''r = 1
n = int(input('\033[34mDigite um valor para ver seu fatorial: '))
print('O fatorial de {} e:'.format(n))
for c in range(n, 0, -1):
    print('\033[36m{} '.format(c), end='')
    r = c * r
print('= O resultado desse fatorial e \033[33m{}'.format(r))'''

r = 1
n = int(input('\033[34mDigite um valor para ver seu fatorial: '))
while n != 0:
    r = n * r
    n = n - 1
    print(n + 1, end=' ')
print('O resultado e {}'.format(r))