# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço. com 5% de desconto
p = float(input('\033[32mDigite o preço do produto: \033[35mR$'))
pc = p * 5 / 100
print('\033[34mEste preço com \033[33m5%\033[34m de desconto e {} reais'.format(p - pc))
