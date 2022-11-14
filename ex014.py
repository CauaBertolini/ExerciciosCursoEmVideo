# Escreva um programa que converta uma temperatura digitada em C° e a converta para °F.
tc = float(input('\033[35mDigite uma temperatura em graus celsius: '))
tf = ((9 * tc) / 5) + 32
print('\033[34m{:.2f}C° convertido em fahrenheit equivale a {:.2f}°f'.format(tc, tf))
