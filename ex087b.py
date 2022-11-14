# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# b) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = somacol = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um numero para [{l}, {c}]: '))
print('-=-' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^7}]', end='')
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
    print()
print('-=-'*30)
print(f'A soma dos valores pares digitados e igual a {somapar}')
for l in range(0, 3):
    somacol += matriz[l][2]
print(f'A soma dos numeros da terceira coluna resulta em {somacol}')
for c in range(0, 3):
    if c == 0 or matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha e {maior}')