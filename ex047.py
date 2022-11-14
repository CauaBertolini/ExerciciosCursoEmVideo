# Crie um programa que mostre na tela todos os numeros pares que estao no intervalo entre 1 e 50.
for n in range(2, 51, 2):
    if n % 2 == 0:
        print(n, end=' ')
