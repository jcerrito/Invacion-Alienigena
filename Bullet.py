import pygame
from pygame.sprite import Sprite


class Bala(Sprite):
    # La clase sirve para manejar las balas didparadas por la nave
    def __init__(self, configuraciones, pantalla, nave):
        super(Bala, self).__init__()
        self.pantalla = pantalla

        # crea una bala rec  en (0,0) y luego establece la posicion correcta
        self.rect = pygame.Rect(
            0, 0, configuraciones.bala_width, configuraciones.bala_height)
        self.rect.centery = nave.rect.centery
        self.rect.right = nave.rect.right

        # almacena la posicion de la bala como un float
        self.x = float(self.rect.x)
        self.color = configuraciones.bala_color
        self.factor_velocidad = configuraciones.factor_velocidad_bala

        # mueve la bala hacia la derecha
    def update(self):
        # Actualiza la posicion decimal de la bala
        self.x += self.factor_velocidad
        # Actualiza la posicion del rect
        self.rect.x = self.x

    # dibuja la bala en la pantalla
    def draw_bala(self):
        pygame.draw.rect(self.pantalla, self.color, self.rect)
