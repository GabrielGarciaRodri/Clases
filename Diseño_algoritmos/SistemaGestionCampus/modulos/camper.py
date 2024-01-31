#Guarda la funcionalidad del CRUD
import os
from tabulate import tabulate
from .variables import save, getAll, camper

def create():
    
    os.system("cls")
    print("""
          *********************************
          *     FORMULARIO DEL CAMPER     *
          *********************************
          """)
    save({
        "Nombre" :input("Ingrese el nombre del camper: "),
        "Apellido" : input("Ingrese el apellido del camper: "),
        "Edad" : int(input("Ingrese la edad del camper: "))
    })
    os.system('pause')
    
def read(codigo=None):
    os.system('cls')
    
    if(not codigo != None):
        print(f"""
             *********************************
             *        TABLA DEL CAMPER       *
             ********************************* 
            """)

        for i, val in enumerate (getAll()):
            print(f"""
            __________________________________
            Codigo: {i+1}  
            Nombre: {val.get("Nombre")}
            Apellido: {val.get("Apellido")}
            Edad: {val.get("Edad")}
            __________________________________
            """)
    else:
        #codigo -1 se utiliza para retroceder una posicion en la lista es decir 0-1
        val = getAll()[codigo-1]
        print(f"""
            __________________________________
            Codigo: {codigo}  
            Nombre: {val.get("Nombre")}
            Apellido: {val.get("Apellido")}
            Edad: {val.get("Edad")}
            __________________________________
            """)
    os.system('pause')
    
def update():
    print("El camper se actualizó")

def delete():
    
    bandera = True
    while (bandera):
        os.system('cls')
        read()
        print("""
        *********************************
        *        ELIMINAR CAMPER        *
        ********************************* 
            """)
        codigo = int(input(f"Ingrese el codigo del camper que desea borrar:\n "))
        read(codigo)
        print("""
            ¿Está seguro que desea eliminar al camper?
            1. Si
            2. No
            3. Cancelar
            """)
        opc = int(input())
        match(opc):
                #Con getAll toma el array y con pop elimina el(codigo)
            case 1: 
                val = camper.pop(codigo-1)
                os.system('cls')
                print(f"""
                    Camper eliminado:
                    __________________________________
                    Codigo: {codigo}  
                    Nombre: {val.get("Nombre")}
                    Apellido: {val.get("Apellido")}                            
                    Edad: {val.get("Edad")}
                    __________________________________
                    """)
                os.system("pause")
                bandera = False
                
            case 3:
                bandera = False
    
def menu():
    
    
    """El siguiente try permite repetir la opcion en caso de que
    El usuario se equivoque"""
    while True:
        #Enumera el array menu
        os.system("cls")
        print("""
             *********************************
             *        MENU DEL CAMPER        *
             ********************************* 
            """)
        menu = ["Crear","Buscar","actualizar","Borrar","Salir"]

        print("".join([f"{i+1}. {val}\n" for i, val in enumerate(menu)]))
        try: 
            opc = int(input())
            if(opc<=len(menu) and opc>0):
                match(opc):
                    case 1:create()
                    case 2:read()
                    case 3:update()
                    case 4:delete()
                    case 5:
                        print("Gracias por usar<3")
                        break
                
        except ValueError:
            print(f"Opcion no habilitada")