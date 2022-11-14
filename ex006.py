# Crie um algoritmo que leia um numero e mostre seu dobro seu triplo e sua raiz quadrada.
n = int(input('\033[34mDigite um numero: '))
print('\033[35mO dobro desse numero e {} o triplo e {}'.format((n*2), (n*3), end=' '))
print('e sua raiz quadrada e {:.3f}'.format((n**(1/2))))

