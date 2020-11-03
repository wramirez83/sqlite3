from db import DbManager

db = DbManager()
cursor = db.connection()
db.insertUser(cursor, ("correo@gmail.com", "12344544", "Activo"))
db.insertParking(cursor, ("MXR471", "2020-11-03 15:00:00"))
#del db