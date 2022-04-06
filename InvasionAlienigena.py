import pygame
from pygame.sprite import Group
import GameFunctions as gameFunctions                                                       # Importamos GameFunctions y sus funciones las guardamos en una variable

from Settings import Settings                                                               # Del archivo Settings importamos la clase Settings
from Ship import Ship                                                                       # Del archivo Ship importamos la clase Ship

def run_game():                                                                             # Definimos el metodo que inicializa el juego, las configuraciones y el objeto screen
    pygame.init()                                                                           # Inicializa la configuracion de pygame
    settings = Settings()                                                                   # Settings nos permite importar las configuraciones del juego
    
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))       # Creamos la pantalla de visualizacion indicando en pixeles el ancho y el alto
    pygame.display.set_caption("Invasión Alienígena")                                       # Asignamos el titulo de la ventana

    ship = Ship(settings, screen)                                                           # Creamos una nave en pantalla
    bullets = Group()                                                                       # Grupo para almacenas lar las balas
    aliens = Group()                                                                        # Creamos un grupo para almacenar los aliens

    gameFunctions.createFleet(settings, screen, aliens)                                     # Creamos una flota de aliens

    while True:                                                                             # Bucle de activacion de juego
        gameFunctions.checkEvents(settings, screen, ship, bullets)                          # Detectar eventos del teclado o raton. Metodo traido desde GameFunctions
        ship.update()                                                                       # Actualizamos los valores de la nave durante la ejecucion
        gameFunctions.updateBullets(settings, screen, ship, bullets, aliens)                # Actualizamos las balas disparadas con respecto a la pantalla
        gameFunctions.updateAliens(settings, aliens)                                        # Actializamos la flota de aliens con respecto a la pantalla
        gameFunctions.refreshScreen(settings, screen, ship, aliens, bullets)                # Actualizamos las imagenes en pantalla durante la ejecucion

run_game()                                                                                  # Ejecutamos el metodo que inicializa el juego