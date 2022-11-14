# Faça um programa que jogue par ou impar com o computador. O jogo sera interrompido quando o jogador perder. Mostrando o total de vitorias consecutivas que ele conquistou no final do jogo.
v = 0
import random
print('-=-'*30)
print('Jogo do Par ou Impar!')
print('-=-'*30)
while True:
    jogador = int(input('Digite um valor: '))
    computador = random.randint(0, 10)
    total = jogador + computador
    tipo = '1'
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()
    print(f'Voce jogou {jogador} e o computador jogou {computador}. Totalizando {total}.')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce venceu!')
            v += 1
        else:
            print('Voce perdeu!')
            break
    if tipo == 'I':
        if total % 2 != 0:
            print('Voce venceu!')
            v += 1
        else:
            print('Voce perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'Voce venceu {v} vezes ate perder.')