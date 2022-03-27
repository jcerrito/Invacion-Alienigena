from operator import length_hint
import sys
import pygame
from Bullet import Bullet                                          # Importamos la clase Bullet

def checkKeydownEvents(event, settings, screen, ship, bullets):    # Responde a las pulsaciones de la teclas
    if event.key == pygame.K_RIGHT:                                # Comparamos el evento con la tecla de flecha derecha
        ship.movingRight = True                                    # Si se cumple la condicion anterior la bandera de movimiento a la derecha se activa
    elif event.key == pygame.K_LEFT:                               # Verificamos si la tecla presionada es: flecha a la izquierda
        ship.movingLeft = True                                     # Si se cumple la condicion anterior la bandera de movimiento a la izquierda se activa
    elif event.key == pygame.K_SPACE:                              # Verificamos si la tecla presionada es: tecla espacio
        if len(bullets) < settings.bulletsAllowed:                 # 
            newBullet = Bullet(settings, screen, ship)             # Creamos una nueva bala
            bullets.add(newBullet)                                 # Agregamos las balas a la pantalla

def checkKeyupEvents(event, ship):                                 # Detecta si se deja de presionar una tecla
    if event.key == pygame.K_RIGHT:                                # Verificamos si la tecla que se soltó es la tecla de flecha derecha
        ship.movingRight = False                                   # Si se cumple la condicion anterior la bandera de movimiento a la derecha se desactiva
    elif event.key == pygame.K_LEFT:                               # Verifcamos si se deja de presionar la tecla flecha a la ezquierda
        ship.movingLeft = False                                    # Si se cumple la condicion anterior la bandera de movimiento a la izquierda se desactiva

def checkEvents(settings, screen, ship, bullets):                  # Metodo para responder a las pulsaciones de teclas y eventos del raton
    for event in pygame.event.get():                               # Ciclo de eventos para controlar el juego
        if event.type == pygame.QUIT:                              # Si el usuario da click en el boton de cierre de la ventana
            sys.exit()                                             # Se cierra todo proceso y termina el juego

        elif event.type == pygame.KEYDOWN:                         # Si se detecta que se presiona una tecla cualquiera del teclado -> comienza a verificar qué tecla fue presionada
            checkKeydownEvents(event,settings,screen,ship,bullets) # Realiza la acción que corresponde a la pulsacion de la tecla

        elif event.type == pygame.KEYUP:                           # Verificamos si la tecla presionada ha sido soltada
            checkKeyupEvents(event, ship)                          # Detiene la accion ejecutada por la tecla presionada

def refreshScreen(settings, screen, ship, bullets):                # Metodo que actualiza las imagenes en la pantalla durante la ejecución
    screen.fill(settings.bg_color)                                 # Dibujamos la pantalla en cada ciclo asignando el color de fondo
    
    for bullet in bullets.sprites():                               # Obtenemos todas las balas que han sido disparadas
        bullet.drawBullet()                                        # Dibujamos cada una de estas balas en la pantalla

    ship.blitme()                                                  # Dibujamos la nave en pantalla   
    pygame.display.flip()                                          # Indica a pygame que dibuje una nueva pantalla y actualiza los espacios

def updateBullets(bullets):                                        # Actualiza la posicion de las balas en pantalla y elimina las que salen de esta
    bullets.update()                                               # Actualizamos los valores para cada bala durante la ejecucion
        
    for bullet in bullets.copy():                                  # Checamos cada una de las balas disparadas
        if bullet.rect.bottom <= 0:                                # Verificamos si la posicion de la bala con respecto a la pantalla alcanza un valor cero
            bullets.remove(bullet)                                 # Si la condicion anterior se cumple, removemos la bala antes de que salga de pantalla
