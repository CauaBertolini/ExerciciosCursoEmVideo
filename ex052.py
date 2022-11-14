# faça um programa que leia um numero inteiro e diga se ele e ou nao um numero primo.
z = 0
n = int(input('\033[36mDigite um Numero: '))
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[34m', end='')
        z += 1
    else:
        print('\033[31m', end='')

    print('{} '.format(c), end='')
if z == 2:
    print('\n\033[35mE primo!', end=' ')
else:
    print('\n\033[35mNao e primo!', end=' ')
print('\033[35mPois {} e divisivel por {} numeros'.format(n, z))
