def aumentar(valor, porcentagem=10, real=False):
    """
    Aumenta o valor na porcentagem dada.
    :param valor: Valor ou preço de algo.
    :param porcentagem: Porcentagem de aumento.
    :return: Valor acrescido da porcentagem.
    """
    r = valor + (valor * porcentagem / 100)
    if real:
        r = moedas(r)
    return r


def diminuir(valor, porcentagem=10, real=False):
    '''
    Diminue o valor na porcentagem dada.
    :param valor: Valor ou preço de algo.
    :param porcentagem: Porcentagem de dedução.
    :return: Valor diminuído da porcentagem.
    '''
    r = valor - (valor * porcentagem / 100)
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


def resumo(valor):
    valorreal = moedas(valor)
    frase = (f'  RESUMO DO VALOR {valorreal}')
    print('-'*(len(frase)+2))
    print(frase)
    print('-'*(len(frase)+2))
    print(f'10% de aumento:{aumentar(valor, real=True):>12}')
    print(f'10% de redução:{diminuir(valor, real=True):>12}')
    print(f'Dobro:{dobro(valor, True):>21}')
    print(f'Metade:{metade(valor, True):>20}')
    print('-'*(len(frase)+2))

