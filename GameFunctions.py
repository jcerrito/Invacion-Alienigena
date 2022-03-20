import sys
import pygame

def checkEvents(ship):                                   # Metodo para responder a las pulsaciones de teclas y eventos del raton
    for event in pygame.event.get():                     # Ciclo de eventos para controlar el juego
        if event.type == pygame.QUIT:                    # Si el usuario da click en el boton de cierre de la ventana
            sys.exit()                                   # Se cierra todo proceso y termina el juego

        elif event.type == pygame.KEYDOWN:               # Si se detecta que se presiona una tecla cualquiera del teclado -> comienza a verificar qué tecla fue presionada
            if event.key == pygame.K_RIGHT:              # Comparamos el evento con la tecla de flecha derecha
                ship.movingRight = True                  # Si se cumple la condicion anterior la bandera de movimiento a la derecha se activa
            elif event.key == pygame.K_LEFT:             # Verificamos si la tecla presionada es: flecha a la izquierda
                ship.movingLeft = True                   # Si se cumple la condicion anterior la bandera de movimiento a la izquierda se activa

        elif event.type == pygame.KEYUP:                 # Verificamos si la tecla presionada ha sido soltada
            if event.key == pygame.K_RIGHT:              # Verificamos si la tecla que se soltó es la tecla de flecha derecha
                ship.movingRight = False                 # Si se cumple la condicion anterior la bandera de movimiento a la derecha se desactiva
            elif event.key == pygame.K_LEFT:             # Verifcamos si se deja de presionar la tecla flecha a la ezquierda
                ship.movingLeft = False                  # Si se cumple la condicion anterior la bandera de movimiento a la izquierda se desactiva

def refreshScreen(settings, screen, ship):               # Metodo que actualiza las imagenes en la pantalla durante la ejecución
    screen.fill(settings.bg_color)                       # Dibujamos la pantalla en cada ciclo asignando el color de fondo
    ship.blitme()                                        # Dibujamos la nave en pantalla   
    pygame.display.flip()                                # Indica a pygame que dibuje una nueva pantalla y actualiza los espacios