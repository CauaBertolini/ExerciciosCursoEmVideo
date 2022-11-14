#Faça um programa que tenha uma função chamada notas() que pode receber várias notas de alunos e vai retornar um dicionário
#com as seguintes informações:

#Quantidade de notas
#A maior nota
#A menor nota
#A média da turma
#A situação (opcional)

#Adicione também as docstrings da função.
def notas(* num, situação=False):
    '''
     Dê uma lista de notas e o programa irá retornar uma tabela com a maior e a menor nota, a média das notas e ainda é possível
    escolher se quer ou não ver a situação da turma.
    :param num: digite uma lista de notas
    :param situação: vem como padrão o False, que representa um não, caso queira receber a situação da turma digite True
    :return: Uma tabela com a maior e menor nota, média da turma e ainda se for requisitado, a atual situação da turma.
    '''
    maior = menor = média = cont = tot = 0
    for n in num:
        cont += 1
        if cont == 1:
            maior = menor = n
        else:
            if n > maior:
                maior = n
            if n < menor:
                menor = n
        tot += n
    média = tot / cont
    print('-'*40)
    print(f'Resolução para a lista de notas {num}')
    print(f'''-> A MAIOR nota foi: {maior}
-> A MENOR nota foi: {menor}
-> A MÉDIA da turma foi: {média:.2f}''')
    if situação == True:
        print('-> A SITUAÇÃO da turma é: ', end='')
        if 6 < média < 7:
            print('Recuperação')
        elif média > 7:
            print('Aprovados!')
        elif média < 6:
            print('Reprovados!')


#Programa Principal:
#notas = list()
#while True:
#   notas.append(int(input('Digite uma nota: ')))
#   r = str(input('Deseja continuar? [S/N] '))
#   if r[0].upper().strip() in 'N':
#        break
#notas(notas)
notas(9.5, 6.7, 2.5, 8, 6, 7,  situação=True)

