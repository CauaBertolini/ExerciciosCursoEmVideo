# A confederaçao nacional de nataçao precisa de um programa que leia o ano de nscimento de um atleta e mostre sua categoria de acordo com a idade:
# - Ate 9 anos: Mirim
# - Ate 14 anos: Infantil
# - Ate 19 Anos: Junior
# - Ate 20 Anos: Senior
# - Acima: Master
from datetime import date
print('\033[33m-=-'*30)
print('\033[32mPreencha o campo abaixo para se inscrever na confederaçao nacional de nataçao')
print('\033[33m-=-'*30)
ano = int(input('\033[34mDigite seu ano de nascimento: '))
atual = date.today().year
idade = atual - ano
print('\033[35mVoce tem {} ano(s). Portanto: \033[36m'.format(idade))
if idade <= 9:
    print('Voce e da categoria Mirim de nataçao')
elif idade <= 14:
    print('Voce e da categoria Infantil de nataçao')
elif idade <= 19:
    print('Voce e da categoria Junior de nataçao')
elif idade <= 25:
    print('Voce e da categoria Senior de nataçao')
elif idade > 25:
    print('Voce e da categoria Master de nataçao')
