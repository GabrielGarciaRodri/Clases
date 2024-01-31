import os
os.system('cls')

producto = {
    "A" : 270,
    "B" : 340,
    "C" : 390
}
#funcion escoger productos

print("Catálogo de productos de maquina dispensadora de alimentos CampusLands.")
cont = 0

for nombre, precio in producto.items():
    cont += 1
    print (f"\t{cont}. Producto: {nombre} ----- valor ${precio}")
    
opc = int(input("Seleccione el producto que desea adquirir.\n"))
nombre=list(producto)[opc-1]
precio=producto.get(nombre)
plata = 0

    
lista= [10, 50, 100]
l_Final = sorted(lista)


#Funcion recibir luks

while plata<precio:
    cont = 1
    print("Insertar moneda")
    for i in l_Final:
        print(f"{cont}. ${i}")
        cont += 1
    moneda = int(input())
    
    match(moneda):
        case 1:
            plata = plata + 10
        case 2:
            plata = plata + 50
        case 3:
            plata = plata + 100
        case _:
            print("Usuario, ese monto no está disponible")

#funcion vueltos

vueltos = plata-precio
print(f"Sus vueltos son {vueltos}")
while vueltos != 0:
    for i in reversed(l_Final): 
        if vueltos >= i:
            print(f"$ {i}")
            vueltos=vueltos-i
            
print("GRACIAS POR SU COMPRA")
    