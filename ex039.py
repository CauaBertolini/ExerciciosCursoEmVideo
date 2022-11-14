# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar
# Se e a hora de se alistar
# Se ja passou o tempo de alistamento
# Seu programa tambem tera que dizer quanto tempo falta ou que passou do prazo
import datetime
ano = int(input('\033[34mEm que ano voce nasceu? '))
anoatual = datetime.date.today().year
idade = anoatual - ano
print('\033[36mVoce tem {} anos de idade'.format(idade), end='')
if idade < 18:
    tempo = 18 - idade
    alistamento = anoatual + tempo
    print('\033[36m e voce tera que se alistar em {} isso sao daqui {} ano(s)! Prepare-se!'.format(alistamento, tempo))
elif idade > 18:
    tempo = idade - 18
    alistamento = anoatual - tempo
    print('\033[36m e o tempo para seu alistamento passou! Sua vez foi no ano de {} a {} ano(s) atras.'.format(alistamento, tempo))
elif idade == 18:
    print('\033[36m. \033[31mVoce tem que se alistar IMEDIATAMENTE!')