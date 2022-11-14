#Crie um programa que vai gerar cinco numeros aleatorios e colocar em uma TUPLA
#Depois disso, mostre a listagem de numeros gerados e tambem indique o menor e o maior numero que estao na tupla.
from random import randint
cont = 1
B = 0
nums = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
print('-=-' * 30)
print(nums)
print('-=-' * 30)
menor = maior = nums[0]
while True:
    cont += 1
    A = cont
    if cont == 1:
        maior = nums[0]
    if nums[A] > nums[B]:
        maior = nums[A]
        B = A
    if cont == 4:
        break
cont = 0
B = 0
while True:
    cont += 1
    A = cont
    if nums[A] < nums[B]:
        menor = nums[A]
        B = A
    if cont == 4:
        break
print(f'O maior valor e {maior} e o menor e {menor}')