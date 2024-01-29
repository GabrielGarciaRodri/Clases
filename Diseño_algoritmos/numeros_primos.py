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



    