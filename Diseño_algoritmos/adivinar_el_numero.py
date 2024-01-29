import os
os.system('cls')

""""from random import randrange
n = randrange(101)

intentos = 0

while True:
    intento = int(input("Adivina el numero: "))
    intentos += 1

    if intento == n:
        print(f"Felicidades, adivinaste en {intentos} intentos!!!")
        break
    elif intento < n:
        print(f"Es mayor que {intento}")
    else:
        intento > n
        print(f"Es menor que {intento}")"""

#Ahora la num_comp adivina
import random

num = int(input("Piensa en un número entre 1 y 100. Ingrésalo aquí: "))
    
lim_inf = 1
lim_sup = 100
intentos = 0
    
while True:
    num_comp = random.randint(lim_inf, lim_sup)
    print(f"¿Es {num_comp} tu número?")
        
    respuesta = input("Ingresa '<', '>', o '=': ")
    intentos += 1
        
    if respuesta == "=":
        print(f"¡Adivine en {intentos} intentos B-)")
        break
    elif respuesta == "<":
        lim_sup = num_comp - 1
    elif respuesta == ">":
        lim_inf = num_comp + 1
    else:
        print("Por favor, ingresa '<', '>', o '='.")
        
