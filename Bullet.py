import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ Clase para disparar las balas desde la nave """
    def __init__(self, settings, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen

        self.rect = pygame.Rect(0, 0, settings.bulletWidth, settings.bulletHeight)     # Las balas no seran imagenes por lo tanto le asignamos una posicion en pantalla con el ancho y alto de la bala
        self.rect.centerx = ship.rect.centerx                                          # Posicionamos las balas con repecto al centro de la nave
        self.rect.top = ship.rect.top                                                  # Ubicamos las balas en el tope de la nave

        self.y = float(self.rect.y)                                                    # Almacenamos la posicion y de la bala en decimal
        self.color = settings.bulletColor                                              # Asignamos el color de la bala desde las configuraciones
        self.speedFactor = settings.speedFactorBullet                                  # Asignamos la velocidad de la bala desde las configuraciones
    
    def update(self):                                                                  # Actualiza la posicion de la bala en la pantalla
        self.y -= self.speedFactor                                                     # Actualiza la posicion decimal de la bala
        self.rect.y = self.y                                                           # Actualiza la posicion de los pixeles en pantalla

    