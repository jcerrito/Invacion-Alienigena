import pygame
from pygame.sprite import Group
# Importaciones de las configuraciones
from Settings import Configuraciones
# Importamos el eva
from Ship import Nave
# Importar funciones_juego
import GameFunctions as fj


def run_game():
    # Se inicializa el juego y se crea un objeto pantalla
    pygame.init()
    configuraciones = Configuraciones()
    pantalla = pygame.display.set_mode(
        (configuraciones.screen_width, configuraciones.screen_height))
    pygame.display.set_caption("Ataque Alienigena", "image/nave.png")

    # se crea un nueva nave
    nave = Nave(configuraciones, pantalla)

    # Crea un grupo para almacenar las balas
    balas = Group()
    # crea un grupo de aliens
    aliens = Group()
    # crea la flota de alienigenas
    fj.crear_flota(configuraciones, pantalla, aliens)
    fondo = pygame.image.load("images/fondo.jpg").convert()

    # Se inicia el bucle principal del juego
    while True:
        fj.verificar_eventos(configuraciones, pantalla, nave, balas)
        nave.update()
        # desghace las balas que han desaparecido
        balas.update()
        fj.update_balas(balas)
        fj.actualizar_pantalla(fondo, pantalla, nave, aliens, balas)


run_game()
