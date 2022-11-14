# Refaça o exercicio 9 mostrando a tabuada de um numero escolhido pelo o usuario escolher, so que agora utilizando o laço for.
print('\033[33m-=-'*20)
n = int(input('\033[34mDigite um numero inteiro para ver sua tabuada: '))
print('\033[33m-=-\033[35m'*20)
for t in range(1, 11):
    print('{} X {:2} = {}'.format(n, t, t*n))
print('\033[33m-=-'*20)