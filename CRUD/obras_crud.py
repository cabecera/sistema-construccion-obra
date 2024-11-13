from datetime import datetime
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
            
    #CREATE
    def create_obras(self):
        codigo_obra = input('Ingrese ID de la Obra = \n')
        sql1 = 'select codigoObra from obras where codigoObra ='+repr(codigo_obra)
        
        if not codigo_obra.isalnum() or len(codigo_obra) != 10:
            raise ValueError("El código debe ser un valor alfanumérico de exactamente 10 caracteres.")
        
        try:
            self.cursor.execute(sql1)
            if self.cursor.fetchone() == None:
                # Pedir el ID de la Constructora
                id_constructora = input('Ingrese ID de la Constructora = \n')
                sql2 = 'select idConstructora from constructoras where idConstructora =' + repr(id_constructora)
                
                try:
                    self.cursor.execute(sql2)
                    if self.cursor.fetchone() != None:  # Si el id_constructora existe
                        
                        descripcionObra = input('Descripcion de la obra = \n')
                        costo = int(input('Costo de la Obra = \n'))
                        fechaInicio = input('Fecha de inicio Obra (dd/mm/aaaa) = \n')
                        
                        # Convertir la fecha de inicio a formato datetime
                        fecha_inicio = datetime.strptime(fechaInicio, '%Y-%m-%d')

                        # Convertir la fecha al formato adecuado para SQL (YYYY-MM-DD)
                        fecha_inicio_sql = fecha_inicio.strftime('%Y-%m-%d')
                        
                        #Insertamos en la base de datos
                        sql3 = "insert into obras (codigoObra, idConstructora, descripcionobra,costo,fechainicio) values (" + repr(codigo_obra) + "," + repr(id_constructora) + "," + repr(descripcionObra) + "," + repr(costo) + "," + repr(fecha_inicio_sql) +")"
                        
                        try:
                            self.cursor.execute(sql3)
                            self.conexion.commit()
                            print("Obra agregada exitosamente.")
                        except Exception as err:
                            self.conexion.rollback()
                            print("Error al insertar la obra:", err)
                    else:
                        print("El ID de la Constructora no existe.")
                except Exception as err:
                    print("Error al verificar el ID de la Constructora:", err)
            else:
                print('Ya existe este ID')
        except Exception as err:
            print(err) 