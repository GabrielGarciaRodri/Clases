"""
Realizar un programa que permita leer el nombre de dos equipos  de la NBA e ingresar el puntaje total de canastas de cada equipo. El programa debe permitir
mostrar la siguiente informacion:
1. Nombre del equipo ganador
2. Nombre del equipo perdedor
3. Diferencia  de canastas entre los equipos

1. Leer equipo1
2. Leer equipo2
3. Ingresar puntaje equipo1
4. Ingresar puntaje equipo2
5. Resta de puntajes

"""
import os
os.system('cls')
equipo1 = str(input("Ingrese el nombre del primer equipo :")).upper()
equipo2 = str(input("Ingrese el nombre del segundo equipo: ")).upper()
cnt1 = int(input("Ingrese la cantidad de canastas del primer equipo: "))
cnt2 = int(input("Ingrese la cantidad de canastas del segundo equipo: "))

#cnt = abs(cnt1 - cnt2)

equipo_ganador = equipo1 if cnt1 > cnt2 else equipo2
equipo_perderor = equipo1 if cnt1 < cnt2 else equipo2


print("El equipo ganador es: ", equipo_ganador)
print("El equipo perdedor es: ", equipo_perderor)
print ("Diferencia de canastas entre los equipos: ", abs(cnt1 - cnt2))