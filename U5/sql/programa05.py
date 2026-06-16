"""
Programa05: Transacción
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

    insertar = """
    INSERT INTO ciudades
    (nombre, pais, poblacion_millones)
    VALUES (%s, %s, %s)
    """

    cursor.execute(
        insertar,
        ("Madrid", "España", 6.8)
    )

    borrar = """
    DELETE FROM ciudades
    WHERE poblacion_millones < 10
    """

    cursor.execute(borrar)

    conexion.commit()

    print("Transacción realizada correctamente")

except Error as e:
    if 'conexion' in locals():
        conexion.rollback()

    print("Transacción revertida por error.")
    print(e)

finally:
    if 'conexion' in locals() and conexion.is_connected():
        cursor.close()
        conexion.close()