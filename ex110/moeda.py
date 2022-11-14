def aumentar(valor, taxa=10, real=False):
    """
    Aumenta o valor na porcentagem dada.
    :param valor: Valor ou preço de algo.
    :param porcentagem: Porcentagem de aumento.
    :return: Valor acrescido da porcentagem.
    """
    r = valor + (valor * taxa / 100)
    if real:
        r = moedas(r)
    return r


def diminuir(valor, taxa=10, real=False):
    '''
    Diminue o valor na porcentagem dada.
    :param valor: Valor ou preço de algo.
    :param porcentagem: Porcentagem de dedução.
    :return: Valor diminuído da porcentagem.
    '''
    r = valor - (valor * taxa / 100)
    if real:
        r = moedas(r)
    return r


def dobro(valor, real=False):
    valord = valor * 2
    if real:
        valorreal = moedas(valord)
        return valorreal
    else:
        return valor * 2


def metade(valor, real=False):
    valorm = valor / 2
    if real:
        valorreal = moedas(valorm)
        return valorreal
    else:
        return valor / 2


def moedas(valor):
    valorreal = (f'R${valor:.2f}')
    valorTexto = str(valorreal)
    valormonetario = valorTexto.replace('.', ',')
    return valormonetario


def resumo(valor, taxaa=10, taxar=5):
    valorreal = moedas(valor)
    print('-'*30)
    print(f'RESUMO DO VALOR {valorreal}'.center(30))
    print('-'*30)
    print(f'Aumento de {taxaa}%: \t{aumentar(valor, taxaa, real=True)}')
    print(f'Redução de {taxar}%: \t\t{diminuir(valor, taxar, real=True)}')
    print(f'Dobro: \t\t\t\t{dobro(valor, True)}')
    print(f'Metade: \t\t\t{metade(valor, True)}')
    print('-'*30)

