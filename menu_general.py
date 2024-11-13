
from CRUD.constructoras_crud import *
from CRUD.obras_crud import *
from os import system

cs = Constructoras()
ob = Obras()

def cerrarBD(self):
    self.cursor.close()
    self.conexion.close()

while True:
    elige = input('\n Elije una opcion: \n\
        \t Menu Constructoras(c)\n\
        \t Menu Obras(o)\n\
        \t Fin(f)\n\
        \t ==> \n ').lower()
    #Si elige la opcion de menu constructora
    if elige == 'c':
        while True:
            elige = input('\n Elije una opcion: \n\
                \t Listar Constructoras(l)\n\
                \t Buscar una Constructora(b)\n\
                \t Crear una Constructora(c)\n\
                \t Actualizar una Constructora(a)\n\
                \t Eliminar una Constructora(e)\n\
                \t Fin(f)\n\
                \t ==> \n ').lower()
            #Si elige una opcion de CRUD
            if elige == 'l':
                cs.list_constructoras()
            elif elige == 'c':
                cs.create_constructora()
            elif elige == 'b':
                cs.read_constructora()  
            elif elige == 'a':
                cs.update_constructoras()
            elif elige == 'e':
                cs.delete_constructora()
            elif elige == 'f':
                print('Fin')
                cs.cerrarBD()
                break
            else:
                print('Error de opción')
            input('Pulse Enter para continuar...')
            system('cls')
            
    #Si elige la opcion de menu obras     
    elif elige == 'o':
        while True:
            elige = input('\n Elije una opcion: \n\
                \t Listar Obras(l)\n\
                \t Buscar una Obra(b)\n\
                \t Crear una Obra(c)\n\
                \t Actualizar una Obra(a)\n\
                \t Fin(f)\n\
                \t ==> \n ').lower()
            #Si elige una opcion de CRUD
            if elige == 'l':
                ob.list_obras()
            elif elige == 'c':
                ob.create_obras()
            elif elige == 'b':
                ob.read_obras()
            elif elige == 'a':
                ob.update_obras()
                        
            elif elige == 'f':
                print('Fin')
                ob.cerrarBD()
                break
            else:
                print('Error de opción')
            input('Pulse Enter para continuar...')
            system('cls')
    
    elif elige == 'f':
        print('Fin')
        cerrarBD()
        break
    else:
        print('Error de opción')    
    input('Pulse Enter para continuar...')
    system('cls')
            

    
    
# def default():
#     print("Opcion fuera de rango") 
#     return

# menu_general = {1:Constructoras.menu_constructoras, 2:Obras, 2:exit}

# while True:
#         print("\n Menu general ")
#         print("1. Menu Constructoras")
#         print("2. Menu Obras")
#         print("3. Fin")

#         try: ##validacion solo numeros
#             opcion = int(input("ELija una opción \n"))
#             menu_general.get(opcion, default)()
#         except ValueError:
#             print("Error. Por favor, ingrese solo numeros")
        
#         input('Pulse Enter para continuar...')
#         system('cls')