#Aprimore o DESAFIO 093 para que ele funcione com
#vários jogadores, incluindo um sistema de visualização
#de detalhes do aproveitamento de cada jogador.
jogador = dict()
partidas = list()
jogadores = list()
total = 0
print('-=-'*30)
while True:
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
        jogadores.append(jogador.copy())
        partidas.clear()
        print('-=-'*30)
    print('-=-' * 30)
    r = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while r not in 'SN':
        r = str(input('Não entendi, tente novamente. Deseja continuar? [S/N] ')).upper().strip()[0]
    if r in 'N':
        break
print('-=-'*30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-=-'*30)
for k, v in enumerate(jogadores):
    print(f'{k:<3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=-'*30)
while True:
    busca = int(input('Deseja ver os dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca > len(jogadores):
        print('ERRO! Não existe jogador neste número.')
    else:
        print(f'Levantamento do jogador {jogadores[busca]["nome"]}')
        for i, g in enumerate(jogadores[busca]['gols']):
            print(f' => Na partida {i} fez {g} gols.')
    print('-=-'*30)