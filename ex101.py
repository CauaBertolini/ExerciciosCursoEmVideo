#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
#retornando um valor literal indicando se uma pessoa tem voto Negado, Opcional ou Obrigatório nas eleições.
import datetime


def voto(ano):
    """
    Esta função calcula através do ano do seu nascimento, se você precisa ou não votar
    no ano atual em que o análise é feita.
    :param ano: Preencha com o ano do seu nascimento
    :return: Irá retornar se você precisa ou não votar e se é obrigatório ou opcional
    """
    atual = datetime.date.today().year
    idade = atual - ano
    if idade > 18:
        return f'Com {idade} ano(s), seu voto é OBRIGATÓRIO'
    elif 18 > idade >= 16 or idade > 65:
        return f'Com {idade} ano(s), seu voto é OPCIONAL'
    elif idade < 16:
        return f'Com {idade} ano(s), seu voto é NEGADO'


ano = int(input('Digite o ano do seu nascimento: '))
print(voto(ano))