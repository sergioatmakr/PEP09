import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
    host="localhost",
    user="champions",
    password="champions",
    database="champions",
    )

    cursor = conexion.cursor()

    cursor.execute("SELECT nombre FROM equipos WHERE champions > 5")

    resultado = cursor.fetchall()

    for serie in resultado:
        print(serie)

    cursor.close()
    conexion.close()

except Error as e:
    print(f" Error con MySQL: {e}")