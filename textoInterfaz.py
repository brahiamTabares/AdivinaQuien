import pygame
import sys

from pygame import *
from pygame.locals import *
import random


 #Configuración de la ventana del juego
pygame.init()
width = 800
height = 800
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Adivina Quién")
avatar = pygame.image.load("mujerMaravilla.png")
avatar = transform.scale(avatar,(300,300))
colorFondo =(1,150,70)


while True:
    window.fill(colorFondo)
    window.blit(avatar,(300,350))
    for evento in pygame.event.get():
        if evento.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
