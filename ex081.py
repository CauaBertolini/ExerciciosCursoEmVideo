#Crie um programa que vai ler varios numeros e colocar em uma lista.
#Depois disso, mostre:
# A) Quantos numeros foram digitados.
# B) A lista de valores, ordenada de forma decrescente
# C) Se o valor 5 foi digitado e esta ou nao na lista.
numeros = []
cont = 0
while True:
    print('-=-' * 25)
    numeros.append(int(input('Digite um numero: ')))
    print('Numero registrado! ')
    cont += 1
    print('-=-' * 25)
    r = (str(input('Deseja continuar? [S/N] '))).upper().strip()[0]
    if r in 'Nn':
        break
    while r not in 'NnSs':
        r = str(input('Nao entendi. Tente novamente. Deseja continuar? [S/N] ')).upper().strip()[0]
print('-=-' * 25)
numeros.sort(reverse=True)
print(f'Foram digitados {cont} numeros, a lista em ordem decrescente e {numeros}.', end='')
if 5 in numeros:
    print(' O valor 5 foi digitado e esta na lista')