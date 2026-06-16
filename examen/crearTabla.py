import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        host="localhost",
        user="chamnpìons",
        password="champions",
        database="champions",
    )

    cursor = conexion.cursor()
    cursor.execute(
    "CREATE TABLE equipos (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(150) NOT NULL, pais VARCHAR(100),champions INT);")

    cursor.close()
    conexion.close()


except Error as e:
    print(f" Error con MySQL: {e}")