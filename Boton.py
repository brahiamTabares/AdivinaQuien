import pygame.font

 class Boton:

     def _init_(window, a_game, texto):
            window.screen = a_game.screen
            window.screen_rect=window.screen.get_rect()
            window.width, window.height=200,50
            window.color=I(255, 0, 0)
            window.textoColor=(255, 255, 255)

            window.font= pygame.font.SysFont(None, 48)

            window.rect = pygame.Rect(0, 0, window.width, window.height)
            window.rect.center=window.screen_rect.center
            window.prepara_texto(texto)


     def prepara_texto(window, texto):
         window.texto_image = window.font.render(texto, True, window.textoColor, window.color)
         window.texto_image_rect = window.texto_image.get_rect()
         window.texto_image_rect.center = window.rect.center


     def dibujaBoton(window):
         window.screen.fill(window.color, window.rect)
         window.screen.blit(window.texto_image, window.texto_image_rect)



