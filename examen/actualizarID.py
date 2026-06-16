import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="series",
        password="series",
        database="series",
    )

    cursor = conexion.cursor()

    sql = "UPDATE equipos SET champions = 20 WHERE id = 1"
    cursor.execute(sql)

    conexion.commit()

    print(cursor.rowcount, "fila actualizada.")

    cursor.close()
    conexion.close()

except Error as e:
    print(f" Error con MySQL: {e}")