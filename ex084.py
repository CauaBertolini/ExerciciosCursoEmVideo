# Faça um programa que leia um nome e peso de varias pessoas, guardando tudo em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
pessoas = list()
pessoa = list()
pesados = list()
leves = list()
cont = 0
print('-=-'*30)
while True:
    pessoa.append(str(input('Nome: ').title()))
    pessoa.append(float(input('Peso: ')))
    print('-=-'*30)
    pessoas.append(pessoa[:])
    cont += 1
    if cont == 1:
        maior = menor = pessoa[1]
    else:
        if pessoa[1] > maior:
            maior = pessoa[1]
        if pessoa[1] < menor:
            menor = pessoa[1]
    pessoa.clear()
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while r not in 'SN':
        r = str(input('Nao entendi! Tente novamente. Quer continuar? [S/N] ')).upper().strip()[0]
    print('-=-'*30)
    if r in 'Nn':
        break
print(f'Foram registradas um total de {len(pessoas)} pessoas.')
print(f'As pessoas mais pesadas pesaram {maior}Kg. Peso de: ', end='')
for p in pessoas:
    if p[1] == maior:
        print(p[0], end=' ')
print()
print(f'As pessoas mais leves pesaram {menor}Kg. Sao elas: ', end='')
for p in pessoas:
    if p[1] == menor:
        print(p[0], end=' ')
print()
