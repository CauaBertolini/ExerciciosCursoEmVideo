#Crie um programa onde o usuario possa digitar cinco valores numericos e cadastre-os em uma lista
#Ja na posiçao correta de inserçao (sem usar o Sort())
#No final, mostre a lista ordenada na tela.
numeros = []
for c in range(0, 5):
    n = int(input('Digite um numero: '))
    if c == 0 or n > numeros[-1]:
        numeros.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(numeros):
            if n <= numeros[pos]:
                numeros.insert(pos, n)
                print(f'Adicionado na posiçao {pos} da lista ')
                break
            pos += 1
print('-=-'*30)
print(f'Os valores digitados foram {numeros}')