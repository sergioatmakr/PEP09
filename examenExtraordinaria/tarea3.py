import mysql.connector
from mysql.connector import Error


def crear_tabla(cursor):
    sql = """
    CREATE TABLE IF NOT EXISTS pilotos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(150) NOT NULL,
        pais VARCHAR(100),
        mundiales INT
    )
    """

    cursor.execute(sql)
    print("Tabla creada correctamente")


def insertar_datos(cursor, conexion):
    datos = [
        ("Michael Schumacher", "Alemania", 7),
        ("Ayrton Senna", "Brasil", 3),
        ("Alonso", "España", 2),
    ]

    sql = """
    INSERT INTO pilotos
    (nombre, pais, mundiales)
    VALUES (%s, %s, %s)
    """

    cursor.executemany(sql, datos)
    conexion.commit()

    print(f"{cursor.rowcount} filas insertadas")


def consultar_pilotos(cursor):
    sql = """
    SELECT nombre, pais, mundiales
    FROM pilotos
    WHERE mundiales > 3
    """

    cursor.execute(sql)

    resultados = cursor.fetchall()

    print("\nPilotos con mas de 3 mundiales:\n")

    for nombre, pais, mundiales in resultados:
        print(f"{nombre} - {pais} - {mundiales} ")


def actualizar(cursor, conexion):
    try:
        cursor.execute(
            """
            UPDATE pilotos SET mundiales = 8 WHERE id = 2
            """
        )

        conexion.commit()

        print("\Actualización de mundiales realizada correctamente")

    except Error:
        conexion.rollback()
        print("\nTransacción revertida por error")


def main():
    conexion = None

    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="formula1",
            password="formula1",
            database="formula1"
        )

        if conexion.is_connected():
            print("Conexión establecida correctamente")

        cursor = conexion.cursor()

        crear_tabla(cursor)
        insertar_datos(cursor, conexion)
        actualizar(cursor, conexion)
        consultar_pilotos(cursor)
        

    except Error as e:
        print("Error:", e)

    finally:
        if conexion and conexion.is_connected():
            cursor.close()
            conexion.close()
            print("\nConexión cerrada")


if __name__ == "__main__":
    main()