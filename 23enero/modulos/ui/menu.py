opciones = ["1. AGREGAR PALABRA\n 2. BUSCAR PALABRA\n 3. BORRAR PALABRA\n 4. SALIR"]

def MenuPrincipal()-> int:
    titulo = """
        +++++++++++++++++++++++++++++++++++++++++
        +  DICCIONARIO TECNICO DE PROGRAMACION  +
        +++++++++++++++++++++++++++++++++++++++++
    """
    for item in opciones:
        print(titulo)
        print(item)
    op = int(input(":)_"))
    return op