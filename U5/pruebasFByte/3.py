# Programa03: Lectura parcial (por bloques)
# Crea un programa que lea un archivo binario de 20 bytes y lo procese en fragmentos de 5 bytes.
# Usa read(5) dentro de un bucle while.
# Muestra los bytes leídos en cada iteración.
# El bucle debe detenerse cuando no haya más datos.

# Primero, para que el programa funcione correctamente, creamos un archivo binario de 20 bytes
with open("archivo20.bin", "wb") as f:
    f.write(bytearray(range(20)))

# Procesamiento por bloques de 5 bytes
with open("archivo20.bin", "rb") as fichero:
    iteracion = 1
    while True:
        bloque = fichero.read(5)
        if not bloque:  # Si el bloque está vacío, es el fin del archivo
            break
        print(f"Iteración {iteracion} - Bytes leídos: {list(bloque)}")
        iteracion += 1