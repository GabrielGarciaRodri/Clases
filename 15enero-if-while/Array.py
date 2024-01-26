import os
numero = int(0)


meses = ["Enero","Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]


isPay = True
while isPay:
    try:
        numero = int(input("Ingrese un numero entre 1 y 12: ")) 
        numero = numero - 1
        print(meses[numero]) 
    except:
        print("Ingrese un numero entero entre 1 y 12")
        numero = int(0)
        os.system('pause')
    
    try:
        sn = str(input("Desea continuar? (S/N) "))
    except:
        print("Caracter no valido")
        numero = int(0)
        os.system('pause')
    
    if sn == "N" :
        isPay = False

 
