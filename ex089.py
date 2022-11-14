# Crie um programa que leia nome e duas notas de varios alunos e guarde tudo em uma
# lista composta. No final, mostre um boletin contendo a media de cada um e permita
# que o usuario possa mostrar as nostas de cada aluno individualmente.
ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if r[0] not in 'SN':
        r = str(input('Não entendi! Tente novamente. Quer continuar? [S/N] ')).upper().strip()[0]
    elif r[0] in 'N':
        break
print('-=-'*30)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('-=-'*30)
for i, dado in enumerate(ficha):
    print(f'{i:<4}{dado[0]:<10}{dado[2]:>8}')
while True:
    print('-=-' * 30)
    escolha = int(input('Deseja ver as notas de qual aluno? [999 para parar] '))
    if escolha == 999:
        print('Finalizando...')
        break
    elif escolha <= len(ficha) - 1:
        print(f'As notas de {ficha[escolha][0]} são {ficha[escolha][1]}')
print(f'{"Volte Sempre":^30}')