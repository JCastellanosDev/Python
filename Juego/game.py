import pygame 
from random import randint, choice
import os 
import sys

# CONFIGURAR LA RUTA CORRECTA
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Cambiar al directorio del script
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
print(f"Directorio de trabajo: {os.getcwd()}")

# Inicializar Pygame
pygame.init()

# Estados del juego
MENU = 0
JUGANDO = 1
INSTRUCCIONES = 2
CREDITOS = 3
GAME_OVER = 4

# Estado inicial
estado_actual = MENU
opcion_menu = 0  # Opción seleccionada en el menú
ANCHO = 800
ALTO = 600

screen = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Burger vs Chubaka")

# Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (255, 0, 0)
azul = (0, 0, 255)
verde = (0, 255, 0)
amarillo = (255, 255, 0)

# Tamaños
jugador_ancho = 100
jugador_alto = 100

# Cargar imágenes
try:
    jugador_image = pygame.image.load(resource_path("burger.png")).convert_alpha()
    jugador_image = pygame.transform.scale(jugador_image, (jugador_ancho, jugador_alto))
    
    enemigo_image = pygame.image.load(resource_path("chubaka.png")).convert_alpha()
    
    fondo_img = pygame.image.load(resource_path("estrellas.png")).convert()
    fondo_img = pygame.transform.scale(fondo_img, (ANCHO, ALTO))
    
    print("✓ Imágenes cargadas")
except Exception as e:
    print(f"Error cargando imágenes: {e}")
    print(f"Buscando en: {os.getcwd()}")
    print(f"Archivos disponibles: {os.listdir('.')}")
    pygame.quit()
    sys.exit()

try:
    # Asegurarse de que el mixer está inicializado
    pygame.mixer.init()
    
    # Cargar sonido de game over
    sonido_game_over = pygame.mixer.Sound("game over.wav")  
    sonido_game_over.set_volume(0.7) 
    
    print("✓ Sonidos cargados")
except Exception as e:
    print(f"⚠ Error cargando sonidos: {e}")
    sonido_game_over = None

# Cargar fuente
try:
    font = pygame.font.Font(resource_path("star.TTF"), 28)
    print("✓ Fuente cargada")
except Exception as e:
    print(f"⚠ Fuente no encontrada: {e}, usando fuente por defecto")
    font = pygame.font.Font(None, 36)

# HITBOXES
JUGADOR_HITBOX_REDUCCION = 20
ENEMIGO_HITBOX_REDUCCION = 35

def get_hitbox(rect, reduccion):
    return pygame.Rect(
        rect.x + reduccion,
        rect.y + reduccion,
        rect.width - (reduccion * 2),
        rect.height - (reduccion * 2)
    )

def reiniciar_juego():
    jugador = pygame.Rect(ANCHO // 2 - jugador_ancho // 2, ALTO - jugador_alto - 10, 
                          jugador_ancho, jugador_alto)
    return {
        'jugador': jugador,
        'meteoritos_v': [],
        'meteoritos_h': [],
        'score': 0,
        'game_over': False,
    }

