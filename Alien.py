import pygame
from pygame.sprite import Sprite

class Alien(Sprite):                                               # Clase para representar a cada uno de los aliens
    
    def __init__(self, settings, screen):                          # Funcion para inicializar el alien y establecer la posicion inicial en pantalla
        super(Alien, self).__init__()

        self.screen = screen                                       # Recibimos los valores de la pantalla de ejecucion
        self.settings = settings                                   # Recibimos los valores de la configacion general del juego
        
        self.alienImage = pygame.image.load("images/alien.bmp")    # Cargamos la imagen del alien a una variable para posteriormente mostrarla en pantalla
        self.rect = self.alienImage.get_rect()                     # Guardamos la imagen como un cuadro de pixeles
        
        self.rect.x = self.rect.width                              # Preparamos la coordenada x para mostrar el alien en pantalla
        self.rect.y = self.rect.height                             # Preparamos la coordenada y para mostrar el alien en pantalla

        self.x = float(self.rect.x)                                # Almacenamos el valor real decimal de la posicion de la nave

    def blitMe(self):                                              # Funcion para posicionar la nave en su posicion actual
        self.screen.blit(self.alienImage, self.rect)               # Mostramos la imagen del alien en pantalla.