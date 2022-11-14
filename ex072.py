# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extensao, de zero ate vinte.
# Seu programa devera ler um numero pelo teclado (entre 0 e 20) e mostra-lo por extenso.
numextenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    while num > 20 or num < 0:
        num = int(input('Tente novamente. Digite um numero entre 0 e 20: '))
    print(f'Voce digitou o numero {numextenso[num]}')
    print('-=-' * 30)
    r = str(input('Quer continuar? [S/N] ')).upper()
    while True:
        if r[0] not in 'SsNn':
            r = str(input('Tente novamente. Deseja continuer? [S/N] '))
        else:
            break
    if r[0] == 'N':
        break
