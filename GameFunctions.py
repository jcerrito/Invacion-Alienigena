import sys
import pygame
from Bullet import Bullet                                                                 # Importamos la clase Bullet
from Alien import Alien
from Ship import Ship                                                                   # Importamos la clase Alien
                    
def checkKeydownEvents(event, settings, screen, ship, bullets):                           # Responde a las pulsaciones de la teclas
    if event.key == pygame.K_RIGHT:                                                       # Comparamos el evento con la tecla de flecha derecha
        ship.movingRight = True                                                           # Si se cumple la condicion anterior la bandera de movimiento a la derecha se activa
    elif event.key == pygame.K_LEFT:                                                      # Verificamos si la tecla presionada es: flecha a la izquierda
        ship.movingLeft = True                                                            # Si se cumple la condicion anterior la bandera de movimiento a la izquierda se activa
    elif event.key == pygame.K_SPACE:                                                     # Verificamos si la tecla presionada es: tecla espacio
        fireBullet(settings, screen, ship, bullets)                                       # Disparamos una bala si aun no se supera el limite
    elif event.key == pygame.K_q:                                                         # Verificamos si la tecla presionada es: tecla q
        sys.exit()                                                                        # Cerramos todos los procesos del juego que se encuentren ejecutando
                    
def checkKeyupEvents(event, ship):                                                        # Detecta si se deja de presionar una tecla
    if event.key == pygame.K_RIGHT:                                                       # Verificamos si la tecla que se soltó es la tecla de flecha derecha
        ship.movingRight = False                                                          # Si se cumple la condicion anterior la bandera de movimiento a la derecha se desactiva
    elif event.key == pygame.K_LEFT:                                                      # Verifcamos si se deja de presionar la tecla flecha a la ezquierda
        ship.movingLeft = False                                                           # Si se cumple la condicion anterior la bandera de movimiento a la izquierda se desactiva
                    
def checkEvents(settings, screen, ship, bullets):                                         # Metodo para responder a las pulsaciones de teclas y eventos del raton
    for event in pygame.event.get():                                                      # Ciclo de eventos para controlar el juego
        if event.type == pygame.QUIT:                                                     # Si el usuario da click en el boton de cierre de la ventana
            sys.exit()                                                                    # Se cierra todo proceso y termina el juego
                    
        elif event.type == pygame.KEYDOWN:                                                # Si se detecta que se presiona una tecla cualquiera del teclado -> comienza a verificar qué tecla fue presionada
            checkKeydownEvents(event,settings,screen,ship,bullets)                        # Realiza la acción que corresponde a la pulsacion de la tecla
                    
        elif event.type == pygame.KEYUP:                                                  # Verificamos si la tecla presionada ha sido soltada
            checkKeyupEvents(event, ship)                                                 # Detiene la accion ejecutada por la tecla presionada
                    
def refreshScreen(settings, screen, ship, aliens, bullets):                               # Metodo que actualiza las imagenes en la pantalla durante la ejecución
    screen.fill(settings.bg_color)                                                        # Dibujamos la pantalla en cada ciclo asignando el color de fondo
                        
    for bullet in bullets.sprites():                                                      # Obtenemos todas las balas que han sido disparadas
        bullet.drawBullet()                                                               # Dibujamos cada una de estas balas en la pantalla
                    
    ship.blitme()                                                                         # Dibujamos la nave en pantalla
    aliens.draw(screen)                                                                   # Dibujamos cada uno de los aliens en pantalla
    pygame.display.flip()                                                                 # Indica a pygame que dibuje una nueva pantalla y actualiza los espacios
                    
def updateBullets(bullets):                                                               # Actualiza la posicion de las balas en pantalla y elimina las que salen de esta
    bullets.update()                                                                      # Actualizamos los valores para cada bala durante la ejecucion
                            
    for bullet in bullets.copy():                                                         # Checamos cada una de las balas disparadas
        if bullet.rect.bottom <= 0:                                                       # Verificamos si la posicion de la bala con respecto a la pantalla alcanza un valor cero
            bullets.remove(bullet)                                                        # Si la condicion anterior se cumple, removemos la bala antes de que salga de pantalla
                    
def fireBullet(settings, screen, ship, bullets):                                          # Dispara una bala si no ha alcanzado el limte
    if len(bullets) < settings.bulletsAllowed:                                            # Si el numero de balas disparadas es menor al permitido
        newBullet = Bullet(settings, screen, ship)                                        # Creamos una nueva bala
        bullets.add(newBullet)                                                            # Agregamos las balas a la pantalla
                    
def getAliensNumberX(settings, alienWidth):                                               # Metodo para definir la cantidad de aliens en el eje x
    availableSpaceX = settings.screen_width - 2 * alienWidth                              # Calculamos el espacio disponible del eje x en pantalla
    aliensNumberX = int(availableSpaceX / (2 * alienWidth))                               # Calculamos cuantas naves caben dentro a lo ancho de la pantalla
    return aliensNumberX                                                                  # Returnamos el numero de aliens que pueden ser colocados en el eje x
                    
def getRowsNumber(settings, heightShip, heightAlien):                                     # Metodo para definir el numero de filas de aliens que se ajusta a la pantalla
    availableSpaceY = (settings.screen_height - (3 * heightAlien) - heightShip)           # Calculamos el espacio disponible en el eje Y                    
    rowsNumber = int(availableSpaceY / (2 * heightAlien))                                 # Calculamos el numero de filas
    return rowsNumber                    
                    
def createAlien(settings, screen, aliens, aliensNumber, rowNumber):                       # Metodo para crear un alien
    newAlien = Alien(settings, screen)                                                    # Se crea cada uno de los aliens para asignar su posicion en la fila
    alienWidth = newAlien.rect.width                                                      # Cargamos el ancho del alien
    newAlien.x = alienWidth + 2 * alienWidth * aliensNumber                               # Calculamos con la posicion en x de cada alien en pantalla
    newAlien.rect.x = newAlien.x                                                          # Asignamox la posicion en x para cada uno e los alien que se crea
    newAlien.rect.y = newAlien.rect.height + 2 * newAlien.rect.height * rowNumber         #
    aliens.add(newAlien)                                                                  # Agregamos cada una de las posiciones al grupo de aliens
                    
def createFleet(settings, screen, aliens):                                                # Crea una flota completa de aliens
    alien = Alien(settings, screen)                                                       # Creamos un nuevo alien
    ship = Ship(settings, screen)
    aliensNumberX = getAliensNumberX(settings, alien.rect.width)                          # Asignamos el numero de aliens en x
    rowsNumber = getRowsNumber(settings, ship.rect.height, alien.rect.height)
    
    for rowNumber in range(rowsNumber):                                                   # Ciclo para crear cada una de las filas con aliens
        for aliensNumber in range(aliensNumberX):                                         # Creamos la cada fila de aliens
            createAlien(settings, screen, aliens, aliensNumber, rowNumber)                # Creamos cada uno de los aliens de acuerdo al ancho de la pantalla 