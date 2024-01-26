mensaje = "Fundamentos, 10"
consonantes = int(0)
vocales = int(0)
lstvocales = "aeiou".upper()    
for caracter in mensaje:
    if caracter.upper() in lstvocales:
        vocales = vocales + 1
    elif caracter.isalpha():
        consonantes += 1
        
print (f"El total de vocales es = {vocales}")
print (f"El total de consonantes es = {consonantes}")

