import sys
import pygame
from Bullet import Bala
from Alien import Alien


def eventos_keydonw(event, nave, configuraciones, pantalla, balas):
    if event.key == pygame.K_UP:
        nave.moving_up = True
    elif event.key == pygame.K_DOWN:
        nave.moving_down = True
    elif event.key == pygame.K_SPACE:
        # crea una nueva vala y la agrega al grupo de balas
        disparar(balas, configuraciones, pantalla, nave)


def eventos_keyup(event, nave):
    if event.key == pygame.K_UP:
        nave.moving_up = False
    elif event.key == pygame.K_DOWN:
        nave.moving_down = False


def verificar_eventos(configuraciones, pantalla, nave, balas):
    # responde a las pulsaciones de las teclas y los eventos del raton
    # Escucha eventos del trclado o del raton
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            eventos_keydonw(event, nave, configuraciones, pantalla, balas)
        elif event.type == pygame.KEYUP:
            eventos_keyup(event, nave)


def actualizar_pantalla(fondo, pantalla, nave, aliens, balas):
    # Actualiza las imagenes en la pantalla y pasa a la nueva pantalla
    # esto es para volver a dibijar la pantalla por cada iteracion en el bucle while
    pantalla.blit(fondo, [0, 0])
    #pantalla.fill((226, 226, 226))
    # Vuelve a dibujar todas las balas detras de la nave y de los extraterrestres
    for bala in balas.sprites():
        bala.draw_bala()
    nave.blitme()
    aliens.draw(pantalla)
    # Hacemos visible la pnatalla mas reciente
    pygame.display.flip()

# actualiza las balas


def update_balas(balas):
    for bala in balas.copy():
        if bala.rect.right == 1350:
            balas.remove(bala)

# dispara una bala si aun no alcanza el limite


def disparar(balas, configuraciones, pantalla, nave):
    if len(balas) < configuraciones.balas_allowed:
        nueva_bala = Bala(configuraciones, pantalla, nave)
        balas.add(nueva_bala)

# Crea flota


def crear_flota(configuraciones, pantalla, aliens):
    alien = Alien(configuraciones, pantalla)
    alien_width = alien.rect.width
    number_aliens_y = get_number_alines_y(configuraciones, alien_width)
    # crea la primra fila de aliens
    for alien_number in range(number_aliens_y):
        crear_alien(configuraciones, pantalla,
                    alien_width, alien_number, aliens)


def get_number_alines_y(configuraciones, alien_width):
    avialable_space_y = configuraciones.screen_width - 2 * alien_width
    number_aliens_y = int(avialable_space_y / (2 * alien_width))
    return number_aliens_y


def crear_alien(configuraciones, pantalla, alien_width, alien_number, aliens):
    alien = Alien(configuraciones, pantalla)
    alien.y = alien_width + 2 * alien_width * alien_number
    alien.rect.y = alien.y
    aliens.add(alien)
