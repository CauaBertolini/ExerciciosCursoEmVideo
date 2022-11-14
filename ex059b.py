# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] Soma
# [ 2 ] Multiplicar
# [ 3 ] Maior
# [ 4 ] Novos Numeros
# [ 5 ] Sair do Programa
# Sue programa devera realizar a operaçao solicitada em cada caso.
from time import sleep
grande = False
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
escolha = 0
print('-=-'*20)
while escolha != 5:
    print('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos Numeros
[ 5 ] Sair do Programa''')
    print('-=-'*20)
    escolha = int(input('Digite sua escolha: '))
    if escolha == 1:
        soma = n1 + n2
        print('A soma entre {} e {} e {}'.format(n1, n2, soma))
    elif escolha == 2:
        m = n1 * n2
        print('A multiplicaçao entre {} e {} e {}'.format(n1, n2, m))
    elif escolha == 3:
        if n1 > n2:
            grande = True
            maior = n1
            print('Entre {} e {} o maior e {}'.format(n1, n2, maior))
        elif n2 > n1:
            grande = True
            maior = n2
            print('Entre {} e {} o maior e {}'.format(n1, n2, maior))
        elif n1 == n2:
            print('Nao ha maior! Os dois sao iguais!')
    elif escolha == 4:
        print('-=-'*20)
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif escolha == 5:
        print('-=-'*20)
        print('Tudo bem! Finalizando programa...')
        sleep(5)
    else:
        print('Escolha invalida, tente novamente!')
    print('-=-'*20)
print('Fim do programa! Volte sempre!')