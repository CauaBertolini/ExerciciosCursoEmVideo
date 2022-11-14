#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogadro e quantos gols ele marcou.
#O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
def ficha(nome='<desconhecido>', gols=0):
    print('_'*40)
    print(f'O jogador {nome}, fez {gols} gol(s) no campeonato')


name = str(input('Nome: ')).strip()
gols = str(input('Quantidade de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if name.strip() == '':
    ficha(gols=gols)
else:
    ficha(name, gols)
