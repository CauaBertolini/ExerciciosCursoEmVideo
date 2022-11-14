# Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.
# Para salarios superiores a R$1.2500,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento e de 15%
salario = float(input('\033[33mDigite quanto voce ganha: \033[36mR$'))
if salario > 1200.00:
    ns = salario + (salario*10/100)
    print('\033[34mComo voce ganhava mais de R$1.200,00 voce ganhou um aumento de 10% e passou a ganhar R${:.2f}'.format(ns))
if salario <= 1200.00:
    ns = salario + (salario*15/100)
    print('\033[35mComo voce ganhava ou menos de ou R$1.200,00 voce ganhou um aumento de 15% e passou a ganhar R${:.2f}'.format(ns))
