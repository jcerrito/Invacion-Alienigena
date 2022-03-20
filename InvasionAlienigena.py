from asyncio import run
import sys
import pygame

from Settings import Settings
from Ship import Ship

def run_game():                                                                             # Definimos el metodo que inicializa el juego, las configuraciones y el objeto screen
    pygame.init()                                                                           # Inicializa la configuracion de pygame
    settings = Settings()                                                                   # Settings nos permite importar las configuraciones del juego
    
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))       # Creamos la pantalla de visualizacion indicando en pixeles el ancho y el alto
    pygame.display.set_caption("Invasión Alienígena")                                       # Asignamos el titulo de la ventana

    ship = Ship(screen)                                                                     # Creamos una nave en pantalla

    bg_color = (settings.bg_color)                                                          # Creamos una variable para establecer el color de fondo en la pantalla

    while True:                                                                             # Bucle de activacion de juego
        
        for event in pygame.event.get():                                                    # Ciclo de eventos para controlar el juego
            if event.type == pygame.QUIT:                                                   # Si el usuario da click en el boton de cierre de la ventana
                sys.exit()                                                                  # Se cierra todo proceso y termina el juego

        screen.fill(bg_color)                                                               # Dibujamos la pantalla en cada ciclo asignando el color de fondo
        ship.blitme()                                                                       # Dibujamos la nave en pantalla
        
        pygame.display.flip()                                                               # Indica a pygame que dibuje una nueva pantalla y actualiza los espacios

run_game()                                                                                  # Ejecutamos el metodo que inicializa el juego