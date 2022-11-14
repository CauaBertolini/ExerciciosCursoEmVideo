# Faça um programa que leia o comprimento do cateto oposto e o do cateto adjacente de um triangulo retangulo. calcule e mostre o comprimeno da hipotenusa.
c1 = float(input('\033[32mDigite o valor de um dos catetos: '))
c2 = float(input('Digite o valor do outro cateto: '))
hi = ((c1 ** 2) + (c2 ** 2)) ** (1/2)
print('\033[34mA hipotenusa deste triangulo retangulo mede {:.2f}'.format(hi))
# Outra maneira de resolver e com uma funcionalidade do modulo Math
from math import hypot
co = float(input('\033[33mQual a medida do cateto oposto: '))
ca = float(input('Qual a medida do cateto adjascente: '))
hip = hypot(co, ca)
print('\033[34mA hipotenusa mede {:.2f}'.format(hip))
