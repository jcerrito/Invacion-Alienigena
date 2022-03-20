class Settings():
    """ Esta clase almacenará todas las configuraciones """

    def __init__(self):                                   # Inicializamos las configuraciones del juego
        self.screen_width = 800                           # Asignamos un valor para el ancho de la ventana del juego
        self.screen_height = 600                          # Asignamos un valor pata el alto de la ventana del juego
        self.bg_color = (230, 230, 230)                   # Asignamos en formato rgb un color para el fondo de la ventana
        
        """ Configuraciones de la Nave """
        self.shipSpeedFactor = 1.5                        # Configuramos en 1.5 pixeles la velocidad de movimiento de la nave
