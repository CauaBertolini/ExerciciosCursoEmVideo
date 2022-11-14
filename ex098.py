# Faça um programa que tenha uma função chamada contador(), que receba três
# parâmetros: início, fim e passo e realize a contagem.
# Seu programa tem que realizar três contagens através de função criada:
# A) De 1 até 10, de 1 em 1
# B) De 10 até 0, de 2 em 2
# C) Uma contagem personalizada.
from time import sleep
def contador(início, fim, passo):

    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1

    print('-=-' * 30)
    print(f'\033[34mContagem de {início} até {fim} de {passo} em {passo}\033[m')
    sleep(0.5)

    if início < fim:
        cont = início
        while cont <= fim:
            if cont % 2 == 0:
                print(f'\033[35m{cont} ', end='', flush=True)
                sleep(0.5)
                cont += passo
            else:
                print(f'\033[36m{cont} ', end='', flush=True)
                sleep(0.5)
                cont += passo
        print('\033[31mFim!\033[m')

    else:
        cont = início
        while cont >= fim:
            if cont % 2 == 0:
                print(f'\033[35m{cont} ', end='', flush=True)
                sleep(0.5)
                cont -= passo
            else:
                print(f'\033[36m{cont} ', end='', flush=True)
                sleep(0.5)
                cont -= passo
        print('\033[31mFim!\033[m')


#Programa Principal
contador(0, 10, 1)
contador(10, 0, 1)
print('-=-' * 30)
print('\033[34mAgora é sua vez de personalizar a contagem!')
i = int(input('\033[35mInício: '))
f = int(input('Fim: '))
p = int(input('Passo: \033[m'))
contador(i, f, p)