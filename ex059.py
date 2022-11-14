# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] Soma
# [ 2 ] Multiplicar
# [ 3 ] Maior
# [ 4 ] Novos Numeros
# [ 5 ] Sair do Programa
# Sue programa devera realizar a operaçao solicitada em cada caso.
from time import sleep
print('\033[33m-=-'*20)
print('\033[32mBem vindo ao Number Helper!')
print('\033[33m-=-'*20)
escolha = 0
while escolha != 5:
    n1 = int(input('\033[34mDigite um valor: '))
    n2 = int(input('\033[34mDigite um segundo valor: '))
    print('\033[33m-=-'*20)
    print('\033[34mO que deseja fazer com {} e {}?'.format(n1,n2))
    print('\033[33m-=-'*20)
    print('''\033[35m[ 1 ] Soma
[ 2 ] Multiplicar
[ 3 ] Maior 
[ 4 ] Novos Numeros 
[ 5 ] Sair do Programa''')
    print('\033[33m-=-'*20)
    escolha = int(input('\033[34mDigite a opçao desejada: '))
    print('\033[33m-=-'*20)
    if escolha == 1:
        r = n1 + n2
        print('\033[36mA soma de {} e {} e igual a {}'.format(n1, n2, r))
    elif escolha == 2:
        r = n1 * n2
        print('\033[36mA multiplicaçao entre {} e {} e igual a {}'.format(n1, n2, r))
    elif escolha == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('\033[36mO numero maior e {}'.format(maior))
    elif escolha == 4:
        print('\033[34mNovos numeros? Ok, iremos recomeçar')
        sleep(2)
        print('\033[34nRecomeçando...')
    elif escolha == 5:
        print('\033[31mEntao acabou...')
    print('\033[33m-=-'*20)


