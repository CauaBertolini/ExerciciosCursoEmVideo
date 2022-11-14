produtos = ('Celular', 1800,
            'Notebook', 8000,
            'Headset', 250,
            'Mouse', 150,
            'Teclado', 125,
            'Gabinet', 7000)
print('-=-' * 13)
print('             Produtos')
print('-=-' * 13)
for posiçao in range (0, len(produtos)):
    if posiçao % 2 == 0:
        print(f'{produtos[posiçao]:.<30}', end='')
    else:
        print(f'R${produtos[posiçao]:>8.2f}')
print('-=-' * 13)