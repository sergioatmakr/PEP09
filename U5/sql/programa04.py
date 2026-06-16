"""
Programa04: Consultar ciudades con más de 25 millones
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

    consulta = """
    SELECT nombre, pais, poblacion_millones
    FROM ciudades
    WHERE poblacion_millones > 25
    """

    cursor.execute(consulta)

    resultados = cursor.fetchall()

    print("Ciudades con más de 25 millones de habitantes:\n")

    for nombre, pais, poblacion in resultados:
        print(
            f"Ciudad: {nombre} | País: {pais} | Población: {poblacion} millones"
        )

except Error as e:
    print("Error:", e)

finally:
    if 'conexion' in locals() and conexion.is_connected():
        cursor.close()
        conexion.close()