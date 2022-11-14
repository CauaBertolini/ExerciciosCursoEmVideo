# Crie um programa que leia uma frase qualquer e diga se ela e um palindroma, desconsiderando os espaços.
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('Voce escreveu {} e de traz pra frente e {}'.format(junto, inverso), end=' ')
if inverso == junto:
    print('entao sim! E um palindromo')
else:
    print('entao nao! Nao e um palindromo')
# Outra maneira de resolver:
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1] # Usando o fatiamento
print('Voce escreveu {} e de traz pra frente e {}'.format(junto, inverso), end=' ')
if inverso == junto:
    print('entao sim! E um palindromo')
else:
    print('entao nao! Nao e um palindromo')