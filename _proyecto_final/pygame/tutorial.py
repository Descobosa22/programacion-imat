import pygame

# Configuración de la interfaz
pygame.init()
ventana = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Juego de baseball")

# Creación de la pelota
ball = pygame.image.load("resources/ball.jpg")
ballrect = ball.get_rect()
ballrect.move_ip(0, 0) # Posición inicial de la pelota: parte superior

# Creación del bate
bate = pygame.image.load("resources/bate.png")
baterect = bate.get_rect()
baterect.move_ip(240, 450)  # Posición inicial del bate: parte inferior

speed = [5, 5] # Vector de la velocidad en coordenadas [x, y]. Derecha-abajo.

jugando = True

# Bucle de juego
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False

    # Compruebo si se ha pulsado alguna tecla capturando el teclado
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        baterect = baterect.move(-3, 0)

    if keys[pygame.K_RIGHT]:
        baterect = baterect.move(3, 0)

    # Compruebo si hay colisión con el bate
    if baterect.colliderect(ballrect):
        speed[1] = -speed[1]

    # Compruebo las colisiones con las paredes laterales
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]  # Se invierte x

    # Compruebo las colisiones con el techo
    if ballrect.top < 0:
        speed[1] = -speed[1] # Se invierte y

    # Muevo la pelota a la nueva posición
    ballrect = ballrect.move(speed)

    if ballrect.bottom > ventana.get_height():
        jugando = False  # Nos salimos del bucle. Se podría poner en la condición. Lo dejamos aquí por si se quiere realizar otra acción.

    # Pinto los elementos con sus rect
    ventana.fill((255, 255, 255))
    ventana.blit(ball, ballrect)
    ventana.blit(bate, baterect)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()