#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posiçao foi digitado o primeiro valor 3.
# C) Quais foram os numeros pares.
cont = 0
onde3 = -1
num1 = int(input('Digite um numero: '))
num2 = int(input('Digite um numero: '))
num3 = int(input('Digite um numero: '))
num4 = int(input('Digite um numero: '))
nums = (num1, num2, num3, num4)
vezes9 = nums.count(9)
onde3 = nums.index(3)
if vezes9 == 0:
    print('O valor 9 nao apareceu nenhuma vez')
else:
    print(f'O valor 9 apareceu {vezes9} vezes')
if onde3 == -1:
    print('O numero 3 nao apareceu em nenhuma posiçao')
else:
    print(f'O numero 3 apareceu na posiçao {onde3 + 1}')
print('Os numeros pares foram: ', end='')
while True:
    if nums[cont] % 2 == 0:
        print(nums[cont], end=', ')
    if cont == 3:
        break
    cont += 1
