import pygame 
from random import randint, choice
import os 
import sys

# CONFIGURAR LA RUTA CORRECTA
if getattr(sys, 'frozen', False):
    # Si es ejecutable de PyInstaller
    carpeta_juego = os.path.dirname(sys.executable)
else:
    # Si es script normal
    carpeta_juego = os.path.dirname(os.path.abspath(__file__))

os.chdir(carpeta_juego)

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
ANCHO = 800
ALTO = 600

screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Juego de Evitar Obstaculos")

# Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (255, 0, 0)
azul = (0, 0, 255)
verde = (0, 255, 0)
amarillo = (255, 255, 0)

# Cargar imágenes
try:
    jugador_image = pygame.image.load("burger.png").convert_alpha()
    jugador_image = pygame.transform.scale(jugador_image, (60, 60))
    
    enemigo_image = pygame.image.load("chubaka.png").convert_alpha()
    enemigo_image = pygame.transform.scale(enemigo_image, (100, 100))
    
    fondo_img = pygame.image.load("estrellas.png").convert()
    fondo_img = pygame.transform.scale(fondo_img, (ANCHO, ALTO))
    
    print("✓ Imágenes cargadas")
except Exception as e:
    print(f"Error cargando imágenes: {e}")
    pygame.quit()
    sys.exit()

# Cargar fuente
try:
    font = pygame.font.Font("star.TTF", 28)
except:
    font = pygame.font.Font(None, 36)

# HITBOXES MÁS PEQUEÑAS (ajusta estos valores para mayor/menor precisión)
JUGADOR_HITBOX_REDUCCION = 10  # Reducir hitbox del jugador
ENEMIGO_HITBOX_REDUCCION = 20   # Reducir hitbox de enemigos

# Función para obtener hitbox reducida
def get_hitbox(rect, reduccion):
    """Crea un rectángulo más pequeño centrado en el original"""
    return pygame.Rect(
        rect.x + reduccion,
        rect.y + reduccion,
        rect.width - (reduccion * 2),
        rect.height - (reduccion * 2)
    )

