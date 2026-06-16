import mysql.connector
from mysql.connector import Error


def crear_tabla(cursor):
    sql = """
    CREATE TABLE IF NOT EXISTS ciudades (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        pais VARCHAR(50),
        poblacion_millones FLOAT
    )
    """

    cursor.execute(sql)
    print("Tabla creada correctamente")


def insertar_datos(cursor, conexion):
    datos = [
        ("Tokio", "Japón", 37.4),
        ("Delhi", "India", 30.3),
        ("Shanghái", "China", 27.1),
        ("São Paulo", "Brasil", 22.0),
        ("Ciudad de México", "México", 21.7)
    ]

    sql = """
    INSERT INTO ciudades
    (nombre, pais, poblacion_millones)
    VALUES (%s, %s, %s)
    """

    cursor.executemany(sql, datos)
    conexion.commit()

    print(f"{cursor.rowcount} filas insertadas")


def consultar_ciudades(cursor):
    sql = """
    SELECT nombre, pais, poblacion_millones
    FROM ciudades
    WHERE poblacion_millones > 25
    """

    cursor.execute(sql)

    resultados = cursor.fetchall()

    print("\nCiudades con más de 25 millones:\n")

    for nombre, pais, poblacion in resultados:
        print(f"{nombre} - {pais} - {poblacion} millones")


def realizar_transaccion(cursor, conexion):
    try:
        cursor.execute(
            """
            INSERT INTO ciudades
            (nombre, pais, poblacion_millones)
            VALUES (%s, %s, %s)
            """,
            ("Madrid", "España", 6.8)
        )

        cursor.execute(
            """
            DELETE FROM ciudades
            WHERE poblacion_millones < 10
            """
        )

        conexion.commit()

        print("\nTransacción realizada correctamente")

    except Error:
        conexion.rollback()
        print("\nTransacción revertida por error")


def main():
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

        cursor = conexion.cursor()

        crear_tabla(cursor)
        insertar_datos(cursor, conexion)
        consultar_ciudades(cursor)
        realizar_transaccion(cursor, conexion)

    except Error as e:
        print("Error:", e)

    finally:
        if conexion and conexion.is_connected():
            cursor.close()
            conexion.close()
            print("\nConexión cerrada")


if __name__ == "__main__":
    main()