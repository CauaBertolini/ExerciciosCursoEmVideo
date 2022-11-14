# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.
n = str(input('\033[34;1mDigite seu nome completo: ')).strip()
nome = n.split()
print('\033[36mMuito prazer em te conhecer!')
print('\033[35mSeu primeiro nome e \033[33m{}'.format(nome[0]))
print('\033[35mSeu ultimo nome e \033[33m{}'.format(nome[len(nome)-1])) # Basicamente eu contei quantos nomes tem, Ex.: Caua Bertolini Fernando tem 3 nomes, mas no python nao 0, 1, 2 nomes na lista entao -1 para informar e dizer o ultimo nome que aparece
