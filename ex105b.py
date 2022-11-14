#Faça um programa que tenha uma função chamada notas() que pode receber várias notas de alunos e vai retornar um dicionário
#com as seguintes informações:

#Quantidade de notas
#A maior nota
#A menor nota
#A média da turma
#A situação (opcional)

#Adicione também as docstrings da função.
def notas(* num, situação=False):
    """
     Dê uma lista de notas e o programa irá retornar uma tabela com a maior e a menor nota, a média das notas e ainda é possível
    escolher se quer ou não ver a situação da turma.
    :param num: Digite uma lista de notas.
    :param Situação: vem como padrão o False, que representa um não, caso queira receber a situação da turma digite True.
    :return: Uma tabela com a maior e menor nota, média da turma e ainda se for requisitado, a atual situação da turma.
    """
    r = dict()
    r['Total'] = len(num)
    r['Maior'] = max(num)
    r['Menor'] = min(num)
    r['Média'] = sum(num)/len(num)
    if situação:
        if 6 < r['Média'] <= 7:
            r['Situação'] = 'Recuperação'
        elif r['Média'] > 7:
            r['Situação'] = 'Aprovados!'
        elif r['Média'] < 6:
            r['Situação'] = 'Reprovados!'
    return r


turmas = []
resp = notas(9, 9, 9, situação=True)
print(resp)
turmas.append(resp)

resp = notas(10, 10, 10, 10, situação=True)
print(resp)
turmas.append(resp)

for t in turmas:
    print(f'A turma teve como média a nota {t["Média"]}')