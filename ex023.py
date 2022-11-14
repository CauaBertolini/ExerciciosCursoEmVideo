# Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados
# Ex.: 1834
# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1
'''n = str(input('Digite um numero de: '))
nd = n.split()
print('Analisando {} concluo que: '.format(n))
print('{} Unidade'.format(n[3]))
print('{} Dezena'.format(n[2]))
print('{} Centena'.format(n[1]))
print('{} Milhar'.format(n[0]))''' # Nao funciona, por isso faremos da forma matematica:
num = int(input('\033[34mDigite um numero de 0 a 9999: '))
u = num // 1 % 10 # Divindo extaxo por 1 e em seguida pegando o resto da divisao por 10 obtemos o valor unitario
d = num // 10 % 10 # Para dezena dividimos por 10
c = num // 100 % 10 # Centena 100
m = num // 1000 % 10 # E milhar 1000
print('\033[33m{} Unidade'.format(u))
print('{} Dezena'.format(d))
print('{} Centena'.format(c))
print('{} Milhar'.format(m))