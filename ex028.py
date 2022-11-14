# Escreva um programa que faça o computador "Pensar" em um numero inteiro entre 0 e 5 e peça para o usuario tentar descobrir qual foi o numero escolhido pelo computador
# O programa devera escrever na tela se o usuario venceu ou perdeu
from random import randint
import time
np = randint(0, 5) # Gera um numero interio, aleatorio ou entre numeros como feito aqui.
print('\033[33;1m-=-\033[m'*13)
print('\033[36mEstou Pensando em um numero de 0 a 5...\033[m')
print('\033[33;1m-=-\033[m'*13)
resposta = int(input('\033[35mQue numero voce acha que e? '))
print('\033[1;34mPROCESSANDO...')
time.sleep(3) # Faz o computador esperar pelo tempo escolhido
print('\033[1;34mANALISANDO NUMEROS...')
time.sleep(3)
print('\033[1;34mVALIDANDO RESPOSTA...\033[m')
time.sleep(2)
if resposta == np:
    print('\033[1;32mVoce acertou em cheio! Parabens! Nossas mentes estao conectadas!\033[m')
else:
    print('\033[1;31mOpa! Nao era bem esse numero. Na verdade era {}'.format(np))
