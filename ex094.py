#Crie um programa que leia nome, sexo e idade de várias
#pessoas, guardando os dados de cada pessoa em um dicionário
#e todos os dicionários em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) A média de idade do grupo.
#C) Uma lista com todas as mulheres.
#D) Uma lista com todas as pessoas com idade acima da média.
pessoas = list()
dados = dict()
tot = totmulher = totmaior = totidade = 0
print('-=-' * 30)
while True:
    dados['nome'] = str(input('Nome: ')).title().strip()
    dados['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
    while dados['sexo'] not in "MF":
        dados['sexo'] = str(input('Não entendi, tente novamente. Sexo: [M/F] '))
    dados['idade'] = int(input('Idade: '))
    tot += 1
    totidade += dados['idade']
    pessoas.append(dados.copy())
    dados.clear()
    print('-=-' * 30),
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while r not in 'SN':
        r = str(input('Não entendi, tente novamente. Quer continuar? [S/N] '))
    print('-=-' * 30)
    if r in 'N':
        break
media = totidade / tot
print(f'Um total de {tot} pessoas foram cadastradas.')
print('-=-' * 30)
print(f'A média de idade entre as pessoas cadastradas é de {media:.0f} anos.')
print('-=-' * 30)
print('As mulheres cadastradas são: ')
print('-=-' * 30)
for v in pessoas:
    if v['sexo'] == 'F':
        print(f'->{v["nome"]:.>15}')
print('-=-' * 30)
print('As pessoas cadastradas com idade acima da média são: ')
print('-=-' * 30)
for i in pessoas:
    if i['idade'] >= media:
        print(f'->{i["nome"]:.>15} ({i["idade"]} anos)')
print('-=-' * 30)
