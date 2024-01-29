#¿Existen otros valores p que sean el n-ésimo primo, 
#tales que espejo(p) es el espejo(n)-ésimo primo?

import os
os.system('cls')

def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def espejo(numero):
    return int(str(numero)[::-1])

def encontrar_espejo_primo_n(n):
    contador_primos = 0
    numero = 2

    while True:
        if es_primo(numero):
            contador_primos += 1
            if contador_primos == n:
                espejo_n_primo = espejo(numero)
                if es_primo(espejo_n_primo):
                    print(f"{n}-ésimo primo: {numero}, Espejo: {espejo_n_primo}")
                    break

        numero += 1

n = 12  # Puedes cambiar el valor de n según tu pregunta
encontrar_espejo_primo_n(n)
