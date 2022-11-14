# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 ate 0, com uma pausa de um segundo entre eles.
from time import sleep
import emoji
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(emoji.emojize('\033[33m:fireworks::fireworks::fireworks::fireworks: Vivaaa :fireworks::fireworks::fireworks::fireworks:'))
