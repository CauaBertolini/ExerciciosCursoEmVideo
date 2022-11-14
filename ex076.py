#Crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos preços, na sequencia.
#No final, mostre uma listagem de preços, organizando os dados de forma tabular.
cont = 0
produtos = ('Celular', 1800, 'Notebook', 8000, 'Headset', 250, 'Mouse', 150, 'Teclado', 125, 'Gabinet', 7000)
print('-=-' * 10 ,' Lista de Produtos ', '-=-' * 10)
for c in produtos:
    cont += 1
    if cont % 2 == 0:
        print(c)
    else:
        print(c, end='......................................................................')