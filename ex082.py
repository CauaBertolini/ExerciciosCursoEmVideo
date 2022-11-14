#Crie um programa que vai ler varios numeros e colocar em uma lista.
#Depois disso, crie duas listas extras que vao conter apenas os valores pares e os valores impares digitados, respectivamente.
#Ao final, mostre o conteudo das tres listas geradas.
numeros = []
numerospares = []
numerosimpares = []
while True:
    print('-=-'*30)
    numeros.append(int(input('Digite um numero: ')))
    print('-=-'*30)
    print('Numero Registrado!')
    print('-=-'*30)
    r = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if r in 'Nn':
        break
    while r not in 'SsNn':
        print('-=-' * 30)
        r = str(input('Nao entendi. Tente novamente. Deseja continuar? [S/N] ')).strip().upper()[0]
        if r in 'Nn':
            break
for n in numeros:
    if n % 2 == 0:
        numerospares.append(n)
    else:
        numerosimpares.append(n)
print('-=-'*30)
print(f'Os valores digitados foram {numeros}')
print(f'Os valores pares digitados foram {numerospares}')
print(f'Os valores impares digitados foram {numerosimpares}')
print('-=-'*30)