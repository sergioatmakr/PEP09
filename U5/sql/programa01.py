"""
Programa01: Conexión a la base de datos

Conectar a la BD ciudades usando:
usuario: ciudades
contraseña: ciudades
"""

import mysql.connector
from mysql.connector import Error

conexion = None

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="ciudades",
        password="ciudades",
        database="ciudades"
    )

    if conexion.is_connected():
        print("Conexión establecida correctamente")

except Error as e:
    print("Error al conectar:", e)

finally:
    if conexion and conexion.is_connected():
        conexion.close()
        print("Conexión cerrada")