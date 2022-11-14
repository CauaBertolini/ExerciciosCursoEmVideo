# Crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com o nome "Santo".
city = str(input('\033[35mDigite o nome de sua cidade: ').strip())
cityd = city.split()
print('\033[34m{} começa com Santo? \033[33m{}'.format(city, 'Santo' in cityd[0].title()))

# Guanabara fez desse geito:

city = str(input('\033[35mDigite o nome da sua cidade: ')).strip()
print('\033[34mSua cidade tem santo no nome?\033[30m', city[:5].title() == 'Santo')