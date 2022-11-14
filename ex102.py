#Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o
#outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: Aqui digite o número que deseja saber o fatorial
    :param show: Tem como padrão "False", quando quiser, poderá colocar "True" para ver o cálculo do fatorial ou não.
    :return: O resultado do fatorial de um número.
    """
    f = 1
    for c in range(n, 0, -1):
        if show == True:
            print(c, end='')
            if c > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


#print(fatorial(10, True))
help(fatorial)