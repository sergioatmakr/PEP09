# Programa 07: Escritura con control de errores
# Escribe un programa que solicite al usuario un nombre de archivo binario de salida.
# Cree un bytearray con 256 bytes con valores de 0 a 255.
# Intente guardarlo usando with open(nombre, 'wb').
# Si ocurre un error (por permisos, espacio, etc.), muestra el mensaje usando strerror(e.errno).

from os import strerror

nombre_archivo = input("Introduce el nombre del archivo binario de salida: ")

# Creamos un bytearray con los números del 0 al 255
datos_256 = bytearray(range(256))

try:
    with open(nombre_archivo, "wb") as fichero:
        fichero.write(datos_256)
    print(f"Archivo '{nombre_archivo}' creado de manera exitosa.")
except OSError as e:
    # Capturamos OSError (madre de FileNotFoundError, PermissionError, etc.)
    print(f"Error al intentar guardar el archivo: {strerror(e.errno)}")