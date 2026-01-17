import pygame 
import random

pygame.init()

#configuracion de la pantalla
ANCHO = 800
ALTO = 600

screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de Evitar Obstaculos")

#colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (255, 0, 0)
azul = (0, 0, 255)
verde = (0, 255, 0)

#jugador
jugador_ancho = 50
jugador_alto = 50
jugador = pygame.Rect(ANCHO // 2 - jugador_ancho // 2, ALTO - jugador_alto - 10, jugador_ancho, jugador_alto)


#Bucle principal del juego
running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #llenar la pantalla
    screen.fill(blanco)
   #dibujar el jugador
    pygame.draw.rect(screen, azul, jugador)

    
    #actualizar pantalla
    pygame.display.flip()
    #controlar frames
    pygame.time.Clock().tick(60)

 

pygame.quit()