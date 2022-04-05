class Configuraciones():
    # Inicializa las configuraciones del juego
    def __init__(self):
        # Establece el tamaño de la ventana
        self.screen_width = 1350
        self.screen_height = 680
        # Establece el color de fondo
        self.bg_color = (230, 230, 230)
        # Configuracion de la velocidad de la nave
        self.factor_velocidad_nave = 1.5

        # Configuraciones de balas
        self.factor_velocidad_bala = 1
        self.bala_width = 15
        self.bala_height = 3
        self.bala_color = (255, 255, 255)
        self.balas_allowed = 10
