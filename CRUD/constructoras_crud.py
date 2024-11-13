import mysql.connector
from os import system
class Constructoras(): 
    def __init__(self):  
        self.conexion = mysql.connector.connect( 
            host = 'localhost',
            user = 'root',
            password = 'carlos123',
            database = 'empresa'
        )
        self.cursor = self.conexion.cursor()    
    
    
    def cerrarBD(self):
        self.cursor.close()
        self.conexion.close()
        
    #Lista
    def listConstructoras(self): 
        sql = 'select * from constructoras'
        try:
            self.cursor.execute(sql)
            repu = self.cursor.fetchall()
            print((
            f"{'ID Constructora':10}"
            f"{'Fono ':20}"
            f"{'Email ':12}"
            ))
            for rep in repu:
                print(f"{rep[0]:10}{rep[1]:20}{rep[2]:12}")
        except Exception as err:
            print(err)
    
    
    #MENU CONSTRUCTORA
    
    def default():
        print("Opcion fuera de rango") 
        return
    def menu_constructoras ():
        menu_constructora = {1:Constructoras.listConstructoras, 2:exit}
    
        respuesta = "si"
        while respuesta =="si":
            print("\n Menu de Constructoras ")
            print("Opcion 1:  Listar constructoras")
            print("Opcion 5:  Volver al menu principal")

            try:   
                opcion = int(input("Elija una opcion \n"))
                if opcion ==5:
                    respuesta = input("Seguro quiere salir al menú general?? si/no \n")
                    respuesta = respuesta.lower()
                
                menu_constructora.get(opcion)()
            except ValueError:
                print("Error. Por favor, ingrese solo numeros")
                import time
                time.sleep(2)
    