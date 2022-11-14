# Crie um programa que leia o nome e o preço de varios produtos. O programa devera perguntar se o usuario vai continuar. No final, mostre:
# A) Qual e o total de gasto na compra.
# B) Quantos produtos custam mais de RS1000
# C) Qual e o nome do produto mais barato.
from time import sleep
r = 's'
cont = total = caro = preçobarato = 0
barato = ''
print('\033[32m-=-'*30)
print('\033[33mLojao do Abreu')
print('\033[32m-=-'*30)
while True:
    cont += 1
    print(f'\033[35mProduto {cont}')
    print('\033[32m-=-' * 30)
    produto = str(input('\033[34mDigite o nome do produto: ')).strip()
    preço = float(input('\033[34mDigite o valor do produto: '))
    total += preço
    if preço > 1000:
        caro += 1
    if cont == 1:
        barato = produto
        preçobarato = preço
    elif preço < preçobarato:
        barato = produto
        preçobarato = preço
    print('\033[32m-=-' * 30)
    r = str(input('\033[36mDeseja continuar? [S/N] ')).strip()
    print('\033[32m-=-' * 30)
    if r[0] in 'Nn':
        print('\033[35mCalculando compra...')
        sleep(5)
        break
print(f'''\033[35mSuas compras aqui no Lojao do Abreu totalizaram no valor de R${total:2f} contando ao todo
com {cont} produtos. Desse total, {caro} produtos custam mais de R$1000. O produto mais barato foi o/a
{barato} custando R${preçobarato:.2f}''')
