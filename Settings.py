class Settings():
    """ Esta clase almacenará todas las configuraciones """

    def __init__(self):                                   # Inicializamos las configuraciones del juego
        self.screen_width = 800                           # Asignamos un valor para el ancho de la ventana del juego
        self.screen_height = 600                          # Asignamos un valor pata el alto de la ventana del juego
        self.bg_color = (230, 230, 230)                   # Asignamos en formato rgb un color para el fondo de la ventana
        
        """ Configuraciones de la Nave """
        self.shipSpeedFactor = 1.5                        # Configuramos en 1.5 pixeles la velocidad de movimiento de la nave

        """ Configuraciones de las balas """
        self.speedFactorBullet = 1                        # Velocidad con la que se movera la bala
        self.bulletWidht = 3                              # Ancho de la bala en pixeles con respecto a la pantalla
        self.bulletHeight = 15                            # Largo de la bala en pixeles con respecto a la pantalla
        self.bulletColor = 60, 60, 60                     # Color que tendra la bala al momento de la ejecucion (RGB)