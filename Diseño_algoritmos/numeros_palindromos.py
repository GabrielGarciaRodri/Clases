import os
os.system('cls')

num1 = (input("Ingrese un numero: "))

if num1 == num1[::-1]:
    print(f"{num1} Es un palindromo")
    
else:
    print(f"{num1} No es un palindromo")