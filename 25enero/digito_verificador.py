# Desarrolle un programa que calcule el dígito verificador de un rol UTFSM.

# Para calcular el dígito verificador, se deben realizar los siguiente pasos:

# Obtener el rol sin guión ni dígito verificador.
# Invertir el número. (e.g: de 201012341 a 143210102).
# Multiplicar los dígitos por la secuencia 2, 3, 4, 5, 6, 7, si es que se acaban 
# los números, se debe comenzar denuevo, por ejemplo, con 143210102:
# 1×2+4×3+3×4+2×5+1×6+0×7+1×2+0×3+2×4=52

# Al resultado obtenido, es decir, 52, debemos sacarle el módulo 11, es decir:

# 52 % 11 = 8

# Con el resultado obtenido en el paso anterior, debemos restarlo de 11:

# 11 − 8 = 3

# Finalmente, el dígito verificador será el obtenido en la resta: 201012341-3.

import os
os.system('cls')
secuencia=[2,3,4,5,6,7]

num = input("Ingrese el numero: ")

#Invierte el numero
invertido = str (num)[::-1]
print (f"El invertido es: {invertido}")

resultado = 0
for i, d in enumerate (invertido):
    digito = int (d)
    secInd = i % len(secuencia)
    resultado += digito * secuencia[secInd]
print (f"El resultado de la secuencia es: {resultado}")

modulo = resultado % 11
verificador = (11-modulo) 

print(f"El digito verificador es: {num}-{verificador}")
    

# def mul(lista, invertido):
#     return [lista[i] * invertido[i] for i in range (len(lista))]
# print (mul(secuencia)*(invertido))



