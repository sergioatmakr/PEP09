import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="champions",
        password="champìons",
        database="champions",
    )

    print(conexion)
    conexion.close()
except Error as e:
    print(f" Error con MySQL: {e}")