# Crie um programa que simule o funcionamento de um caixa eletronico. No inicio, pergunta ao usuario qual sera o valor a ser sacado (numero inteiro) e o programa vai informar quantas cedulas de cada valor serao entregues.
# Obs: Considere que o caixa possui cedulas de R$50, R$20, R$10 e R$1.
print('-=-' * 40)
print('Bem Vindo ao Banco BVB')
print('-=-' * 40)
dinheiro = int(input('Digite o valor a ser sacado: R$'))
print('-=-' * 40)
total = dinheiro
cedula = 50
totcedula = 0
print('Serao emitidas as seguintes notas:')
print('-=-' * 40)
while True:
    if total >= cedula:
        total -= cedula
        totcedula += 1
    else:
        if totcedula > 0:
            print(f'{totcedula} notas de R${cedula}')
        if cedula == 50:
            cedula = 20
            totcedula = 0
        elif cedula == 20:
            cedula = 10
            totcedula = 0
        elif cedula == 10:
            cedula = 1
            totcedula = 0
        if total == 0:
            break
print('-=-' * 40)
