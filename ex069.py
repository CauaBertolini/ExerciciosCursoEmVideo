# Crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada, o programa devera perguntar se o usuario quer ou nao continuar. No final, mostrar:
# A) Quantas pessoas tem mais de 18 anos;
# B) Quantos Homens foram cadastrados;
# C) Quantas mulheres tem menos de 20 anos.
adultos = homens = mulheresjovens = cont = 0
print('-=-'*30)
print('Pesquisa de dados')
print('-=-'*30)
while True:
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite o seu sexo: [M/F] ')).strip()
    while sexo[0] not in 'MmFf':
        sexo = str(input('Opçao invalida, tente novamente: [M/F] ')).strip()
    if idade > 18:
        adultos += 1
    if sexo[0] in 'Mm':
        homens += 1
    if sexo[0] in 'Ff' and idade < 20:
        mulheresjovens += 1
    cont += 1
    print('-=-'*30)
    continuar = str(input('Dejesa Continuar? [S/N] ')).strip()
    while continuar[0] not in 'SsNn':
        continuar = str(input('Resposta invalida, tente novamente: [S/N] ')).strip()
    if continuar[0] in 'Nn':
        print('-=-' * 30)
        break
    print('-=-'*30)
print(f'''Os resultados da pesquisa foram os seguintes: 
[ {adultos} ] Pessoas sao maiores de 18 anos;
[ {homens} ] Homens se cadastraram;
[ {mulheresjovens} ] Mulheres tem menos de 20 anos.''')