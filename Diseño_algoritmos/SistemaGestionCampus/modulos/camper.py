#Guarda la funcionalidad del CRUD
import os
from tabulate import tabulate
from .variables import save, getAll

def create():
    
    os.system("clear")
    print("""
          *********************************
          *     FORMULARIO DEL CAMPER     *
          *********************************
          """)
    save({
        "nombre" :input("Ingrese el nombre del camper: "),
        "apellido" : input("Ingrese el apellido del camper: "),
        "edad" : int(input("Ingrese la edad del camper: "))
    })
    os.system('pause')
    
def read():
    print("""
             *********************************
             *        TABLA DEL CAMPER       *
             ********************************* 
            """)
    os.system('cls')
    print (tabulate(getAll()))
    os.system('pause')
    
def update():
    print("El camper se actualizó")

def delete():
    print("El camper se borró")
    
def menu():
    
    menu = ["Crear","Buscar","actualizar","Borrar","Salir"]
    """El siguiente try permite repetir la opcion en caso de que
    El usuario se equivoque"""
    while True:
        #Enumera el array menu
        os.system("clear")
        print("""
             *********************************
             *        MENU DEL CAMPER        *
             ********************************* 
            """)
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