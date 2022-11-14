n = int(input('Digite um valor para ver seu fatorial: '))
c = n
f = 1
print('Calculando {}! ', end=''.format(n))
while c > 0:
    print('{}'.format(c), end='')
    print(' x 'if c > 1 else ' = ', end='')
    f = f * c
    c -= 1
print('{}'.format(f))
