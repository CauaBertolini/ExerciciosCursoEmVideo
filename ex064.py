# Crie um programa que leia Varios Numeros inteiros pelo teclado. O programa so vai parar quando o usuario digitar o valor 999. Que e a condiçao de parada. No final, mostre quantos numeros foram digitados e qual foi a soma entre eles.
# (desconsiderando o flag).
c = 0
n = 0
soma = 0
n = int(input('Digite um numero: (999 para parar) '))
while n != 999:
    c += 1
    soma += n
    n = int(input('Digite um numero: (999 para parar) '))
print('Voce digitou {} numeros e a soma de todos e igual a {}'.format(c, soma))
