# Crie um programa que crie uma matriz de dimensao 3X3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com o a formataçao correta.
linha1 = list()
linha2 = list()
linha3 = list()
matriz = list()
cont = 0
print('-=-'*30)
for l1 in range(0, 3):
    linha1.append(int(input('Digite um numero: ')))
for l2 in range(0, 3):
    linha2.append(int(input('Digite um numero: ')))
for l3 in range(0, 3):
    linha3.append(int(input('Digite um numero: ')))
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
print('-=-'*30)
