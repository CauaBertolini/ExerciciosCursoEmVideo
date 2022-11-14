#Crie um programa onde o usuario possa digitar varios valores numericos e cadastre-os em uma lista.
#Caso o numero ja exista la dentro, ele nao sera adicionado. No final, serao exibidos todos os valores unicos digitados, em ordem crescente.
numeros = []
print('-=-' * 22)
while True:
    n = int(input('Digite um numero: '))
    print('-=-' * 22)
    if n not in numeros:
        numeros.append(n)
        print('Numero registrado com sucesso!')
    elif n in numeros:
        print('O valor digitado ja existe, ele nao foi registrado.')
    print('-=-' * 22)
    r = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    if r in 'Nn':
        print('-=-' * 22)
        break
    print('-=-' * 22)
numeros.sort()
print(f'Os valores registrados em ordem crescente foram {numeros}')
print('-=-' * 22)