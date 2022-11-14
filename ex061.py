# Refaça o desafio ex051, lendo o primeiro termo de uma razao de uma PA, mostrando os 10 primeiros termos da progressao usando a estrutura while.
print('Gerador de PA')
print('-=-'*20)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{}'.format(termo), end='')
    print(' -> ' if cont < 10 else ' Fim. ', end='')
    termo += razao
    cont += 1