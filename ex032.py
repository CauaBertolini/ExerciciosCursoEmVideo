# Faça um prgrama que leia um ano qualquer e mostre se ele e Bissexto.
'''ano = int(input('Digite um ano: '))
if ano % 4 == 0:
    print('{} e bissexto!'.format(ano))
else:
    print('{} nao e bissexto! Anos bissextos ocorrem a cada quatro anos, e sempre sao multiplos de quatro.'.format(ano))'''
import datetime
ano = int(input('\033[35mDigite o ano que quer analisar, digite 0 para o ano atual: '))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('\033[34m{} e BISSEXTO!'.format(ano))
else:
    print('\033[31mO ano {} nao e BISSEXTO!'.format(ano))
