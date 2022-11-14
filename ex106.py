#Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer.
#Quando o usuário digitar a palavra 'FIM', o programa se encerrará.

#OBS.: use utilidades.
from time import sleep
c = ('\033[m', #0 = Sem cor
       '\033[0;41m', #1 = Vermelho
       '\033[0;42m', #2 = Verde
       '\033[0;43m', #3 - Amarelo
       '\033[0;44m', #4 - Azul
       '\033[0;45m', #5 - Roxo
       '\033[0;46m', #6 - Verde Água
       '\033[7;1;37m', #7 - Branco
       )


def título(msg=str, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


def ajuda(funç=''):
    título(f'Acessando Biblioteca \'{bibliotecaOuFunção}\'', 4)
    print(c[7], end='')
    help(funç)
    print(c[0], end='')
    sleep(2)


while True:
    título('Sistema de Ajuda PyHelp', 2)
    bibliotecaOuFunção = (str(input('Biblioteca ou Função > ')))
    if bibliotecaOuFunção.upper() == 'FIM':
        break
    else:
        ajuda(bibliotecaOuFunção)
título('Até Logo', 1)



