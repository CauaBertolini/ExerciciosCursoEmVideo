# Faça um programa que tenha uma lista chamada números e duas funções
# chamadas sorteia() e somapar(). A primeira função vai sortear 5 números e vai colocá-los
# dentro da lista e a segunda função vai mostrar a soma entre todos os valores
# pares sorteados pela função anterior.
import random
import time


def sorteia(lista):
    print(f'Sorteando 5 valores: ')
    for c in range(0, 5):
        n = (random.randint(1, 10))
        lista.append(n)
        time.sleep(1)
        print(f'{n} ', end='', flush=True)
    print('Pronto!')


def somapar(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f'A soma dos valores pares da lista {lista}, é igual a {soma}')


números = list()
sorteia(números)
somapar(números)