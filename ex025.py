# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.
nome = str(input('\033[34mDigite seu nome completo: '))
nomeupado = nome.upper()
print('\033[35mSeu nome tem Silva? \033[33m{}'.format('SILVA' in nomeupado))
