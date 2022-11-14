# Faça um programa que tenha uma função chamada área(), que receba dimensões de um terreno retangular
# (largura e comprimento) e mostre a área do terreno.
def area(A, B):
    Area = A * B
    print(Area)


print('-=-'*30)
a = float(input('Altura: (m) '))
b = float(input('Comprimento: (m) '))
print('-=-'*30)
print(f'A Área correspondente a essas dimensões é ', end='')
area(a, b)
print('-=-'*30)
