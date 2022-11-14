# Desenvolva um programa que leia seis numeros INTEIROS e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o.
z = 0
for n in range(1, 7):
    n = int(input('\033[34mDigite o {}° Numero: '.format(n)))
    if n % 2 == 0:
        z += n
print('\033[35mA soma de todos os numeros pares e igual a {}'.format(z))
