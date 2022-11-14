# Crie um programa onde o usuario possa digitar sete valores numericos e
# cadastre-os em uma lista unica que mantenha separados os valores pares e impares.
# No final, mostre os valores pares e impares em ordem crescente.
todosnumeros = list()
numerospares = list()
numerosimpares = list()
numero = list()
for c in range(1, 8):
    print(f'{c}° valor')
    numero.append(int(input(('Digite um Numero: '))))
    if numero[0] % 2 == 0:
        numerospares.append(numero[:])
    else:
        numerosimpares.append(numero[:])
    numero.clear()
todosnumeros.append(numerospares[:])
todosnumeros.append(numerosimpares[:])
todosnumeros[0].sort()
todosnumeros[1].sort()
print(f'Os numeros pares digitados sao: {todosnumeros[0]}')
print(f'Os numeros inpares digitados sao: {todosnumeros[1]}')