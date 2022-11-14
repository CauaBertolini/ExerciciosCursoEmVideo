# Faça um programa que calcule a soma entre todos os numeros impares que sao multiplos de tres e que se encontram no intervalo de 1 ate 500
s = 0
contador = 0
for r in range(1, 501, 2):
    if r % 3 == 0:
        contador = contador + 1
        s = s + r
print('A soma dos {} numeros entre 1 e 500 impares divisiveis por 3 deu {}'.format(contador, s))
