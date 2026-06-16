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

    sql = "INSERT INTO equipos (nombre, pais,champions) VALUES (%s, %s,%s)"
    val = [
            ("Barcelona','España',6"),
            ("Bayer,Alemania,5"),
            ("Real Madrid,España,5")
            ]
    cursor.executemany(sql, val)

    conexion.commit()

    print(cursor.rowcount, "fila insertada.")

    cursor.close()
    conexion.close()

except Error as e:
    print(f" Error con MySQL: {e}")