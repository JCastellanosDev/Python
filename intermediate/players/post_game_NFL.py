# Sistema Interactivo de Gestión de Jugadores
from playerss import players


# Mostrar todas las posiciones
print("=== POSICIONES DE JUGADORES ===")
for player in players:
    print(f"{player['name']}: {player['position']}")

print("\n" + "="*40 + "\n")

# Permitir al usuario seleccionar y actualizar un jugador
print("=== SELECCIONAR JUGADOR PARA ACTUALIZAR ===")
print("\nJugadores disponibles:")
for i, player in enumerate(players, 1):
    print(f"{i}. {player['name']} - {player['position']} (#{player['jersey_number']})")

# Solicitar selección del usuario
while True:
    try:
        opcion = int(input("\nIngresa el número del jugador que deseas actualizar (1-{}): ".format(len(players))))
        if 1 <= opcion <= len(players):
            jugador_seleccionado = players[opcion - 1]
            break
        else:
            print(f"Por favor, ingresa un número entre 1 y {len(players)}")
    except ValueError:
        print("Por favor, ingresa un número válido")

# Mostrar estadísticas actuales
print(f"\n--- Jugador seleccionado: {jugador_seleccionado['name']} ---")
print(f"Posición: {jugador_seleccionado['position']}")
print(f"Número de camiseta: {jugador_seleccionado['jersey_number']}")
print(f"Yardas actuales: {jugador_seleccionado['yards']}")
print(f"Touchdowns actuales: {jugador_seleccionado['touchdowns']}")

# Permitir al usuario actualizar las estadísticas
print("\n¿Qué deseas hacer?")
print("1. Añadir yardas y touchdowns")
print("2. Establecer nuevos valores totales")

while True:
    try:
        modo = int(input("\nElige una opción (1 o 2): "))
        if modo in [1, 2]:
            break
        else:
            print("Por favor, elige 1 o 2")
    except ValueError:
        print("Por favor, ingresa un número válido")

if modo == 1:
    # Modo: Añadir a las estadísticas existentes
    print("\n--- AÑADIR ESTADÍSTICAS ---")
    while True:
        try:
            nuevas_yardas = int(input("¿Cuántas yardas deseas añadir?: "))
            if nuevas_yardas >= 0:
                break
            else:
                print("Por favor, ingresa un número positivo")
        except ValueError:
            print("Por favor, ingresa un número válido")
    
    while True:
        try:
            nuevos_touchdowns = int(input("¿Cuántos touchdowns deseas añadir?: "))
            if nuevos_touchdowns >= 0:
                break
            else:
                print("Por favor, ingresa un número positivo")
        except ValueError:
            print("Por favor, ingresa un número válido")
    
    jugador_seleccionado['yards'] += nuevas_yardas
    jugador_seleccionado['touchdowns'] += nuevos_touchdowns

else:
    # Modo: Establecer nuevos valores totales
    print("\n--- ESTABLECER NUEVOS VALORES ---")
    while True:
        try:
            nuevas_yardas = int(input("Ingresa el nuevo total de yardas: "))
            if nuevas_yardas >= 0:
                break
            else:
                print("Por favor, ingresa un número positivo")
        except ValueError:
            print("Por favor, ingresa un número válido")
    
    while True:
        try:
            nuevos_touchdowns = int(input("Ingresa el nuevo total de touchdowns: "))
            if nuevos_touchdowns >= 0:
                break
            else:
                print("Por favor, ingresa un número positivo")
        except ValueError:
            print("Por favor, ingresa un número válido")
    
    jugador_seleccionado['yards'] = nuevas_yardas
    jugador_seleccionado['touchdowns'] = nuevos_touchdowns

# Mostrar estadísticas actualizadas
print(f"\n✓ Estadísticas actualizadas de {jugador_seleccionado['name']}:")
print(f"  Yardas: {jugador_seleccionado['yards']}")
print(f"  Touchdowns: {jugador_seleccionado['touchdowns']}")

print("\n" + "="*40 + "\n")

#  Calcular promedios
print("=== ESTADÍSTICAS PROMEDIO DEL EQUIPO ===")

total_yards = sum(player['yards'] for player in players)
total_touchdowns = sum(player['touchdowns'] for player in players)
num_players = len(players)

average_yards = total_yards / num_players
average_touchdowns = total_touchdowns / num_players

print(f"Promedio de yardas por jugador: {average_yards:.2f}")
print(f"Promedio de touchdowns por jugador: {average_touchdowns:.2f}")
print(f"Total de jugadores: {num_players}")

# Mostrar todos los jugadores con sus estadísticas actualizadas
print("\n=== ESTADÍSTICAS COMPLETAS DEL EQUIPO ===")
for player in players:
    print(f"{player['name']} ({player['position']}): {player['yards']} yardas, {player['touchdowns']} TDs")