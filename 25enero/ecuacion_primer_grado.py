import os
os.system('cls')

a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))

def respuesta(a, b):

    if a != 0:
        x = -b/a
        return print(f"solucion unica: {x}")
    
    elif a == 0 and b == 0:
        return "No hay solucion unica"
    
    else:
        return "Sin solucion"
    
solucion = respuesta(a, b)
    
print(solucion)