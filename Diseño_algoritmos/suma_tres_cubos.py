import os
os.system('cls')

#NO ME SALE Y NO SÉ PORQUÉ!!!!!!!!!!!!!! >:(
def cubo(objetivo):

    objetivo = 100
    limite = int(objetivo ** (1/3)) + 1
    x = -limite
    while x <= limite:
        y = -limite
        while y <= limite:
            z = -limite
            while z <= limite:
                if x**3 + y**3 + z**3 == objetivo:
                    if (x, y, z) != (1870, -1797, -903):
                        print(f"{x}^3 + {y}^3 + {z}^3 = {objetivo}")
                z += 1
            y += 1
        x += 1

        print(f"Expresiones de {objetivo} como la suma de tres cubos:")

        print("1870^3 - 1797^3 - 903^3 = 100")

        cubo(objetivo)
