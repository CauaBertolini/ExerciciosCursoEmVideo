# Reforça o Desafio 035 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo sera formado:
# Equilatero: Todos os lados iguais
# Isoceles: Dois lados iguais
# Escaleno: Todos os lados diferentes
print('\033[33m-=-'*20)
print('\033[32mAnalisador de Triangulos')
print('\033[33m-=-'*20)
print('\033[34mDigite as medidas dos lados dos catetos para prosseguir')
print('\033[33m-=-'*20)
m1 = float(input('\033[35mPrimeira medida: '))
m2 = float(input('Segunda Medida: '))
m3 = float(input('Terceira Medida: '))
print('\033[33m-=-'*20)
if m1 < (m2+m3) and m2 < (m1+m3) and m3 < (m1+m2):
    print('\033[34mE possivel formar um triangulo ', end='')
    if m1 == m2 and m1 == m3 and m2 == m3:
        print('EQUILATERO, pois todos os lados sao iguais')
    elif m1 == m2 and m1 != m3 or m1 == m3 and m1 != m2 or m2 == m3 and m2 != m1:
        print('ISOCELES, pois dois lados sao iguais')
    elif m1 != m2 and m1 != m3 and m2 != m3:
        print('ESCALENO, pois todos os lados sao diferentes uns dos outros')
else:
    print('\033[31mNao e possivel formar um Triangulo com essas medidas')
