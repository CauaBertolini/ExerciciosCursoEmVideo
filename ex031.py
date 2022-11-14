# Desenvolva um programa que pergunte a distancia de uma viajem em km. Calcule o preço da passagem, cobrando R$0,50 por km para viajens ate 200km e R$0,45 para viajens mais longas.
distancia = int(input('\033[34mQual e a distancia da viajem? '))
if distancia <= 200:
    preço = 0.50 * distancia
    print('\033[35mVoce tem que pagar R${:.2f} pela viajem'.format(preço))
else:
    preço = 0.45 * distancia
    print('\033[33mVoce tem que pagar R${:.2f} pela viajem'.format(preço))

# Outra maneira de resolver

# preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45