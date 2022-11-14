# Faça um programa  que em Python que abra e reproduza o audio de um arquivo MP3
import pygame
from time import sleep
print('Programing is working...')
sleep(5)
pygame.mixer.init()
pygame.init
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()):pass
