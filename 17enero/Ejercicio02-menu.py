import os
os.system('cls')
titulo = """
----------------------------
-  OPERACIONES CON LISTAS  -
----------------------------
"""
opciones = "1. Agregar camper\n2. Eliminar camper\n3. Buscar camper\n4. Salir"
isPay = True
campers = []
while isPay :
    os.system('cls')
    print(titulo)
    print(opciones)
    op = int(input(":"))
    if (op == 1):
        id = str(len(campers)).zfill(5)
        nombre = input("Ingrese Nombre del Camper :")
        campers.append([id,nombre])
        print(campers)
        os.system('pause')
    elif (op == 2):
        nombre = input("Ingrese Nombre del Camper a Eliminar:")
        for i,item in enumerate(campers):
            if (nombre in item):
                campers.pop(i)
                print(campers)
                os.system('pause')
                break
            else :
                print("El camper digitado no se encuentra en la lista")
    elif (op == 3):
        nombre = input("Ingrese Nombre del Camper a Buscar:")
        for item in campers:
            if (nombre in item):
                print("Codigo : ",(item[0]))
                print("Codigo : ",(item[1]))
                #print("El nombre del camper es: ", (item.index(nombre)), "Se encuentra en la posicion :", (item.index(nombre)))
                os.system('pause')
    elif (op == 4):
        os.system('cls')
        isPay = False
        print("Gracias marica(de pana) por usar mi programa, la buena parce . . .")
        os.system('pause')
    else:
        os.system('cls')
        print("La opcion no es valida")
        os.system('pause')