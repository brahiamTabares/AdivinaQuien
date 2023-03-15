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

#configuracion del Botton

BUTTONCOLOR1 = (255,255, 0)
TEXTBUTTONCOLOR = (0, 0,255)
x = 200
y = 400
ancho = 200
alto = 100
rectangulo = pygame.Rect(x, y, ancho, alto)

pygame.draw.rect(window, BUTTONCOLOR1, rectangulo)

fuente = pygame.font.Font(None, 80)
texto = fuente.render("PLAY", True, TEXTBUTTONCOLOR)
texto_rect = texto.get_rect(center=rectangulo.center)
while True:
    window.fill(colorFondo)
    window.blit(ImagenPrincipal, (20, 5))
    window.blit(texto, texto_rect)
    for evento in pygame.event.get():
        if evento.type==QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if rectangulo.collidepoint(evento.pos):
                print("Haz hecho clic en el botón")


    # llamados de los componentes de texto
    window.blit(miTextoSistema,(220,200))
    window.blit(miTexto,(100,250))

    #Botton event


    pygame.display.update()