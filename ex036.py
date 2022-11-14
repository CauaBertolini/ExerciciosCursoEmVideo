# Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. O programa
# vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestaçao mensal sabendo que ele nao pode exceder 30% do salario ou entao o emprestimo sera negado.
print('\033[33m-=-'*30)
print('\033[32mBem vindo ao Pegue Seu Emprestimo! Preencha os campos abaixo e pegue seu emprestimo!')
print('\033[33m-=-'*30)
valor = float(input('\033[34mDigite o valor do Imovel: R$'))
salario = float(input('Digite o valor do seu salario: R$'))
anos = int(input('Digite em quantos anos deseja pagar: \033[m'))
valormensal = valor/(anos*12)
salarioporcem = (salario*30)/100
meses = anos*12
if valormensal <= salarioporcem:
    print('\033[33m-=-'*30)
    print('\033[32mEmprestimo Aprovado!')
    print('\033[33m-=-'*30)
    print('\033[36mVoce tera que pagar mensalmente R${:.2f} durante {} meses!'.format(valormensal, meses))
elif valormensal > salarioporcem:
    print('\033[31m-=-'*30)
    print('Emprestimo Negado!')
    print('-=-'*30)
    print('\033[36mO valor de R${:.2f} que voce tem que pagar mensalmente ultrapassa 30% de seu salario e o emprestimo nao podera ser dado!'.format(valormensal))
