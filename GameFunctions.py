import sys
import pygame

def checkEvents():                                       # Metodo para responder a las pulsaciones de teclas y eventos del raton
    for event in pygame.event.get():                     # Ciclo de eventos para controlar el juego
        if event.type == pygame.QUIT:                    # Si el usuario da click en el boton de cierre de la ventana
            sys.exit()                                   # Se cierra todo proceso y termina el juego

def refreshScreen(settings, screen, ship):               # Metodo que actualiza las imagenes en la pantalla durante la ejecución
    screen.fill(settings.bg_color)                       # Dibujamos la pantalla en cada ciclo asignando el color de fondo
    ship.blitme()                                        # Dibujamos la nave en pantalla
        
    pygame.display.flip()                                # Indica a pygame que dibuje una nueva pantalla y actualiza los espacios