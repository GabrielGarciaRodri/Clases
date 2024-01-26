import os
os.system('cls')
"""#Declara
numero = []  
#lISTA VACIA
#Obtener la longitud
print(len(numero))
print(type(numero))
#Agregar elementos a la lista
numero.append(1)
print(numero)
#Acceder elementos a la lista
print(numero[0])
#Modificar elemento
numero[0] = 20
print(numero[0])
#Eliminar 
numero.pop(0)
print(len(numero))"""
#inicializar
frutas = ["Manzana","Pera"]
frutas.insert(0,"Uvas")
print(frutas.index("Manzana"))
#frutas.pop(frutas.index("Manzana")) (eliminar)
hola = frutas.index("Pera")
print(hola)
#Acceder valores
for item in frutas:
    print(item)
eliminar = input("Ingrese el nombre de la fruta a eliminar: ")
"""
Como eliminar
for i,item in enumerate(frutas):
    if(eliminar == item):
        #frutas.pop(frutas.index(i))(cuidado con la funcion, no se puede eliminar algo de una
        #que se esta usando)
        frutas.remove(eliminar)
        print(frutas)"""
#Se usa cuando se quiere eliminar dos registros iguales
tem = []
for item in frutas:
    if (eliminar != item):
        tem.append(item)
frutas = tem
for item in frutas:
    print(item)