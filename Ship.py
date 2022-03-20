import pygame

class Ship():
    """ Clase para controlar el comportamienot de la nave """

    def __init__(self, screen):                               # Metodo encargado de inicializar la nave y establecer la posicion de inicio
        self.screen = screen

        self.image = pygame.image.load("images/ship.bmp")     # Cargamos la imagen de la nave
        self.rect = self.image.get_rect()                     # Obtenemos el rect de la superficie para mostrar la nave
        self.screen_rect = screen.get_rect()                  # Obtenemos el rect de la pantalla

        self.rect.centerx = self.screen_rect.centerx          # La coordenada rect x del centro de la nave la igualamos a la coordenada rect x del centro de la pantalla
        self.rect.bottom = self.screen_rect.bottom            # La coordenada rect y de la parte inferior de la nave la igualamos a la coordenada rect y de la parte inferior de la pantalla

    def blitme(self):                                         # Metodo para posicionar la nave en su posicion actual
        self.screen.blit(self.image, self.rect)               # Posiciona la imagen en la pantalla para visualizarla
        