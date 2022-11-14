# Crie um programa que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem no final
# de acordo com a media atingida.
# Media abaixo de 5.0: reprovado
# Media entre 5.0 e 6.9 recuperaçao
# Media 7.0 ou superior: aprovado
print('\033[33;1m-=-'*30)
print('\033[32mAnalisador de Media! Digite duas de suas notas e veremos sua situaçao!')
print('\033[33;1m-=-'*30)
nota1 = float(input('\033[34mDigite sua primeira nota: '))
nota2 = float(input('\033[34mDigite sua segunda nota: '))
media = (nota1 + nota2)/2
from time import sleep
print('\033[34mAnalisando notas...')
sleep(3)
if media < 5:
    print('\033[31mREPROVADO! Sua media {} esta abaixo de 5.0!'.format(media))
elif media >= 5 and media < 7:
    print('\033[35mRECUPERAÇAO! Sua media {} foi acima de 5.0 mas nao superou 6.9!'.format(media))
elif media >= 7.0:
    print('\033[36mAPROVADO! Parabens seus esforços neste ano resultaram na media {} e voce passou!'.format(media))
