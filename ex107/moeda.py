def aumentar(valor, taxa=10, real=False):
    """
    Aumenta o valor na porcentagem dada.
    :param valor: Valor ou preço de algo.
    :param porcentagem: Porcentagem de aumento.
    :return: Valor acrescido da porcentagem.
    """
    r = valor + (valor * taxa / 100)
    return r


def diminuir(valor, taxa=10, real=False):
    '''
    Diminue o valor na porcentagem dada.
    :param valor: Valor ou preço de algo.
    :param porcentagem: Porcentagem de dedução.
    :return: Valor diminuído da porcentagem.
    '''
    r = valor - (valor * taxa / 100)
    return r


def dobro(valor, real=False):
    valord = valor * 2
    return valord


def metade(valor, real=False):
    valorm = valor / 2
    return valorm
