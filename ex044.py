# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condiçao de pagamento:
# A vista dinheiro ou cheque: 10% de desconto
# A vista no cartao: 5% de desconto
# Em ate 2x no cartao: preço normal
# 3x ou mais no cartao: 20% de juros
print('\033[1;33m-=-'*30)
print("\033[32mCaixa Eletronico BVB's")
print('\033[1;33m-=-'*30)
valor = float(input('\033[34mDigite o Preço das compras: \033[33mR$'))
print('\033[1;33m-=-'*30)
print('\033[35mOpçao de Pagamento:\033[36m\nDigite 1 para a vista no dinheiro ou cheque\nDigite 2 para a vista no cartao\nDigite 3 para parcelar no cartao')
print('\033[1;33m-=-'*30)
opçao = int(input('\033[34mDigite a opçao escolhida: '))
print('\033[1;33m-=-'*30)
if opçao == 1:
    novovalor = (valor - ((valor*10)/100))
    print('\033[32mVoce tem que pagar R${:.2f} pelo produto, sua opçao de pagamento lhe da 10% de desconto!'.format(novovalor))
elif opçao == 2:
    novovalor = (valor-((valor*5)/100))
    print('\033[32mVoce tem que pagar R${:.2f} pelo produto, sua opçao de pagamento lhe da 5% de desconto!'.format(novovalor))
elif opçao == 3:
    print('\033[35mOpçoes de parcelamento: \033[36m\nDigite 1 para parcelar em 2 vezes\nDigite 2 para parcelar em 3 vezes ou mais')
    print('\033[1;33m-=-'*30)
    opçao2 = int(input('\033[34mDigite a opçao escolhida: '))
    print('\033[1;33m-=-' * 30)
    if opçao2 == 1:
        parcela = valor / 2
        print('\033[32mVoce tem que pagar 2x de R${:.2f}'.format(parcela))
    elif opçao2 == 2:
        vezes = int(input('\033[34mDigite em quantas vezes voce deseja parcelar: '))
        parcela = valor / vezes
        print('\033[1;33m-=-' * 30)
        novovalor = parcela+((parcela*20)/100)
        print('\033[32mVoce tem que pagar {}x de R${:.2f}, sua opçao de pagamento lhe da uma taxa de juros de 20%\nO total a ser pago sera R${:.2f}'.format(vezes, novovalor, valor+(valor*20/100)))
    else:
        print('\033[31mVoce nao digitou nenhuma opçao valida. Tente novamente.')
else:
    print('\033[31mVoce nao escolheu nenhuma opçao valida de pagamento. Tente novamente.')
print('\033[1;33m-=-'*30)
