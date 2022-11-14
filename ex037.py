# Escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual sera a base de conversao
# 1 para binario
# 2 para octal
# 3 para hexadecimal
num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversao:
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opçao = int(input('Digite a opçao escolhida: '))
if opçao == 1:
    print('{} convertido para BINARIO e igual a {}'.format(num, bin(num)[2:]))
elif opçao == 2:
    print('{} convertido para OCTAL e igual a {}'.format(num, oct(num)[2:]))
elif opçao == 3:
    print('{} convertido para HEXADECIMAL e igual a {}'.format(num, hex(num)[2:]))
else:
    print('Voce nao escolheu nenhuma opçao valida de conversao.')
