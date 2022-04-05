import pygame


class Nave:
    def __init__(self, configuraciones, pantalla):
        # Inicializa la nave y estable su posicion de partida
        self.pantalla = pantalla
        self.configuracones = configuraciones
        # Carga la imagen de la nave y obtiene su rect
        self.imagen = pygame.image.load("images/nave.png")
        self.rect = self.imagen.get_rect()
        self.pantalla_rect = pantalla.get_rect()

        # Empiza carda nueva nave empieza en la parte izquierda central de la pantalla
        self.rect.centery = self.pantalla_rect.centery
        self.rect.left = self.pantalla_rect.left

        # Almacena un valor decimal para el centro de la nave
        self.center = float(self.rect.centery)
        # Banderas de movimiento
        self.moving_up = False
        self.moving_down = False

    def update(self):
        # actualiza la posicion de la nave segun la bandera de movimiento
        if self.moving_up and self.rect.top > 0:
            self.center -= self.configuracones.factor_velocidad_nave
        if self.moving_down and self.rect.bottom < self.pantalla_rect.bottom:
            self.center += self.configuracones.factor_velocidad_nave
        self.rect.centery = self.center

    def blitme(self):
        # dibuja el eva en su ubicacion actual
        self.pantalla.blit(self.imagen, self.rect)
