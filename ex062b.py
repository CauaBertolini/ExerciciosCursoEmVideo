print('Gerador de PA do Caua')
print('-=-'*20)
termo = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos voce quer a mais? '))
print('Programa encerrado! {} termos foram mostrados.'.format(total))