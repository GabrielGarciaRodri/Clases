import os
os.system('cls')

a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))

def resolver_ecuacion_lineal(a, b):
    # Verificar si 'a' es diferente de cero para evitar divisiones por cero
    if a != 0:
        # Despejar 'x' de la ecuación ax + b = 0
        x = -b / a
        return x
    else:
        # La ecuación no tiene solución si 'a' es igual a cero
        return "La ecuación no tiene solución real cuando 'a' es igual a cero."
    
x = -b/a
solucion = resolver_ecuacion_lineal(a, b)
    
print(f"La solución de {a}x + {b} = 0 es x = {solucion}")