# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por km rodado.
dias = int(input('\033[35mPor quantos dias ele foi alugado? '))
kmrodado = float(input('Quantos Km ele percorreu? '))
pt = (dias * 60) + (kmrodado * 0.15)
print('\033[34mO valor total a ser pago pelo aluguel do carro e \033[33mR${:.2f}'.format(pt))