def dibujar_menu_principal(screen, font, opcion_seleccionada):
    """Dibuja el menú principal del juego"""
    # Fondo
    screen.blit(fondo_img, (0, 0))
    
    # Overlay semi-transparente
    overlay = pygame.Surface((ANCHO, ALTO))
    overlay.set_alpha(150)
    overlay.fill((0, 0, 50))
    screen.blit(overlay, (0, 0))
    
    # Título del juego
    try:
        titulo_font = pygame.font.Font("retro?.otf", 60)
    except: 
        titulo_font = pygame.font.Font(None, 60)
    
    titulo = titulo_font.render("BURGER vs CHUBAKA", True, amarillo)
    screen.blit(titulo, (ANCHO // 2 - titulo.get_width() // 2, 100))
    
    # Subtítulo
    subtitulo = font.render("La venganza de chubaka", True, blanco)
    screen.blit(subtitulo, (ANCHO // 2 - subtitulo.get_width() // 2, 180))
    
    # Opciones del menú
    opciones = ["JUGAR", "INSTRUCCIONES", "CREDITOS", "SALIR"]
    
    for i, texto in enumerate(opciones):
        # Color según si está seleccionada
        if i == opcion_seleccionada:
            color = amarillo
            prefijo = "> "
        else:
            color = blanco
            prefijo = "  "
        
        texto_renderizado = font.render(prefijo + texto, True, color)
        y_pos = 300 + (i * 60)
        screen.blit(texto_renderizado, (ANCHO // 2 - texto_renderizado.get_width() // 2, y_pos))
    
    # Instrucciones de navegación
    try:
        instrucciones_font = pygame.font.Font("retro?.otf", 24)
    except:
        instrucciones_font = pygame.font.Font(None, 24)
    
    instrucciones = instrucciones_font.render("Usa ↑↓ para navegar, ENTER para seleccionar", True, (150, 150, 150))
    screen.blit(instrucciones, (ANCHO // 2 - instrucciones.get_width() // 2, ALTO - 50))


def dibujar_instrucciones(screen, font):
    """Dibuja la pantalla de instrucciones"""
    screen.blit(fondo_img, (0, 0))
    
    overlay = pygame.Surface((ANCHO, ALTO))
    overlay.set_alpha(200)
    overlay.fill((0, 0, 50))
    screen.blit(overlay, (0, 0))
    
    # Título
    titulo = font.render("INSTRUCCIONES", True, amarillo)
    screen.blit(titulo, (ANCHO // 2 - titulo.get_width() // 2, 50))
    
    # Instrucciones
    instrucciones_font = pygame.font.Font("retro?.otf", 28)
    instrucciones = [
        "CONTROLES:",
        "",
        "← → ↑ ↓ - Mover la hamburguesa",
        "P - Pausar el juego",
        "H - Mostrar hitboxes (debug)",
        "",
        "OBJETIVO:",
        "",
        "Evita que chubaka te coma",
        "Gana puntos por cada chubaka esquivado",
        "A partir de 10 puntos aparecen meteoritos horizontales",
        "La velocidad aumenta cada 10 puntos",
        "",
        "¡Sobrevive el mayor tiempo posible!"
    ]
    
    y_pos = 130
    for linea in instrucciones:
        if linea == "CONTROLES:" or linea == "OBJETIVO:":
            color = amarillo
        else: 
            color = blanco
        
        texto = instrucciones_font.render(linea, True, color)
        screen.blit(texto, (ANCHO // 2 - texto.get_width() // 2, y_pos))
        y_pos += 35
    
    # Volver
    volver = font.render("Presiona ESC para volver", True, verde)
    screen.blit(volver, (ANCHO // 2 - volver.get_width() // 2, ALTO - 60))


def dibujar_creditos(screen, font):
    """Dibuja la pantalla de créditos"""
    screen.blit(fondo_img, (0, 0))
    
    overlay = pygame.Surface((ANCHO, ALTO))
    overlay.set_alpha(200)
    overlay.fill((0, 0, 50))
    screen.blit(overlay, (0, 0))
    
    # Título
    titulo = font.render("CREDITOS", True, amarillo)
    screen.blit(titulo, (ANCHO // 2 - titulo.get_width() // 2, 100))
    
    # Créditos
    creditos_font = pygame.font.Font("retro?.otf", 30)
    creditos = [
        "",
        "Desarrollado por: JCastellanosDev",
        "",
        "¡Gracias por jugar!"
    ]
    
    y_pos = 180
    for linea in creditos:
        texto = creditos_font.render(linea, True, blanco)
        screen.blit(texto, (ANCHO // 2 - texto.get_width() // 2, y_pos))
        y_pos += 40
    
    # Volver
    volver = font.render("Presiona ESC para volver", True, verde)
    screen.blit(volver, (ANCHO // 2 - volver.get_width() // 2, ALTO - 60))

juego = reiniciar_juego()
clock = pygame.time.Clock()
PUNTUACION_HORIZONTALES = 10
MOSTRAR_HITBOXES = False

# Cache de imágenes redimensionadas
imagenes_enemigo_cache = {}

def get_enemigo_image(tamaño):
    """Obtiene imagen de enemigo del tamaño especificado (usa cache)"""
    if tamaño not in imagenes_enemigo_cache:
        imagenes_enemigo_cache[tamaño] = pygame.transform.scale(
            enemigo_image, (tamaño, tamaño)
        )
    return imagenes_enemigo_cache[tamaño]

# Bucle principal
running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            # NAVEGACIÓN DEL MENÚ
            if estado_actual == MENU:
                if event.key == pygame.K_UP:
                    opcion_menu = (opcion_menu - 1) % 4
                elif event.key == pygame.K_DOWN:
                    opcion_menu = (opcion_menu + 1) % 4
                elif event.key == pygame.K_RETURN:
                    if opcion_menu == 0:  # JUGAR
                        estado_actual = JUGANDO
                        juego = reiniciar_juego()
                        print("Iniciando juego...")
                    elif opcion_menu == 1:  # INSTRUCCIONES
                        estado_actual = INSTRUCCIONES
                    elif opcion_menu == 2:  # CREDITOS
                        estado_actual = CREDITOS
                    elif opcion_menu == 3:  # SALIR
                        running = False
            
            # VOLVER AL MENÚ desde INSTRUCCIONES o CREDITOS
            elif estado_actual == INSTRUCCIONES or estado_actual == CREDITOS:
                if event.key == pygame.K_ESCAPE:
                    estado_actual = MENU
            
            # CONTROLES DEL JUEGO
            elif estado_actual == JUGANDO:
                if event.key == pygame.K_SPACE and juego['game_over']:
                    estado_actual = MENU
                    opcion_menu = 0
                    print("Volviendo al menú...")
                if event.key == pygame.K_h:
                    MOSTRAR_HITBOXES = not MOSTRAR_HITBOXES
                    print(f"Hitboxes: {'Visible' if MOSTRAR_HITBOXES else 'Oculto'}")
                if event.key == pygame.K_ESCAPE:
                    estado_actual = MENU
                    opcion_menu = 0

    # RENDERIZADO SEGÚN ESTADO
    if estado_actual == MENU:
        dibujar_menu_principal(screen, font, opcion_menu)
    
    elif estado_actual == INSTRUCCIONES:
        dibujar_instrucciones(screen, font)
    
    elif estado_actual == CREDITOS:
        dibujar_creditos(screen, font)
    
    elif estado_actual == JUGANDO:
        if not juego['game_over']:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and juego['jugador'].left > 0:
                juego['jugador'].x -= 7
            if keys[pygame.K_RIGHT] and juego['jugador'].right < ANCHO:
                juego['jugador'].x += 7
            if keys[pygame.K_UP] and juego['jugador'].top > 0:
                juego['jugador'].y -= 7
            if keys[pygame.K_DOWN] and juego['jugador'].bottom < ALTO:
                juego['jugador'].y += 7

            # METEORITOS VERTICALES
            if randint(1, 30) == 1:
                pos_x = randint(0, ANCHO - 150)
                velocidad_aleatoria = randint(3, 10)
                tamaño_aleatorio = choice([90, 100, 120, 140, 160])
                
                nuevo = {
                    'rect': pygame.Rect(pos_x, -tamaño_aleatorio, tamaño_aleatorio, tamaño_aleatorio),
                    'velocidad': velocidad_aleatoria,
                    'tamaño': tamaño_aleatorio
                }
                
                juego['meteoritos_v'].append(nuevo)

            # METEORITOS HORIZONTALES
            if juego['score'] >= PUNTUACION_HORIZONTALES and randint(1, 60) == 1:
                desde_derecha = choice([True, False])
                pos_y = randint(0, ALTO - 120)
                velocidad_aleatoria = randint(3, 9)
                tamaño_aleatorio = choice([90, 100, 110, 130])
                
                if desde_derecha:
                    nuevo_h = {
                        'rect': pygame.Rect(ANCHO, pos_y, tamaño_aleatorio, tamaño_aleatorio),
                        'direccion': -1,
                        'velocidad': velocidad_aleatoria,
                        'tamaño': tamaño_aleatorio
                    }
                else:
                    nuevo_h = {
                        'rect': pygame.Rect(-tamaño_aleatorio, pos_y, tamaño_aleatorio, tamaño_aleatorio),
                        'direccion': 1,
                        'velocidad': velocidad_aleatoria,
                        'tamaño': tamaño_aleatorio
                    }
                
                juego['meteoritos_h'].append(nuevo_h)

            jugador_hitbox = get_hitbox(juego['jugador'], JUGADOR_HITBOX_REDUCCION)

            # Actualizar meteoritos verticales
            meteoritos_v_temp = []
            for meteor in juego['meteoritos_v']:
                meteor['rect'].y += meteor['velocidad']
                
                if meteor['rect'].top > ALTO:
                    juego['score'] += 1
                else:
                    meteoritos_v_temp.append(meteor)
                    
                meteor_hitbox = get_hitbox(meteor['rect'], ENEMIGO_HITBOX_REDUCCION)
                if jugador_hitbox.colliderect(meteor_hitbox):
                    if sonido_game_over: 
                        sonido_game_over.play()
                    print(f"¡Colisión vertical! Score: {juego['score']}")
                    juego['game_over'] = True
            
            juego['meteoritos_v'] = meteoritos_v_temp

            # Actualizar meteoritos horizontales
            meteoritos_h_temp = []
            for meteor_h in juego['meteoritos_h']:
                meteor_h['rect'].x += meteor_h['velocidad'] * meteor_h['direccion']
                
                if meteor_h['rect'].right < 0 or meteor_h['rect'].left > ANCHO:
                    juego['score'] += 1
                else:
                    meteoritos_h_temp.append(meteor_h)
                    
                meteor_h_hitbox = get_hitbox(meteor_h['rect'], ENEMIGO_HITBOX_REDUCCION)
                if jugador_hitbox.colliderect(meteor_h_hitbox):
                    if sonido_game_over: 
                        sonido_game_over.play()
                    print(f"¡Colisión horizontal! Score: {juego['score']}")
                    juego['game_over'] = True
            
            juego['meteoritos_h'] = meteoritos_h_temp

        # DIBUJAR JUEGO
        screen.blit(fondo_img, (0, 0))
        screen.blit(jugador_image, juego['jugador'])
        
        # Dibujar meteoritos
        for meteor in juego['meteoritos_v']:
            enemigo_img = get_enemigo_image(meteor['tamaño'])
            screen.blit(enemigo_img, meteor['rect'])
        
        for meteor_h in juego['meteoritos_h']:
            enemigo_img = get_enemigo_image(meteor_h['tamaño'])
            screen.blit(enemigo_img, meteor_h['rect'])
        
        # Hitboxes (debug)
        if MOSTRAR_HITBOXES:
            jugador_hitbox = get_hitbox(juego['jugador'], JUGADOR_HITBOX_REDUCCION)
            pygame.draw.rect(screen, verde, jugador_hitbox, 2)
            
            for meteor in juego['meteoritos_v']:
                meteor_hitbox = get_hitbox(meteor['rect'], ENEMIGO_HITBOX_REDUCCION)
                pygame.draw.rect(screen, rojo, meteor_hitbox, 2)
            
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
            texto_restart = font.render("Presiona ESPACIO para volver al menu", True, blanco)
            
            screen.blit(texto_go, (ANCHO // 2 - texto_go.get_width() // 2, ALTO // 2 - 80))
            screen.blit(texto_score, (ANCHO // 2 - texto_score.get_width() // 2, ALTO // 2 - 20))
            screen.blit(texto_restart, (ANCHO // 2 - texto_restart.get_width() // 2, ALTO // 2 + 40))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
print("Juego cerrado correctamente")