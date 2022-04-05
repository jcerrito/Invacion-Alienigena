import pygame
from pygame.sprite import Sprite


class Alien(Sprite):  # Clase para representar a cada uno de los aliens

    def __init__(self, configuraciones, pantalla):  # Funcion para inicializar el alien y establecer la posicion inicial en pantalla
        super(Alien, self).__init__()

        self.pantalla = pantalla  # Recibimos los valores de la pantalla de ejecucion
        self.configuraciones = configuraciones  # Recibimos los valores de la configacion general del juego

        self.image = pygame.image.load("images/alien.png")  # Cargamos la imagen del alien a una variable para posteriormente mostrarla en pantalla
        self.rect = self.image.get_rect()  # Guardamos la imagen como un cuadro de pixeles

        self.rect.y = 100 #Preparamos la coordenada x para mostrar el alien en pantalla
        self.rect.x = 1250  # Preparamos la coordenada y para mostrar el alien en pantalla

        self.y = float(self.rect.y)  # Almacenamos el valor real decimal de la posicion de la nave

    def blitMe(self):  # Funcion para posicionar la nave en su posicion actual
        self.pantalla.blit(self.alienImage, self.rect)  # Mostramos la imagen del alien en pantalla.