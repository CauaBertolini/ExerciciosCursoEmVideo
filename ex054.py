# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda nao atingiram a marioridade e quantas ja sao maiores. 21 marioriedade
from datetime import date
novos = 0
velhos = 0
atual = date.today().year
for a in range(1, 8):
    ano = int(input('Digite o ano de nascimento da {}° pessoa: '.format(a)))
    if atual - ano < 21:
        novos += 1
    elif atual - ano >= 21:
        velhos += 1
print('{} pessoas destas sete ja passaram da marioridade (21 anos) e {} ainda nao!'.format(velhos, novos))
