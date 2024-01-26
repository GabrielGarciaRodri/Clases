notaA = int(0)
notaB = int(0)
notaC = int(0)



print("Escriba la nota del 60%: ")
notaA = float(input(":"))

if notaA <= 5 and notaA >= 0:

    print("Escriba la nota del 25%: ")
    notaB = float(input(":"))

    print("Escriba la nota del 15%: ")
    notaC = float(input(":"))

    print("La nota final es = ",((notaA * 0.6) + (notaB * 0.25) + (notaC * 0.15)))

else :
    
    print("Las notas validas van de 0 a 5, intente nuevamente")




