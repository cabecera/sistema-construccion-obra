from os import system
from data_base_MD5 import DatabaseMD5

db = DatabaseMD5()

while True:
    elige = input('\n Elije una opcion: \n\
        \t Ingresar sesion(i)\n\
        \t Crear usuario(c)\n\
        \t Fin(f)\n\
        \t ==> \n ').lower()
    if elige == 'i':
        db.ingresar()
    elif elige == 'c':
        db.crearUsuario()

    elif elige == 'f':
        print('Fin')
        break
    else:
        print('Error de opción')
        input('Pulse Enter para continuar...')
        system('cls')        



    
#MENU CON DICCIONARIOS, NO FUNCIONAL AUN    
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