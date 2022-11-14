# Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento
s = float(input('\033[33mDigite seu salario: R$'))
sa = s * 15 / 100
print('\033[34mSeu salario com 15% de aumento e {:.2f} reais'.format(s + sa))
