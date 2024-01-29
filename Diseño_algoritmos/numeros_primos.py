import os
os.system('cls')

num = int(input("1.Ingrese un numero para saber si es primo o compuesto: "))

if num < 4:
    print ("El numero es primo")
else:
    compuesto = False
    for i in range (2, int(num**0.5)+1):

        if num % i == 0:
            compuesto = True
            break

    if compuesto:
        print("Es compuesto")

    else:
        print("Es primo")


#Escriba un programa que muestre los n
#primeros números primos, donde n
#es ingresado por el usuario:
        
n = int(input("Ingrese un numero, este mostrara la cantidad de numeros primos hasta ese numero: "))

print(f"los {n} primeros numeros primos son:")
contador = 0
numero = 2

while contador < n:
    #Mismo sistema que el de los numeros compuesto,
    #Solo que ahora cuando la variable actual es
    #Verdadera, es un numero primo
    primo = True
    for i in range (2, int(numero**0.5) + 1):
        if numero % i == 0:
            primo = False
            break
    if primo:
        print(numero,end=' ')
        contador += 1
    numero += 1

#Escriba un programa que cuente cuántos 
#son los números primos menores que m
#, donde m es ingresado por el usuario:

m = int(input("Ingrese un numero: "))
primo = True
for i in range (2, int(numero**0.5) + 1):
    if numero % i == 0:
        primo = False
        break



    

    