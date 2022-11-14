# Desenvolva um programa que leia o primeiro termo e a razao de uma PA (progressao aritmetica). no final, mostre os 10 primeiros termos dessa progressao.
print('\033[33m-=-'*15)
print('\033[32m10 Termos De Uma PA')
print('\033[33m-=-'*15)
primeiro = int(input('\033[34mDigite o Primeiro Termo: '))
razao = int(input('\033[34mDigite a Razao: \033[35m'))
decimo = primeiro + (10 - 1) * razao
for pa in range(primeiro, decimo + razao, razao):
    print(pa, end=' -> ')
print('Acabou')