#Faça um programa que leia nome e média de um aluno,
#guardando também a situação em um dicionário. No final,
#mostre o conteúdo da estrutura na tela.
from time import sleep
aluno = dict()
print('-=-'*30)
aluno['nome'] = str(input('Digite seu nome: ')).strip().title()
aluno['media'] = float(input('Digite sua média: '))
if aluno["media"] >= 7:
    aluno['situaçao'] = 'aprovado!'
elif 7 > aluno["media"] > 6:
    aluno['situaçao'] = 'ficar de recuperação!'
else:
    aluno['situaçao'] = 'reprovado!'
print('-=-'*30)
sleep(2)
print('Calculando...')
sleep(3)
print('-=-'*30)
print(f'A situação do {aluno["nome"]} é {aluno["situaçao"]}')
print('-=-'*30)
