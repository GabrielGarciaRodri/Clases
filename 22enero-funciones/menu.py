import os
def MenuPrincipal():
    os.system('cls')
    operaciones=["+. Suma \n-. Resta\n0. Salir"]
    for item in operaciones:
        print(item)
    return input(":")