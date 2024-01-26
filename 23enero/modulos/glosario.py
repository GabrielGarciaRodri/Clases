import os

def AddWord(dataSource : dict):
    
    word = input("Ingrese la palabra: ").upper()
    data = dataSource.get(word[0:1])
    significado = input("Ingrese el significado: ")
    wordAdd = {
            "palabra" : word,
            "significado" : significado,
        }
    data.update({word:wordAdd})
    os.system('pause')
    
def DelWord(dataSource : dict):
    palabra = input("Ingrese la palabra que quiere borrar: ").upper()
    dataSource.get(palabra[0:1]).pop(palabra)
        
            
def SearchWord(dataSource : dict):
    palabra = input("Ingrese la palabra que desea buscar: ").upper()
    print(dataSource.get(palabra[0:1]).get(palabra)["significado"])
    os.system('pause')