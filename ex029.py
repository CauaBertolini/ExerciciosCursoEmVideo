# Escreva um programa que leia a velocidade de um carro
# Se ele ultrapassar 80km/h mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7.00 por cada km acima do limite
velocidade = float(input('\033[34mVelocidade do seu carro: '))
if velocidade > 80:
    pm = (velocidade - 80)*7
    ku = velocidade - 80
    print('\033[31mVoce tera que pagar R${:.2f} de multa por ultrapassar {}km/h o limite de 80km/h'.format(pm, ku))
else:
    print('\033[36mOk! Esta tudo certo.')