# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# A media de idade do grupo
# Qual e o nome do homem mais velho
# quantas mulheres tem menos de 20 anos
divisor = 0
soma = 0
mulheres = 0
nomvelho = ''
mulheres = 0
for p in range(1, 5):
    print('-=-=-=-=- {}° Pessoa -=-=-=-=-'.format(p))
    nome = str(input('Nome: '.format(p)).strip())
    idade = int(input('Idade: '.format(p)))
    sexo = str(input('Sexo [M/F]: ').strip().upper())
    divisor = divisor + 1
    soma += idade
    media = soma / divisor
    if sexo == 'M': # Masculino
        if p == 1:
            velho = idade
            nomvelho = nome
        else:
            if idade > velho:
                velho = idade
                nomvelho = nome
    elif sexo == 'F': # Feminino
        if idade < 20:
            mulheres += 1
print('A media de idade do grupo e {} anos. '.format(media))
print('Tem {} mulheres com mais de 20 anos.'.format(mulheres))
print('O homem mais velho e o {} que tem {} anos'.format(nomvelho, velho))
