#Crie um programa que gerencie o aproveitamento de um
#jogador de futebol. O programa vai ler o nome do jogador
#e quantas partidas ele jogou. Depois vai ler a quantidade de
#gols feitos em cada partida. No final, tudo isso será guardado
#em um dicionário, incluindo o total de gols feitos durante o
#campeonato.
jogador = dict()
partidas = list()
total = 0
print('-=-'*30)
jogador["nome"] = str(input('Nome do jogador: ').title().strip())
tot = int(input(f'Quantidade de partidas jogadas por {jogador["nome"]}: '))
print('-=-'*30)
if tot > 0:
    print('Gols Por Partida')
    print('-=-'*30)
    for jogo in range(0, tot):
        partidas.append(int(input(f'    Quantidade de gols na {jogo}° partida: ')))
        jogador['gols'] = partidas[:]
        jogador['total'] = sum(partidas)
    print('-=-'*30)
print(f'O jogador {jogador["nome"]} que jogou {tot} partidas\n'
      f'fez um total de {jogador["total"]} gols.')
print('-=-'*30)
for i, v in enumerate(jogador['gols']):
    print(f' => Na partida {i} fez {v} gols.')
print('-=-'*30)