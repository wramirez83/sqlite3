#importar sqlite3
import sqlite3
from sqlite3 import Error
from config import Config

class DbManager():
    def __init__(self):
        pass
    
    def connection(self):
        try:
            #Crear la conexion / o se crea
            self.con = sqlite3.connect("parking.db")
            print("Conexion Realizada y Cursor")
            return self.con.cursor()
        except Error:
            print(Error)

    def insertUser(self,cursor, data):   
        cursor.execute("""INSERT INTO users (email, password, status) VALUES(?,?,?)""", data)
        
    def insertParking(self,cursor, data):   
        cursor.execute("""INSERT INTO parking (plate, datetimein) VALUES(?,?)""", data)

    def __del__(self):
        print("Destruccion Llamada de la instancia")
        self.con.commit()
        self.con.close()
    
#con = connection()
#cursor = cursor(con)
#insertUser(cursor, ("correo@gmail.com", "12344544", "Activo"))
#close(con)
print(Config.DB_NAME)