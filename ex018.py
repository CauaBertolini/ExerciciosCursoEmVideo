# Faça programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.
import math
ang = float(input('\033[34mDigite um angulo: '))
s = math.sin(math.radians(ang))
c = math.cos(math.radians(ang))
t = math.tan(math.radians(ang))
print('\033[35mO angulo {} tem o seno {:.2f} cosseno {:.2f} e sua tangente e {:.2f}'.format(ang, s, c, t))