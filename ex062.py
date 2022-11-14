# Melhore o desafio ex061, perguntando para o usuario se ele quer mostrar mais alguns termos. O programa  encerra quando ele disser que quer mostrar 0 (nenhum) termos.
print('-=-'*20)
print('Gerador de PA 2.0')
print('-=-'*20)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(primeiro), end='')
        primeiro += razao
        cont += 1
    print('Pausa ')
    mais = int(input('Quantos termos voce quer a mais? '))
print('Progressao finalizada com {} termos mostrados'.format(total))