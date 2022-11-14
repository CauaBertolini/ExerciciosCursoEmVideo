#Faça um programa que leia 5 valores numeros e gurade-os em uma lista.
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posiçoes na lista.
cont = 0
maior2 = menor2 = 0
print('-=-'*22)
numeros = [(int(input('Digite um numero na posicao 0: '))),
           (int(input('Digite um numero na posicao 1: '))),
           (int(input('Digite um numero na posicao 2: '))),
           (int(input('Digite um numero na posicao 3: '))),
           (int(input('Digite um numero na posicao 4: ')))]
print('-=-'*22)
for p, n in enumerate(numeros):
    cont += 1
    if cont == 1:
        maior = n
        menor = n
        posmenor = p
        posmaior = p
    if n > maior:
        maior = n
        posmaior = p
    if n < menor:
        menor = n
        posmenor = p
print(f'Voce digitou os valores {numeros}')
print('-=-' * 22)
print(f'O maior valor digitado foi {maior} que esta na {posmaior + 1}° posiçao \n'
      f'enquanto o menor valor digitado foi o {menor} que esta na {posmenor + 1}° posiçao.')
print('-=-'*22)
