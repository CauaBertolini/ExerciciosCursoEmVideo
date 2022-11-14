#Crie um programa que tenha uma tupla com varias palavras (nao usar acentos). Depois disso, voce deve mostrar para cada palavra, quais sao suas vogais.
palavras = ('boi', 'banana', 'arvore', 'latex', 'liberdade', 'enciclopedia')

for p in palavras:
    print(p, end=' : ')
    if 'a' in p.lower():
        print('a ', end='')
    if 'e' in p.lower():
        print('e ', end='')
    if 'i' in p.lower():
        print('i ', end='')
    if 'o' in p.lower():
        print('o ', end='')
    if 'u' in p.lower():
        print('u.')