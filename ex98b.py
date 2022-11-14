# Faça um programa que tenha uma função chamada contador(), que receba três
# parâmetros: início, fim e passo e realize a contagem.
# Seu programa tem que realizar três contagens através de função criada:
# A) De 1 até 10, de 1 em 1
# B) De 10 até 0, de 2 em 2
# C) Uma contagem personalizada.
from time import sleep

def contador(Início, Fim, Passo):
    print('-=-'*30)
    print(f'Contagem de {Início} até {Fim} contando de {Passo} em {Passo}:')

    if Passo < 0:
        Passo *= -1
    if Passo == 0:
        Passo = 1

    if Fim > Início:
        cont = Início
        while cont <= Fim:
            print(f'{cont} ', end='', flush=True)
            sleep(1)
            cont += Passo
        print('Fim!')

    else:
        cont = Início
        while cont >= Fim:
            print(f'{cont} ', end='', flush=True)
            sleep(1)
            cont -= Passo
        print('Fim!')


contador(0, 10, 1)
contador(10, 0, 2)
print('-=-'*30)
print('Agora é sua vez de personalizar o contador: ')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)