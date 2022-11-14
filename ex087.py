# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# b) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
linha1 = list()
linha2 = list()
linha3 = list()
matriz = list()
cont = 0
pares = list()
print('-=-'*30)
for l1 in range(0, 3):
    n = int(input('Digite um numero: '))
    linha1.append(n)
    if n % 2 == 0:
        pares.append(n)
for l2 in range(0, 3):
    n = int(input('Digite um numero: '))
    linha2.append(n)
    if n % 2 == 0:
        pares.append(n)
for l3 in range(0, 3):
    n = int(input('Digite um numero: '))
    linha3.append(n)
    if n % 2 == 0:
        pares.append(n)
matriz.append(linha1[:])
matriz.append(linha2[:])
matriz.append(linha3[:])
print('-=-'*30)
for n in matriz[0]:
    cont += 1
    print(f'[ {n} ]', end='' if cont % 3 != 0 else '\n')
for n in matriz[1]:
    cont += 1
    print(f'[ {n} ]', end='' if cont % 3 != 0 else '\n')
for n in matriz[2]:
    cont += 1
    print(f'[ {n} ]', end='' if cont % 3 != 0 else '\n')
if matriz[0][1] < matriz[1][1] > matriz[2][1]:
    maior = matriz[1][1]
elif matriz[1][1] < matriz[0][1] > matriz[2][1]:
    maior = matriz[0][1]
elif matriz[1][1] < matriz[2][1] > matriz[0][1]:
    maior = matriz[2][1]
cont = 0
for n in pares:
    cont += 1
    if cont == 1:
        somapar = n
    else:
        somapar += n
soma = matriz[0][2] + matriz [1][2] + matriz [2][2]
print('-=-'*30)
print(f'A soma de todos os valores pares e igual a {somapar}.')
print(f'A soma dos valores da terceira coluna e igual a {soma}.')
print(f'O maior valor da segunda coluna e {maior}.')
print('-=-'*30)
