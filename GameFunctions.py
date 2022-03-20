import sys
import pygame

def checkEvents():                                       # Metodo para responder a las pulsaciones de teclas y eventos del raton
    for event in pygame.event.get():                     # Ciclo de eventos para controlar el juego
            if event.type == pygame.QUIT:                # Si el usuario da click en el boton de cierre de la ventana
                sys.exit()                               # Se cierra todo proceso y termina el juego