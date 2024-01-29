import os
os.system('cls')

def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def es_palindromo(numero):
    binario = bin(numero)[2:]
    return binario == binario[::-1]

contador_primos_palindromos = 0
numero = 2

while contador_primos_palindromos < 10:
    if es_primo(numero) and es_palindromo(numero):
        binario_numero = bin(numero)[2:]
        print(f"Primo #{contador_primos_palindromos + 1}: {numero} (Binario: {binario_numero})")
        contador_primos_palindromos += 1
    numero += 1
