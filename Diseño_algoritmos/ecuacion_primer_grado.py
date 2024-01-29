import os
os.system('cls')

a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))

if a != 0:
    x = -b/a
    print(f"Solucion unica: {x}")
    
elif a == 0 and b == 0:
    print("No hay solucion unica") 
    
else:
    print("Sin solucion") 
