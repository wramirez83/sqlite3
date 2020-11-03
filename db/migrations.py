#importar sqlite3
import sqlite3 #Relativa
import os
import sys

sys.path.append("..")
from config import Config #Absoluto

root = Config.DB_PATH + os.sep + ".." + os.sep + "sql" + os.sep + Config.DB_NAME

#Crear la conexion / o se crea
con = sqlite3.connect(root)

#Crear el Curso
cursor = con.cursor()
cursor2 = con.cursor()

#Crear una tabla
cursor.execute("""CREATE TABLE users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT NOT NULL,
    password TEXT NOT NULL,
    status TEXT
)
               """)

cursor2.execute("""CREATE TABLE parking(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    plate TEXT NOT NULL,
    datetimein TEXT NOT NULL,
    datetimeout TEXT
)
               """)
con.commit()
con.close()
