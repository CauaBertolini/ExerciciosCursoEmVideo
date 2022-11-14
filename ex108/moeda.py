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


def moedas(valor=0, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')
