# Crie um programa que leia o nome completo de uma pessoa e mostre:
# > O nome com todas as letras maiusculas
# > O nome com todas as letras minusculas
# > Quantas letras ao todo (sem considerar os espaços)
# > Quantas letras tem o primeiro nome
nome = str(input('\033[34mDigite seu nome completo: ')).strip()
dividido = nome.split()
print('\033[35mAnalisando seu nome...')
print('Seu nome em maiusculo ficaria:', nome.upper())
print('Seu nome em minusculo ficaria: ', nome.lower())
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
# print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
print('Seu primeiro nome que e {} tem {} letras'.format(dividido[0], len(dividido[0])))
