# Programa01: Creación y escritura básica
# Crea un programa que genere un archivo binario llamado datos.bin.
# Crea un bytearray con los números del 1 al 10.
# Escríbelo en el fichero usando el modo 'wb'.
# Muestra por pantalla un mensaje indicando cuántos bytes se escribieron.

# Creamos el bytearray con los números del 1 al 10
datos_escribir = bytearray(range(1, 11))

with open("datos.bin", "wb") as fichero:
    bytes_escritos = fichero.write(datos_escribir)
    print(f"Se han escrito con éxito {bytes_escritos} bytes en 'datos.bin'.")