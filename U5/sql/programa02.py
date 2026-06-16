"""
Programa02: Crear una tabla ciudades
"""

import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="ciudades",
        password="ciudades",
        database="ciudades"
    )

    cursor = conexion.cursor()

    sql = """
    CREATE TABLE ciudades (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        pais VARCHAR(50),
        poblacion_millones FLOAT
    )
    """

    cursor.execute(sql)

    print("Tabla creada correctamente")

except Error as e:
    print("Error:", e)

finally:
    if 'conexion' in locals() and conexion.is_connected():
        cursor.close()
        conexion.close()