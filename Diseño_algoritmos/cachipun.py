import os
os.system('cls')

#Crea la funcion para predefinir que cosa le gana a que
#usando el diccionario de opciones, y con el if retorna 
#las opciones que los jugadores eligieron
def ganador(player1, player2):
    opciones = {
        "piedra": "tijera",
        "tijera": "papel",
        "papel" : "piedra"
    }

    if opciones[player1] == player2:
        return 'player1'
    elif opciones[player2] == player1:
        return 'player2'
    else:
        player1 == player2
        return 'empate'
    
puntaje1 = 0
puntaje2 = 0
limite = 3
print("Las jugadas posibles son: Piedra, Papel, Tijera. . . ")


while puntaje1 < limite and puntaje2 < limite:
    player1 = input("Escriba su jugada player 1: ").lower()
    player2 = input("Escriba su jugada player 2: ").lower()

    jugada = ganador(player1, player2)
    print(f"ganador de ronda: {jugada}")

    if jugada == 'player1':
        puntaje1 += 1
    
    elif jugada == 'player2':
        puntaje2 += 1   

if puntaje1 > puntaje2:
    print (f"El ganador es el jugador 1")

else:
    print (f"el ganador es el jugador 2 ")






