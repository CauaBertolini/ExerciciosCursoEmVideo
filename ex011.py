# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria
# para pinta-la sabendo que cada litro de tinta, pinta uma area de 2m²
b = float(input('\033[34mLargura da parede: '))
a = float(input('\033[34mAltura da parede: '))
tq = b * a
print('\033[35mSua parede tem {:.2f} metros quadrados, portanto vai precisar de {:.2f}l de tinta'.format(tq, tq / 2.0))
