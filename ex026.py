# Faça um programa que leia uma frase pelo teclado e mostre:
# > Quantas vezes aparece a letra "A"
# > Em que posiçao ela aparece a primeira vez
# > Em que posiçao aparece a ultima vez
frase = str(input('\033[34mDigite uma frase: ')).upper().strip()
print('\033[33mA letra "A" aparece {} vezes nessa frase.'.format(frase.count('A')))
print('A letra "A" aparece pela primeira vez na posiçao {}'.format(frase.find('A')+1))
print('A letra "A" aparece pela ultima vez na posiçao {}'.format(frase.rfind('A')+1))