# Función para reiniciar el juego
def reiniciar_juego():
    jugador = pygame.Rect(ANCHO // 2 - 30, ALTO - 70, 60, 60)
    return {
        'jugador': jugador,
        'meteoritos_v': [],
        'meteoritos_h': [],
        'score': 0,
        'game_over': False,
        'vel_v': 6,
        'vel_h': 5
    }

# Inicializar el juego
juego = reiniciar_juego()

# Reloj
clock = pygame.time.Clock()

# PUNTUACIÓN PARA METEORITOS HORIZONTALES
PUNTUACION_HORIZONTALES = 10

# Variable para mostrar hitboxes (debug)
MOSTRAR_HITBOXES = False  # Cambia a True para ver las hitboxes

# Bucle principal
running = True 
while running:
    # EVENTOS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and juego['game_over']:
                juego = reiniciar_juego()
                print("Juego reiniciado")
            # Presiona 'H' para ver las hitboxes
            if event.key == pygame.K_h:
                MOSTRAR_HITBOXES = not MOSTRAR_HITBOXES

    # LÓGICA DEL JUEGO (solo si NO está en game over)
    if not juego['game_over']:
        # Movimiento del jugador
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and juego['jugador'].left > 0:
            juego['jugador'].x -= 7
        if keys[pygame.K_RIGHT] and juego['jugador'].right < ANCHO:
            juego['jugador'].x += 7
        if keys[pygame.K_UP] and juego['jugador'].top > 0:
            juego['jugador'].y -= 7
        if keys[pygame.K_DOWN] and juego['jugador'].bottom < ALTO:
            juego['jugador'].y += 7

        # Generar meteoritos verticales
        if len(juego['meteoritos_v']) < 5:
            nuevo = pygame.Rect(randint(0, ANCHO - 100), -100, 100, 100)
            juego['meteoritos_v'].append(nuevo)

        # Generar meteoritos horizontales
        if juego['score'] >= PUNTUACION_HORIZONTALES and randint(1, 40) == 1:
            if choice([True, False]):
                nuevo_h = {
                    'rect': pygame.Rect(ANCHO, randint(0, ALTO - 100), 100, 100),
                    'direccion': -1
                }
            else:
                nuevo_h = {
                    'rect': pygame.Rect(-100, randint(0, ALTO - 100), 100, 100),
                    'direccion': 1
                }
            juego['meteoritos_h'].append(nuevo_h)

        # Obtener hitbox del jugador
        jugador_hitbox = get_hitbox(juego['jugador'], JUGADOR_HITBOX_REDUCCION)

        # Actualizar meteoritos verticales
        meteoritos_v_temp = []
        for meteor in juego['meteoritos_v']:
            meteor.y += juego['vel_v']
            
            if meteor.top > ALTO:
                juego['score'] += 1
                if juego['score'] % 10 == 0:
                    juego['vel_v'] += 0.5
            else:
                meteoritos_v_temp.append(meteor)
                
            # Colisión con hitbox reducida
            meteor_hitbox = get_hitbox(meteor, ENEMIGO_HITBOX_REDUCCION)
            if jugador_hitbox.colliderect(meteor_hitbox):
                print(f"¡Colisión! Score: {juego['score']}")
                juego['game_over'] = True
        
        juego['meteoritos_v'] = meteoritos_v_temp

        # Actualizar meteoritos horizontales
        meteoritos_h_temp = []
        for meteor_h in juego['meteoritos_h']:
            meteor_h['rect'].x += juego['vel_h'] * meteor_h['direccion']
            
            if meteor_h['rect'].right < 0 or meteor_h['rect'].left > ANCHO:
                juego['score'] += 1
            else:
                meteoritos_h_temp.append(meteor_h)
                
            # Colisión con hitbox reducida
            meteor_h_hitbox = get_hitbox(meteor_h['rect'], ENEMIGO_HITBOX_REDUCCION)
            if jugador_hitbox.colliderect(meteor_h_hitbox):
                print(f"¡Colisión horizontal! Score: {juego['score']}")
                juego['game_over'] = True
        
        juego['meteoritos_h'] = meteoritos_h_temp

    # DIBUJAR TODO
    screen.blit(fondo_img, (0, 0))
    
    # Dibujar jugador
    screen.blit(jugador_image, juego['jugador'])
    
    # Dibujar meteoritos verticales
    for meteor in juego['meteoritos_v']:
        screen.blit(enemigo_image, meteor)
    
    # Dibujar meteoritos horizontales
    for meteor_h in juego['meteoritos_h']:
        screen.blit(enemigo_image, meteor_h['rect'])
    
    # MOSTRAR HITBOXES (para debug - presiona 'H' para activar/desactivar)
    if MOSTRAR_HITBOXES:
        # Hitbox del jugador
        jugador_hitbox = get_hitbox(juego['jugador'], JUGADOR_HITBOX_REDUCCION)
        pygame.draw.rect(screen, verde, jugador_hitbox, 2)
        
        # Hitboxes de meteoritos verticales
        for meteor in juego['meteoritos_v']:
            meteor_hitbox = get_hitbox(meteor, ENEMIGO_HITBOX_REDUCCION)
            pygame.draw.rect(screen, rojo, meteor_hitbox, 2)
        
        # Hitboxes de meteoritos horizontales
        for meteor_h in juego['meteoritos_h']:
            meteor_h_hitbox = get_hitbox(meteor_h['rect'], ENEMIGO_HITBOX_REDUCCION)
            pygame.draw.rect(screen, rojo, meteor_h_hitbox, 2)
    
    # Puntuación
    score_text = font.render(f"Puntuacion: {juego['score']}", True, blanco)
    screen.blit(score_text, (10, 10))
    
    # Advertencia meteoritos horizontales
    if (juego['score'] >= PUNTUACION_HORIZONTALES and 
        juego['score'] < PUNTUACION_HORIZONTALES + 3 and 
        not juego['game_over']):
        warning = font.render("¡METEORITOS LATERALES!", True, amarillo)
        screen.blit(warning, (ANCHO // 2 - warning.get_width() // 2, 50))
    
    # Game Over
    if juego['game_over']:
        overlay = pygame.Surface((ANCHO, ALTO))
        overlay.set_alpha(128)
        overlay.fill(negro)
        screen.blit(overlay, (0, 0))
        
        texto_go = font.render("GAME OVER", True, rojo)
        texto_score = font.render(f"Puntuacion: {juego['score']}", True, verde)
        texto_restart = font.render("Presiona ESPACIO", True, blanco)
        
        screen.blit(texto_go, (ANCHO // 2 - texto_go.get_width() // 2, ALTO // 2 - 80))
        screen.blit(texto_score, (ANCHO // 2 - texto_score.get_width() // 2, ALTO // 2 - 20))
        screen.blit(texto_restart, (ANCHO // 2 - texto_restart.get_width() // 2, ALTO // 2 + 40))
    
    # Actualizar
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
print("Juego cerrado correctamente")