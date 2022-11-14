# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhiido
import random
a1 = input('\033[34mPrimeiro aluno: ')
a2 = input('\033[35mSegundo aluno: ')
a3 = input('\033[33mTerceiro aluno: ')
a4 = input('\033[36mQuarto aluno: ')
lista = [a1, a2, a3, a4]
print('\033[30mO aluno sorteado foi {}'.format(random.choice(lista)))
