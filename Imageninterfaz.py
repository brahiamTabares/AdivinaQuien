import pygame
import sys
from pygame import *
from pygame.locals import *



 #Configuración de la ventana del juego
pygame.init()
width = 600
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Adivina Quién")

# Configuración de la imagen

ImagenPrincipal = pygame.image.load("heroes.jpg")
ImagenPrincipal = transform.scale(ImagenPrincipal, (550, 200))
colorFondo =(0,0,0)

# Configuración del texto

miFuente = pygame.font.Font(None,80)
miTexto = miFuente.render("Adivina Quien",0,(255,255,0))

# Determinar la Fuente del texto

miFuenteSistema = pygame.font.SysFont("Arial",50)
miTextoSistema = miFuenteSistema.render("Juego",0,(255,255,255))

while True:
    window.fill(colorFondo)
    window.blit(ImagenPrincipal, (20, 5))
    for evento in pygame.event.get():
        if evento.type==QUIT:
            pygame.quit()
            sys.exit()
    # llamados de los componentes de texto
    window.blit(miTextoSistema,(220,200))
    window.blit(miTexto,(100,250))
    pygame.display.update()
