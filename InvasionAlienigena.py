from asyncio import run

import pygame
import GameFunctions as gameFunctions                                                       # Importamos GameFunctions y sus funciones las guardamos en una variable

from Settings import Settings                                                               # Del archivo Settings importamos la clase Settings
from Ship import Ship                                                                       # Del archivo Ship importamos la clase Ship

def run_game():                                                                             # Definimos el metodo que inicializa el juego, las configuraciones y el objeto screen
    pygame.init()                                                                           # Inicializa la configuracion de pygame
    settings = Settings()                                                                   # Settings nos permite importar las configuraciones del juego
    
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))       # Creamos la pantalla de visualizacion indicando en pixeles el ancho y el alto
    pygame.display.set_caption("Invasión Alienígena")                                       # Asignamos el titulo de la ventana

    ship = Ship(screen)                                                                     # Creamos una nave en pantalla

    bg_color = (settings.bg_color)                                                          # Creamos una variable para establecer el color de fondo en la pantalla

    while True:                                                                             # Bucle de activacion de juego
        
        gameFunctions.checkEvents()                                                         # Detectar eventos del teclado o raton. Metodo traido desde GameFunctions

        screen.fill(bg_color)                                                               # Dibujamos la pantalla en cada ciclo asignando el color de fondo
        ship.blitme()                                                                       # Dibujamos la nave en pantalla
        
        pygame.display.flip()                                                               # Indica a pygame que dibuje una nueva pantalla y actualiza los espacios

run_game()                                                                                  # Ejecutamos el metodo que inicializa el juego