import json

info = {
    "Nombre" : input("Ingrese el nombre: "),
    "Telefono": [
        {
            f"{'Fijo' if(int (input('0. Nro Fijo 1. Celular: '))) else 'celular' }":
            int(input(f'Numero de contacto {x+1}: '))
        }
        for x in range((int(input("Cuantos numeros de contacto tiene?: "))))
    ]
}

busqueda = input ("Numero")
for x, val in enumerate (info["Telefono"]):
    if( busqueda in val.get("Celular")):
        print(val)

# print(json.dumps(info))