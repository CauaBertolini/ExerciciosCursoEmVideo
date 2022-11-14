# Faça um programa que leia tres numeros e mostre qual e o maior e qual e o menor.
import time
n1 = int(input('\033[35mPrimeiro Numero: '))
n2 = int(input('Segundo Numero: '))
n3 = int(input('Terceiro Numero: '))
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('\033[34;1mO menor valor foi definido...')
time.sleep(3)
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('\033[34;1mO maior valor foi definido...')
time.sleep(3)
print('\033[34;1mProcessando...')
time.sleep(4)
print('\033[33mO maior valor e {} e o menor e {}!'.format(maior, menor))

# Outra maneira seria definir o n1 como menor e maior e dpps usar esse metodo para verificar e substituir se necessario economizando assim um IF

