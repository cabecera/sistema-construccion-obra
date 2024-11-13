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
    def list_constructoras(self): 
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
            
    #CREATE
    def create_constructora(self):
        id_constructora = input('Ingrese ID de la constructora= \n')
        
        #if not id_constructora.isalnum() or len(id_constructora) != 10:
        #    raise ValueError("El código debe ser un valor alfanumérico de exactamente 10 caracteres.")
        
        sql1 = 'select idConstructora from constructoras where idConstructora ='+repr(id_constructora)
        try:
            self.cursor.execute(sql1)
            if self.cursor.fetchone() == None:
                fono = input('Fono = \n') 
                email = input('Email \n')
                sql2 = "insert into constructoras values("+repr(id_constructora)+","+repr(fono)+","+repr(email)+")"
                try:
                    self.cursor.execute(sql2)
                    self.conexion.commit()    
                except Exception as err:
                    self.conexion.rollback()
                    print(err)
            else:
                print('Ya existe este ID')
        except Exception as err:
            print(err)  
            
    #READ
    def read_constructora(self):    
        id_buscar = input('Ingrese ID de constructora a buscar = \n')
    
        sql = 'select * from constructoras where idconstructora = '+repr(id_buscar) 
        #repr agrega cremillas al cod
        try:
            self.cursor.execute(sql)
            rep = self.cursor.fetchone()
            if rep is not None:
                print((
                f"{'ID Constructora':10}"
                f"{'Fono ':20}"
                f"{'Email ':12}"
                ))
                
                print(f"{rep[0]:10}{rep[1]:20}{rep[2]:12}")
            else:
                print('Id no existe en la base de datos')
        except Exception as err:
            print("Error al realizar la consulta", err) 
            
    #UPDATE
    def update_constructoras(self):
        #Llamar una funcion dentro de otra
        self.list_constructoras()
        
        id_buscar = input('Ingrese ID de constructora que desea actualizar = \n')
        sql1 = 'select * from constructoras where idconstructora='+repr(id_buscar)
        try:
            self.cursor.execute(sql1)
            rep=self.cursor.fetchone()
            if rep!= None:
                print((
                    f"{'ID Constructora':20}"
                    f"{'Fono ':20}"
                    f"{'Email ':12}"
                    ))
                print(f"{rep[0]:20}{rep[1]:20}{rep[2]:12}")
                ##Da la opcion de elegir que desea modificar
                elige=input('\n Que desea modificar?\n fono(f)\n email(e)\n').lower()
                if elige=='f':
                    campo='fono'
                    nuevo=input('Ingrese nuevo fono= ')
                if elige=='e':
                    campo='email'
                    nuevo=input('Ingrese nuevo email= ')
                

                sql2 = 'update constructoras set '+campo+'='+repr(nuevo)+' where idconstructora='+repr(id_buscar)
                try:
                    self.cursor.execute(sql2)
                    self.conexion.commit()
                except Exception as err:
                    self.conexion.rollback()
                    print(err)
            else:
                print('No existe ese código')
        except Exception as err: 
            print(err)
            
    #DELETE        
    def delete_constructora(self):
        #Llamar una funcion dentro de otra
        self.list_constructoras()
        
        id_buscar = input('Ingrese ID de constructora que desea eliminar = \n')
        sql1 = 'select * from constructoras where idconstructora='+repr(id_buscar)
        try:
            self.cursor.execute(sql1)
            if self.cursor.fetchone() != None:
                sql2 = 'select * from obras where idConstructora ='+repr(id_buscar)
                try:
                    self.cursor.execute(sql2)
                    if self.cursor.fetchone()!= None:
                        print('No se puede eliminar, porque esta en la tabla Obras')
                    else:
                        sql3 = 'delete from constructoras where idconstructora='+repr(id_buscar)
                        try:
                            self.cursor.execute(sql3)
                            self.conexion.commit()
                        except Exception as err:
                            self.conexion.rollback()
                            print(err)
                except Exception as err:
                    print(err)
            else:
                print('No existe este codigo')
        except Exception as err:
            print(err)