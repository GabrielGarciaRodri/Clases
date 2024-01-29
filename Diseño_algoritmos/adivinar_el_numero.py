import os
os.system('cls')

from random import randrange
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
        print(f"Es menor que {intento}")
        