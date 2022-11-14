# Crie um programa que leia o quanto de dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar considerando 1.00 dolar = 3,27 reais
d = float(input('\033[33mDigite o quanto voce tem de dinheiro neste momento na sua carteira: \033[32;1mR$'))
print('\033[35mVoce pode comprar \033[34;1mUS${:.2f}'.format(d / 3.27))
