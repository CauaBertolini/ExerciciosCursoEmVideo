# Crie um programa que leia varios numeros inteiros pelo teclado. No final da execuçao, mostre a media entre todos os valores e quais foram o maior e o menor valor lidos. O programa deve perguntar ao usuario se ele quer ou nao continuar a digitar valores.
c = 0
n = 0
soma = 0
r = 'S'
while r.upper() == 'S':
    n = int(input('\033[34mDigite um valor: '))
    soma += n
    c += 1
    if c == 1:
        maior = n
        menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
    r = str(input('\033[35mQuer continuar? S/N: ')).strip()[0]
media = soma / c
print('\033[36mVoce digitou {} valores e a media entre todos os numeros e {:.2f} o maior numero e {} e o menor numero e {}'.format(c, media, maior, menor))