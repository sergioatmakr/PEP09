# Programa 06: Copia de ficheros binarios
# Escribe un programa que copie el contenido de un archivo binario (origen.bin) a otro
# (copia.bin) usando un búfer de 64 KB.
# Usa readinto() y write() dentro de un bucle while.
# Muestra cuántos bytes se copiaron en total.

# Primero generamos un 'origen.bin' de prueba con datos para simular el proceso
with open("origen.bin", "wb") as f:
    f.write(bytearray([7] * 70000))  # Un archivo de poco más de 68 KB

# Proceso de copia
TAMANO_BUFFER = 64 * 1024  # 64 KB = 65536 bytes
bufer = bytearray(TAMANO_BUFFER)
bytes_totales_copiados = 0

with open("origen.bin", "rb") as origen, open("copia.bin", "wb") as copia:
    while True:
        # Leemos del origen guardando en el bytearray
        bytes_leidos = origen.readinto(bufer)
        
        if bytes_leidos == 0:  # Fin de fichero
            break
            
        # Escribimos en el destino exactamente los bytes leídos de la porción del búfer
        copia.write(bufer[:bytes_leidos])
        bytes_totales_copiados += bytes_leidos

print(f"Copia finalizada. Se han copiado un total de {bytes_totales_copiados} bytes.")