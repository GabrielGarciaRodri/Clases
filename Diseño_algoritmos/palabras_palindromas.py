import os
os.system('cls')

# UNICAMENTE PARA UNA PALABRA
# word = (input("Ingrese una palabra: "))

# if word == word[::-1]:
#     print(f"{word} Es un palindromo")

# else:
#     print(f"{word} No es palindromo")

#Para oraciones completas
word = (input("Ingrese una palabra: "))

# Divide la oración en palabras y eliminar espacios
sinEspacios = [palabra for palabra in word.split() if palabra.strip()]

# Une las palabras sin espacios
union = ''.join(sinEspacios)

if union == union[::-1]:
    print(f"{union} Es un palindromo")

else:
    print(f"{union} no es un palindromo")

