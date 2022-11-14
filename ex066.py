# Crie um programa que leia varios numeros inteiros pelo teclado. O programa so vai parar quando o usuario digitar o valor 999, que e a condiçao de parada. No final, mostre quantos numeros foram digitados e qual foi a soma entre eles (desconsiderando o flag).
n = s = cont = 0
while True:
    n = int(input('Digite um numero (999 para parar): '))
    if n == 999:
        break
    s += n
    cont += 1
print(f'Voce digitou {cont} numeros e a soma entre todos eles e igual a {s}')