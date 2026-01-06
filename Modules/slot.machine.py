import random
import os # Importa el módulo os para controlar sistema operativo

def clear_screen(): # Función para limpiar la pantalla
     os.system("clear" if os.name == "posix" else "cls")

def play():
    clear_screen()
    print("\nWelcome to the Slot Machine!")

    symbols = ['🍒', '🍇', '🍉', "7️⃣"]

    results = random.choices(symbols, k=3)


    print(results[0] + "|" + results[1] + "|" + results[2])# para mostrar los resultados y el [] sirve para acceder a los elementos de la lista

    if results[0] == "7️⃣" and results[1] == "7️⃣" and results[2] == "7️⃣":
        print("JACKPOT! You won the grand prize!")
    else:
        print("Better luck next time!")

while True: # Loop para poder jugar varias veces
        play() # Llama a la función play para iniciar el juego

        continue_play = input("\nDo you want to play again? (y/n): ").upper()# Convierte la entrada a mayúsculas para facilitar la comparación
        if continue_play != "Y":
            print("Thanks for playing! Goodbye!")
            break
             
             

