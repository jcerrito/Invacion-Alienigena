import pygame
from pygame.sprite import Sprite

class Alien(Sprite):                                                                               # Clase para representar a cada uno de los aliens
                                    
    def __init__(self, settings, screen):                                                          # Funcion para inicializar el alien y establecer la posicion inicial en pantalla
        super(Alien, self).__init__(                                )                                

        self.screen = screen                                                                       # Recibimos los valores de la pantalla de ejecucion
        self.settings = settings                                                                   # Recibimos los valores de la configacion general del juego
                                        
        self.image = pygame.image.load("images/alien.bmp")                                         # Cargamos la imagen del alien a una variable para posteriormente mostrarla en pantalla
        self.rect = self.image.get_rect()                                                          # Guardamos la imagen como un cuadro de pixeles
                                        
        self.rect.x = self.rect.width                                                              # Preparamos la coordenada x para mostrar el alien en pantalla
        self.rect.y = self.rect.height                                                             # Preparamos la coordenada y para mostrar el alien en pantalla                                

        self.x = float(self.rect.x)                                                                # Almacenamos el valor real decimal de la posicion de la nave                                

    def blitMe(self):                                                                              # Funcion para posicionar la nave en su posicion actual
        self.screen.blit(self.alienImage, self.rect)                                               # Mostramos la imagen del alien en pantalla.

    def checkEdges(self):                                                                          # Controla que la flota de aliens no salga de la pantalla
        screenRect = self.screen.get_rect()                                                        # Obtenemos los bordes de la pantalla
        if self.rect.right >= screenRect.right:                                                    # Si el movimiento a la derecha de los alien es mayor al borde de la pantalla
            return True                                                                            # Regresamos el valor True
        elif self.rect.left <= 0:                                                                  # Si el borde de la izquierda es menor a 0
            return True                                                                            # Regresamos el valor True

    def update(self):                                                                              # Método para mover el alien a la derecha
        self.x += (self.settings.speedFactorAlien * self.settings.fleetDirection)                  # Actualizamos la posicion en x del alien en pantalla
        self.rect.x = self.x                                                                       # Determinamos cual sera su nueva posicion en pantalla
