# Desenvolva um programa que leia as duas notas de um aluno, calcule e a sua media
import math
pn = float(input('\033[35mDigite a primeira nota: '))
sn = float(input('Digite a segunda nota: '))
m = ((pn + sn)/2)
print('\033[33mA media desse aluno e {}'.format(m))
print('\033[36mAplicando o areedondamento a media desse aluno sera {}'.format(math.ceil(m)))


