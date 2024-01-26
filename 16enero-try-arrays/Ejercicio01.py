"""
Ejercicio:
Se desea realizar un programa que permita leer N numeros enteros positivos y cuando se ingrese un numero negativo debe mostrar la siguiente informacion;
1. Total de numeros pares ingresados
2. Tota de numeros impares ingresados
3. Promedio de los numeros enteros registrados
4. Cuantos numeros son mayores que 50
5. Cuantos numeros son mayores de 10 y menores que 50
6. Cuantos numeros son menores de 10
7. Total de numeros

Analisis:
N numero = while
Solo numeros enteros positivos
Condicion numero negativo, acabar el  ciclo
1. Contador numero pares, for
2. Contador numeros impares, for
3. promedio operacion matematica
4. Contador numeros mayores a 50, for
5. Contador numeros mayores a 10 y menores que 50 , for
6. Contador numeros menores de 10, for 

consonantes = int(0)
vocales = int(0)
lstvocales = "aeiou".upper()    
for caracter in mensaje:
    if caracter.upper() in lstvocales:
        vocales = vocales + 1
    elif caracter.isalpha():
        consonantes += 1
        
print (f"El total de vocales es = {vocales}")
print (f"El total de consonantes es = {consonantes}")

"""
par = int(0)
impar = int(0)
may = int(0)
bet = int(0)
men = int(0)
divprom = int(0)
aux = int((0))

isPay = True
while isPay :
    
    print("Bienvenido, digite el numero a continuacion")
    numero = int(input((":")))
    
    if numero < 0 :
         print("El total de numeros pares es: ", par)
         print("El total de numeros impares es: ", impar)
         print("El promedio es: ", prom)
         print("El total de numeros mayores a 50 es: ", may)
         print("El total de numeros entre 50 y 10 es: ", bet)
         print("El total de numeros menores a 10 es: ", men)
         isPay = False

    npar = numero % 2
    if npar == 0:
            par = par + 1
    else:
        impar = impar + 1
    
    aux += numero
    divprom = divprom + 1
    prom = (aux) / divprom

    if numero >= 50 :
         may = may + 1
    elif numero <= 10:
         men = men + 1
    else :
         bet = bet + 1
    

    


