"""
LA FEDERACION COLOMBIANA DE FUTBOL DESEA CREAR UN PROGRAMA QUE LE PERMITA
LLEVAR EL CONTROL Y REGISTRO DE TODOS LOS EQUIPOS QUE SE ENCUENTRAN
PARTICIPANDO EN LA LIGA BETPLAY. LA FEDERACION DESEA ORGANIZAR EL TORNEO
TENIENDO EN CUENTA LA SIGUIENTE INFORMACION:

    - NOMBRE DEL EQUIPO
    - PJ
    - PG
    - PP
    - PE
    - GF
    - GC
    - TP

REQUERIMIENTOS:
1. EL PROGRAMA DEBE PERMITIR REGISTRAR CADA UNO DE LOS EQUIPOS QUE VAN A
PARTICIPAR EN EL TORNEO, TENGA EN CUENTA QUE AL MOMENTO DE REGISTRAR CADA
EQUIPO LAS VARIABLES DE PJ,PG,PP,PE,GF,GC,TP DEBEN SER 0

2. REGISTRO DE FECHA. EL REGISTRO DE FECHAS SE DEBE INGRESAR LOS EQUIPOS
QUE SE ENFRENTARON. EL PROGRAMA DEBE PERMITIR SELECCIONAR QUE EQUIPO JUGO DE
LOCAL Y QUE EQUIPO JUGO DE VISITANTE. ADEMAS SE DEBE REGISTRAR EL MARCADOR DE
CADA UNO DE LOS EQUIPOS. EL PROGRAMA DEBE DETERMINAR CUAL FUE EL EQUIPO
GANADOR Y CUAL ES EL PERDEDOR Y ASIGNAR LOS VALORES CORRESPONDIENTES EN LA
TABLA DE POSICIONES. RECUERDE QUE CADA PARTIDO GANADO EQUIVALE A 3 PUNTO
Y LOS EMPATADOS EQUIVALEN A 1 PUNTO.

3. REPORTES
    A. NOMBRE DEL EQUIPO QUE MAS GOLES ANOTO
    B. NOMBRE DEL EQUIPO QUE MAS PUNTOS TIENE
    C. NOMBRE DEL EQUIPO QUE MAS PARTIDOS GANO
    D. TOTAL DE GOLES ANOTADOS POR TODOS LOS EQUIPOS
    E. PROMEDIO DE GOLES ANOTADOS EN EL TORNEO

ANALISIS:
-Programa control y registro x
-Registrar equipos, otros parametros = 0 (Menu, equipo) x
-Registrar fechas   (Registro de fechas) x 
-Equipos que se enfrentaron (Preguntar en el registro de fechas) x
-Seleccionar local o visitante  (Menu local o visitante) x
-Registrar marcador cada equipo (Menu marcador cada equipo) x 
-Determinar equipo ganador y equipo perdedor mismo apartado (Mensaje equipo ganador y equipo perdedor) x
-Asignar valores a las tablas   (Procesar los datos) x
-Partido ganado +3 , empatado +1    (Calcular los datos)
-REPORTES
    A. Que equipo anoto mas goles   (Reporte anotar)
    B. Que equipo tiene mas puntos  (Reporte puntos)
    C. Que equipo gano mas partidos (Reporte mas ganador)
    D. Total de goles anotados por todos los equipos  (Total goles) 
    E. Promedio de goles    (Promedio goles)
"""
import os
from tabulate import tabulate
os.system('cls')
titulo = """
-------------------------
-  PROGRAMA DE EQUIPOS  -
-------------------------
- 1. Registrar equipos  -
- 2. Registro fechas    -
- 3. Consultar Marcador -
- 4. Salir              -
-------------------------
"""
gregistro = int(0)
isMenu = True
equipos = []
registro = []
while isMenu:

    pj = int(0)
    pg = int(0)
    pp = int(0)
    pe = int(0)
    gf = int(0)
    gc = int(0)
    tp = int(0)
    
    print(titulo)
    op = int(input(": "))
    
    if op == 1:
        id = str(len(equipos)).zfill(5)
        nombre = input("Ingrese el nombre del equipo: ")
        equipos.append([id,nombre,pj,pg,pp,pe,gf,gc,tp])
        #                0,     1, 2, 3, 4, 5, 6, 7, 8
        
    elif op ==2:
        
        nombre1 = input("Ingrese el nombre del equipo local: ")
        for item in equipos:
            if (nombre1 in item):
                print("Ingrese los goles anotados")
                #Obtener los goles anotados del equipo 1
                gf1 = int(input(":"))
                #Obtener los goles almacenados en el array
                gfavor1 = item[6]
                #Sumar los goles
                gfavor1 += gf1
                #Almacenarlos en el array
                item[6] = gfavor1
                #Añadir los goles en el array registro
        nombre2 = input("Ingrese el nombre del equipo visitante: ")
        for item1 in equipos:
            if (nombre2 in item1):
                print("Ingrese los goles anotados")
                #Obtener los goles anotados del equipo 2
                gf2 = int(input(":"))
                #Obtener los goles almacenados en el array
                gfavor2 = item1[6]
                #Sumas los goles
                gfavor2 += gf2
                #Almacenarlos en el array
                item1[6] = gfavor2
                
        #Si el equipo 1 gana
        if gf1 > gf2 :
            for item2 in equipos:
                if (nombre1 in item2):
                    #Sumar los partidos jugados
                    item2[2] = item2[2] + 1
                    #Añadir a partidos ganados
                    item2[3] = item2[3] + 1
                    #Añadir a goles contra
                    #Obtener los goles almacenados en el array
                    gcontra1 = item2[7]
                    #Sumas los goles
                    gcontra1 += gf2
                    #Almacenarlos en el array
                    item2[7] = gcontra1
                    #Añadir los puntos
                    item2[8] = item2[8] + 3
                if (nombre2 in item2):
                    #Sumar los partidos jugados
                    item2[2] = item2[2] + 1
                    #Sumar los partidos perdidos
                    item2[4] = item2[4] + 1
                    #Añadir a goles contra
                    #Obtener los goles almacenados en el array
                    gcontra2 = item2[7]
                    #Sumas los goles
                    gcontra2 += gf1
                    #Almacenarlos en el array
                    item2[7] = gcontra2
            print("El equipo ganador es: ",nombre1)
            print("El equipo perdedor es: ",nombre2)
            
        #Si el equipo 2 gana
        elif gf2 > gf1 :
            for item3 in equipos:
                if (nombre2 in item3):
                    #Sumar los partidos jugados
                    item3[2] = item3[2] + 1
                    #Añadir a partidos ganados
                    item3[3] = item3[3] + 1
                    #Añadir a goles contra
                    #Obtener los goles almacenados en el array
                    gcontra2 = item3[7]
                    #Sumas los goles
                    gcontra2 += gf1
                    #Almacenarlos en el array
                    item3[7] = gcontra2
                    #Añadir los puntos
                    item3[8] = item[8] + 3
                if (nombre1 in item3):
                    #Sumar los partidos perdidos
                    item3[4] = item3[4] + 1
                    #Sumar los partidos jugados
                    item3[2] = item3[2] + 1
                    #Añadir a goles contra
                    #Obtener los goles almacenados en el array
                    gcontra1 = item3[7]
                    #Sumas los goles
                    gcontra1 += gf2
                    #Almacenarlos en el array
                    item3[7] = gcontra1
            print("El equipo ganador es: ",nombre2)
            print("El equipo perdedor es: ",nombre1)
        #Si empatan
        elif gf1 == gf2 :
            for item4 in equipos:
                if (nombre1 in item4):
                    #Sumar los partidos jugados
                    item4[2] = item4[2] + 1
                    #Añadir a partidos empatados
                    item4[5] = item4[5] + 1
                    #Añadir a goles contra
                    #Obtener los goles almacenados en el array
                    gcontra1 = item4[7]
                    #Sumas los goles
                    gcontra1 += gf2
                    #Almacenarlos en el array
                    item4[7] = gcontra1
                    #Añadir los puntos
                    item4[8] = item4[8] + 1
                if (nombre2 in item4):
                    #Sumar los partidos jugados
                    item4[2] = item4[2] + 1
                    #Sumar los partidos empatados
                    item4[5] = item4[5] + 1
                    #Añadir a goles contra
                    #Obtener los goles almacenados en el array
                    gcontra2 = item4[7]
                    #Sumas los goles
                    gcontra2 += gf1
                    #Añadir los puntos
                    #Almacenarlos en el array
                    item4[7] = gcontra2
                    #Añadir los puntos 
                    item4[8] = item4[8] + 1
            print("Los equipos han quedado empatados")

    elif op ==3:
        
        #equipogoles = emax[1]
        #print(equipogoles)
        print(tabulate(equipos,headers=['ID','EQUIPO','PJ','PG','PP','PE','GF','GC','TP']))
        gmax = max(equipos, key=lambda x: x[7])[1]
        print("El equipo con mas puntos es: ",gmax)
        ptmax = max(equipos, key=lambda x: x[8])[1]
        print("El equipo con mas puntos es: ",ptmax)
        pmax = max(equipos, key=lambda x: x[3])[1]
        print("El equipo con mas puntos es: ",pmax)
        suma = int(0)
        columna = 6
        for i in equipos:
            suma += i[6]
            pganados = +i[3]
        print("El total de goles es :", suma)
        #Terminar promedio y probar
        
        print("El promedio de goles es:")

        os.system('pause')
    elif op == 4:
        isMenu = False
        os.system('pause')
    else:
        os.system('cls')
        print("La opcion no es valida")
        os.system('pause')

