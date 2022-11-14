# Crie um programa onde o usuario possa digitar sete valores numericos e
# cadastre-os em uma lista unica que mantenha separados os valores pares e impares.
# No final, mostre os valores pares e impares em ordem crescente.
numeros = [[], []]
for c in range(1, 8):
    numero = int(input(f'Digite o {c}° valor: '))
    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)
print('-=-' * 30)
numeros[0].sort()
numeros[1].sort()
print(f'Os numeros pares sao: {numeros[0]}')
print(f'Os numeros impares sao: {numeros[1]}')