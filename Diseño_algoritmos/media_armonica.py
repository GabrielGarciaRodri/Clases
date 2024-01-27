import os
os.system('cls')

num = int(input("¿Cuantos numeros va a ingresar?) "))

lista = []

for i in range (num):
    numero = float (input(f"ingrese el numero {i}: "))
    #almacena el numero i dentro de la lista con append
    lista.append(numero)

#En cada iteración, la variable numero toma el valor del siguiente elemento en la lista.
media = (num / sum(1/numero for numero in lista))

print (f"Numeros ingresados: {lista}")

print (f"La media es: {media}")