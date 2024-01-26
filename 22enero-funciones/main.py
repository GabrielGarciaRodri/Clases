import matematicas as mat
import os
import menu as menu

isRunning = True
while isRunning:
    op=menu.MenuPrincipal()
    if (op == "+"):
        os.system('cls')
        num1 = int(input("Ingrese el primer numero"))
        num2 = int(input("Ingrese el segundo numero"))
        print( f'La suma del {num1}+{num2} = {mat.Operaciones(num1, num2,op)} ')
        os.system('pause')
    
    if (op == ("0")):
        isRunning = False