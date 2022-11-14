palavras = ('boi', 'banana', 'arvore', 'latex', 'liberdade', 'enciclopedia')
for p in palavras:
    print(f'\nNa palavra \033[36;1m{p.upper()}\033[m temos as vogais: ', end='')
    for letra in p:
        if letra.lower() in 'aeioi':
            print(letra, end=' ')
