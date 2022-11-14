# Faça um programa que tenha uma função chamada escreva(), que receba
# um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
# EX.:
# escreva('Olá Mundo!')
# Saída:
# -------------
#  Olá, Mundo!
# -------------
def titulo(frase):
    tamanho = len(frase) + 4
    print('\033[31m|' * tamanho)
    print(f'  {frase}')
    print('\033[31m|' * tamanho)


frase = str(input('Digite uma Frase: '))
titulo(frase)