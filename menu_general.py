
from CRUD.constructoras_crud import *
from CRUD.obras_crud import *
from os import system


# cs = Constructoras()
# ob = Obras()


def default():
    print("Opcion fuera de rango") 
    return

menu_general = {1:Constructoras.menu_constructoras, 2:Obras, 2:exit}

while True:
        print("\n Menu general ")
        print("1. Menu Constructoras")
        print("2. Menu Obras")
        print("3. Fin")

        try: ##validacion solo numeros
            opcion = int(input("ELija una opción \n"))
            menu_general.get(opcion, default)()
        except ValueError:
            print("Error. Por favor, ingrese solo numeros")
        
        input('Pulse Enter para continuar...')
        system('cls')