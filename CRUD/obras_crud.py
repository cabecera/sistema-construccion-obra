import mysql.connector 
from os import system
class Obras(): 
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

    def list_obras(self): 
        sql = 'select * from obras'
        try:
            self.cursor.execute(sql)
            repu = self.cursor.fetchall()
            print((
            f"{'Codigo Obra ':10}"
            f"{'Id Constructora ':10}"
            f"{'Descripción Obra ':12}"
            f"{'Costo de la Obra ':12}"
            f"{'Fecha Inicio ':12}"
            ))
            for rep in repu:
                print(f"{rep[0]:10}{rep[1]:20}{rep[2]:20}{rep[3]:<12}{rep[4].strftime('%d/%m/%Y'):12}")
        except Exception as err:
            print(err)