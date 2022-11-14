# Faça um programa que tenha uma função chamada maior(), que receba vários
# parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep
def maior(* num):
    cont = 0
    maior = 0
    for n in num:
        print(f'{n} -> ', end='', flush=True)
        sleep(0.5)
        cont += 1
        if cont == 1:
            maior = n
        else:
            if n > maior:
                maior = n
    print('Fim!')
    print(f'Ao todo foram digitados \033[34m{cont}\033[m números, dentre eles, o maior foi {maior}', flush=True)
    sleep(1)

maior(3, 6, 7)
maior(1, 2, 3)
maior(99, 1)
maior()

print('FIZ ISSO SOZINHO MANO, SÓ ERREI PQ N SABIA USAR O DESEMPACOTAMENTO')