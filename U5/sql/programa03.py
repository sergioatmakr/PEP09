"""
Programa03: Insertar registros
"""

import mysql.connector
from mysql.connector import Error

datos = [
    ("Tokio", "Japón", 37.4),
    ("Delhi", "India", 30.3),
    ("Shanghái", "China", 27.1),
    ("São Paulo", "Brasil", 22.0),
    ("Ciudad de México", "México", 21.7)
]

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="ciudades",
        password="ciudades",
        database="ciudades"
    )

    cursor = conexion.cursor()

    sql = """
    INSERT INTO ciudades
    (nombre, pais, poblacion_millones)
    VALUES (%s, %s, %s)
    """

    cursor.executemany(sql, datos)

    conexion.commit()

    print(f"{cursor.rowcount} filas insertadas")

except Error as e:
    print("Error:", e)

finally:
    if 'conexion' in locals() and conexion.is_connected():
        cursor.close()
        conexion.close()