numeros = []
maior = menor = 0
for c in range(0, 5):
    numeros.append(int(input(f'Digite um numero na posiçao {c}: ')))
    if c == 0:
        maior = menor = numeros[c]
    else:
        if numeros[c] > maior:
            maior = numeros[c]
        if numeros[c] < menor:
            menor = numeros[c]
print('-=-' * 30)
print(f'Voce digitou os valores {numeros}')
print(f'O maior valor digitado foi {maior} nas posiçoes: ', end='')
for i, v in enumerate(numeros):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor} nas posiçoes: ', end='')
for i, v in enumerate(numeros):
    if v == menor:
        print(f'{i}...', end='')
print()
