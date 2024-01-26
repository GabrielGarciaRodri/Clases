import os
os.system('cls')
nro = 1
totalNros = 0
sumNros = 0
totalPares = 0
totalImpares = 0
while (nro >= 0):
    try:
        nro = int(input("Ingrese un Nro Positivo"))
    except ValueError:
        print("Error en el valor ingresado")
        nro = 0
        os.system('pause')

    
    if (nro >= 0):
        if (nro % 2 == 0):
            totalPares +=1
        else:
            totalImpares +=1
        
        totalNros += 1
        sumNros += nro

print(f'Promedio de numeros ingresados = {sumNros/totalNros}')
print(f'Total numeros pares = {totalPares}')
print(f'Total numeros ingresados = {totalNros}')

