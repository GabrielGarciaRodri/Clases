palabra = "hola".upper()
print("Bienvenido al juego del ahorcado, la palabra que esta en juego tiene 4 espacios: ")
print("Escriba alguna letra: ")
intento = 3
total = len(palabra)
isPlaying = True
while isPlaying:
    letra = input("Ingrese letra :").upper()
    if (letra in palabra):
        for i in palabra:
            if(letra == i):
                total -= 1    
    else:
        intento -= 1
        if(intento == 0):
            print ("Perdiste")
            isPlaying = False
    
    
#RESUELTO CON CICLO FOR
#for i in range(0,len(palabra),1):
#    letra = input("Ingrese letra :").upper()
#    if (letra in palabra):
#        total -= 1
#        palabra = palabra.replace(letra, "-")
#        if total == 0:
#            print("gano")
#            break
#    else: 
#        intento -= 1 
#    if intento == 0:
#        print ("Perdiste")
#        break
    
   
   