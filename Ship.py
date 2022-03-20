import pygame

class Ship():
    """ Clase para controlar el comportamienot de la nave """

    def __init__(self, settings, screen):                     # Metodo encargado de inicializar la nave y establecer la posicion de inicio
        self.screen = screen
        self.settings = settings                              # Con la variable settings podemos hacer uso de las configuraciones

        self.image = pygame.image.load("images/ship.bmp")     # Cargamos la imagen de la nave
        self.rect = self.image.get_rect()                     # Obtenemos el rect de la superficie para mostrar la nave
        self.screen_rect = screen.get_rect()                  # Obtenemos el rect de la pantalla

        self.rect.centerx = self.screen_rect.centerx          # La coordenada rect x del centro de la nave la igualamos a la coordenada rect x del centro de la pantalla
        self.rect.bottom = self.screen_rect.bottom            # La coordenada rect y de la parte inferior de la nave la igualamos a la coordenada rect y de la parte inferior de la pantalla

        self.center = float(self.rect.centerx)                # Almacenamos un valor decimal para el centro de la nave

        self.movingRight = False                              # Bandera de movimiento de la nave hacia la derecha
        self.movingLeft = False                               # Bandera de movimiento de la nave hacia la izquierda

    def update(self):                                         # Actualiza la posicion de la nave acorde  al bandera de movimiento
        if self.movingRight:                                  # Verificamos si la bandera de movimiento a la derecha se encuentra activa
            self.center += self.settings.shipSpeedFactor      # Si la bandera de movimiento a la derecha se encuentra activa movemos la nave a la derecha
        
        if self.movingLeft:                                   # Verificamos si la bandera de movimiento a la izquierda se encuentra activa
            self.center -= self.settings.shipSpeedFactor      # Si la bandera de movimiento a la izquierda se encuentra activa movemos la nave a la izquierda

        self.rect.centerx = self.center                       # Aplicamos el movimiento para que este se muestre en pantalla

    def blitme(self):                                         # Metodo para posicionar la nave en su posicion actual
        self.screen.blit(self.image, self.rect)               # Posiciona la imagen en la pantalla para visualizarla
        