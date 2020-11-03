import os

class Config():
    #Retorna el directorio de trabajo actual
    DB_PATH = os.getcwd()
    DB_NAME = "parking.db"