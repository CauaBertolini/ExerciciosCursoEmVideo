# Faça um programa que leia o sexo de uma pessoa, mas so aceite os valores M ou F. Caso esteja errado, peça a digitaçao novamente ate ter um valor correto.
homem = 0
mulher = 0
'''while homem + mulher == 0:
    sexo = str(input('\033[34mDigite seu sexo: [M/F] ')).strip().upper()[0]
    print('\033[33m-=-'* 15)
    if sexo == 'M':
        print('\033[35mAnotado, Masculino!')
        homem += 1
    elif sexo == 'F':
        print('\033[35mAnotado, Feminino!')
        mulher += 1
    else:
        print('\033[31mOpa! Nao entendi, tente de novo por favor')
        print('\033[33m-=-'* 15''' # Eu fiz esse
sexo = str(input('Insira seu sexo: [F/M] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados invalidos, por favor, insira seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))