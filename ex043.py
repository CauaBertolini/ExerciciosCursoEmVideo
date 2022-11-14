# Desenvolva uma logica que leia o peso e a altura de uma pessoa, calculer seu IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal
# 25 ate 30: Sobrepeso
# 30 ate 40: Obesidade
# Acima de 40: Obesidade morbida
peso = float(input('\033[34mDigite seu peso: (kg) '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('\033[37mVoce esta abaixo do peso!')
elif imc >= 18.5 and imc < 25:
    print('\033[34mSeu peso esta ideal!')
elif imc >= 25 and imc < 30:
    print('\033[33mVoce esta com Sobrepeso!')
elif imc >= 30 and imc < 40:
    print('\033[35Voce esta Obeso(a)!')
elif imc > 40 and imc < 80:
    print('\033[31mVoce esta com obesidade morbida! Procure mudar seus habitos e tente reverter isso!')
elif imc > 80:
    print('\033[36mIsso e muito alem do que e recomendado para voce! Procure ajuda agora! Sua vida depende disso!')
print('\033[34mSeu IMC e {:.2f}'.format(imc))
