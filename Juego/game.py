import pygame 
from random import choice
import os 
import sys

# CONFIGURAR LA RUTA CORRECTA
# Obtener la carpeta donde está game.py
carpeta_juego = os.path.dirname(os.path.abspath(__file__))
# Cambiar el directorio de trabajo a esa carpeta
os.chdir(carpeta_juego)

# Inicializar Pygame
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
jugador_ancho = 60
jugador_alto = 60
jugador = pygame.Rect(ANCHO // 2 - jugador_ancho // 2, ALTO - jugador_alto - 10,
                       jugador_ancho, jugador_alto)

#meteoritos 
meteorito_ancho = 100
meteorito_alto = 100
meteoritos = []

#cargar imagen del jugador 
jugador_image = pygame.image.load("burger.png").convert_alpha()
enemigo_image = pygame.image.load("chubaka.png").convert_alpha()
fondo_img = pygame.image.load("estrellas.png")

#definir tamaño de imagenes 
jugador_tamaño =(jugador_alto, jugador_ancho)
enemigo_tamaño = (meteorito_alto, meteorito_ancho)
fondo_tamaño = (800, 600)

#redimensionar imagenes
jugador_image = pygame.transform.scale(jugador_image, jugador_tamaño)
enemigo_image = pygame.transform.scale(enemigo_image, enemigo_tamaño)
fondo_img = pygame.transform.scale(fondo_img, fondo_tamaño)



#Puntuacion
score = 0 
font = pygame.font.Font(None, 36)

#reloj para controlar FPS
clock = pygame.time.Clock()

#Bucle principal del juego
running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and jugador.left > 0:
        jugador.x -= 5
    if keys[pygame.K_RIGHT] and jugador.right < ANCHO:
        jugador.x += 5
    if keys[pygame.K_UP] and jugador.top > 0:
        jugador.y -= 5
    if keys[pygame.K_DOWN] and jugador.bottom < ALTO:
        jugador.y += 5    

    #generar meteoritos
    if len(meteoritos) < 5:
        meteor = pygame.Rect(choice(range(0, ANCHO - meteorito_ancho)), 0,
                              meteorito_ancho, meteorito_alto)
        meteoritos.append(meteor)

    #mover meteoritos
    for meteor in meteoritos:
        meteor.y += 6
        if meteor.top > ALTO:
            meteoritos.remove(meteor)
            score += 1

        #detectar colisiones
        if jugador.colliderect(meteor):
            print("¡Colisión! Fin del juego.")
            running = False    
    #llenar la pantalla
    screen.blit(fondo_img, (0, 0))

   #dibujar el jugador
    screen.blit(jugador_image, (jugador.x, jugador.y))

    #dibujar meteoritos
    for meteor in meteoritos:
        screen.blit(enemigo_image, (meteor.x, meteor.y))    

    #Mostrar Puntuacion 
    score_text = font.render(f"Puntuacion: {score}", True, blanco)
    screen.blit(score_text, (10, 10)   )
    #actualizar pantalla
    pygame.display.flip()
    #controlar frames
    clock.tick(60)

 

pygame.quit()