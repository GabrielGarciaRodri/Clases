import os
os.system('cls')

print("Las jugadas posibles son: Piedra, Papel, Tijera. . . ")
player1 = input("Escriba su jugada player 1: ")
player2 = input("Escriba su jugada player 2: ")

empate = 0

if player1 == player2:
    empate += 1
    print("Empate")

# import random

# # Relaciones de ganador y perdedor
# relaciones = {
#     "piedra": "tijera",
#     "tijera": "papel",
#     "papel": "piedra"
# }

# # Elección preestablecida del usuario
# eleccion_usuario = "piedra"

# # Elección aleatoria de la máquina
# opciones = list(relaciones.keys())
# eleccion_maquina = random.choice(opciones)

# # Imprimir las elecciones
# print(f"Usuario eligió: {eleccion_usuario}")
# print(f"Máquina eligió: {eleccion_maquina}")

# # Determinar el ganador
# if eleccion_usuario == eleccion_maquina:
#     print("Empate")
# elif relaciones[eleccion_usuario] == eleccion_maquina:
#     print("¡Ganaste!")
# else:
#     print("La máquina gana.")

