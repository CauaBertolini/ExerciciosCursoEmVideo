# Faça um programa que mostre a tabuada de varios numeros, um de cada vez, para cada valor digitado pelo usuario. O programa sera interrompido quando o numero solicitado for negativo.
n = 0
m = 1
print('\033[36m-=-'*25)
print('\033[32mBem vindo a Tabuada Automatica!')
print('\033[36m-=-'*25)
while True:
    n = int(input('\033[34mDigite um numero para ver sua tabuada (numero negativo para parar): '))
    m = 1
    print('\033[36m-=-' * 25)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'\033[35m{n} X {m} = {n*m}')
        m += 1
    print('\033[36m-=-' * 25)