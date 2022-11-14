def aumentar(valor=0, taxa=10, format=False):
    """
    Aumenta o valor na porcentagem dada.
    :param valor: Valor ou preço de algo.
    :param porcentagem: Porcentagem de aumento.
    :return: Valor acrescido da porcentagem.
    """
    r = valor + (valor * taxa / 100)
    return r if format is False else moedas(r)


def diminuir(valor=0, taxa=10, format=False):
    '''
    Diminue o valor na porcentagem dada.
    :param valor: Valor ou preço de algo.
    :param porcentagem: Porcentagem de dedução.
    :return: Valor diminuído da porcentagem.
    '''
    r = valor - (valor * taxa / 100)
    return r if format is False else moedas(r)


def dobro(valor=0, format=False):
    valord = valor * 2
    return valord if not format else moedas(valord)


def metade(valor=0, format=False):
    valorm = valor / 2
    return valorm if not format else moedas(valorm)


def moedas(valor):
    valorreal = (f'R${valor:.2f}')
    valorTexto = str(valorreal)
    valormonetario = valorTexto.replace('.', ',')
    return valormonetario

