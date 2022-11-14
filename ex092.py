#Crie um programa que leia o nome, ano de nascimento e
#carteira de trabalho e cadastre-os [com idade] em um dicionário
#se por acaso a CTPS for diferente de ZERO, o dicionário receberá
#também o ano de contratação e o salário. Calcule e acrescente
#além da idade, com quantos anos a pessoa vai se aposentar.
# 35 anos de contribuição se aposenta
from datetime import datetime
trabalhador = dict()
trabalhador['Nome'] = str(input('Nome: '))
trabalhador['Ano'] = int(input('Ano de nascimento: '))
trabalhador['Idade'] = datetime.now().year - trabalhador['Ano']
trabalhador['CTPS'] = int(input('Carteira de Trabalho: [Digite 0 caso não tenha uma] '))
if trabalhador['CTPS'] != 0:
    trabalhador['Contratação'] = int(input('Ano que foi contratado: '))
    trabalhador['Salário'] = float(input('Salário: R$ '))
    trabalhador['IdadeAposenta'] = trabalhador["Idade"] + (35 - (datetime.now().year - trabalhador["Contratação"]))
print('-=-'*30)
if trabalhador['CTPS'] != 0:
    print(f'Olá {trabalhador["Nome"]}! ', end='')
    if trabalhador['IdadeAposenta'] < trabalhador['Idade']:
        print(f'Você tem {trabalhador["Idade"]} anos. De acordo com nossas\n'
          f'estatísticas voçê deveria ter se aposentado com {trabalhador["IdadeAposenta"]} anos.')
    elif trabalhador['IdadeAposenta'] > 0:
        print(f'Você tem {trabalhador["Idade"]} anos. De acordo com nossas\n'
          f'estatísticas voçê irá se aponsentar com {trabalhador["IdadeAposenta"]} anos.')
if trabalhador['CTPS'] == 0:
    print(f'Olá {trabalhador["Nome"]}!')