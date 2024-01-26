import modulos.ui.menu as m
import modulos.glosario as g
import os

glosario =  {
    "A" : {},
    "B" : {},
    "C" : {},
    "D" : {},
    "E" : {},
    "F" : {}
}
isActive = True
while isActive:
    os.system('cls')
    
    op = m.MenuPrincipal()
    if (op == 1):
        g.AddWord(glosario)
        print(glosario)
        os.system('pause')
        
    elif (op == 2):
        g.SearchWord(glosario)
    elif (op == 3):
        g.DelWord(glosario)
        print(glosario)
        os.system('pause')
        
        
        
    elif (op == 4):
        isActive = False
        
    else:
        os.system('cls')
        isActive=False
        print("La opcion ingresada no es valida!!!")
        os.system('pause')