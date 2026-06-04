# Programa 08: Copiador seguro de archivos
# Escribe un programa que: Pida al usuario el archivo de origen y el destino.
# Compruebe que el archivo de origen existe. Copie su contenido en bloques de 64 KB.
# Muestre progreso en pantalla (por ejemplo, cada 1 MB copiado).
# Informe al final del número total de bytes escritos.
# Use try/except, with, y bytearray correctamente.

import os
from os import strerror

origen_path = input("Introduce la ruta del archivo de origen: ")
destino_path = input("Introduce la ruta del archivo de destino: ")

# 1. Comprobamos si el archivo de origen existe explícitamente
if not os.path.exists(origen_path):
    print(f"Error: El archivo de origen '{origen_path}' no existe.")
else:
    TAMANO_BUFFER = 64 * 1024  # Bloques de 64 KB
    UN_MEGABYTE = 1024 * 1024  # 1 MB para calcular el progreso
    
    bufer = bytearray(TAMANO_BUFFER)
    total_bytes_escritos = 0
    bytes_acumulados_progreso = 0

    try:
        with open(origen_path, "rb") as f_origen, open(destino_path, "wb") as f_destino:
            while True:
                bytes_leidos = f_origen.readinto(bufer)
                
                if bytes_leidos == 0:
                    break
                
                f_destino.write(bufer[:bytes_leidos])
                total_bytes_escritos += bytes_leidos
                bytes_acumulados_progreso += bytes_leidos
                
                # Mostrar el progreso en pantalla cada vez que supera 1 MB acumulado
                if bytes_acumulados_progreso >= UN_MEGABYTE:
                    megas_copiados = total_bytes_escritos / UN_MEGABYTE
                    print(f"Progreso: {megas_copiados:.2f} MB copiados...")
                    bytes_acumulados_progreso %= UN_MEGABYTE  # Mantener el residuo

        print("\n--- Copia de seguridad finalizada con éxito ---")
        print(f"Número total de bytes escritos en el destino: {total_bytes_escritos} bytes ({total_bytes_escritos / UN_MEGABYTE:.2f} MB).")

    except OSError as e:
        print(f"Ocurrió un error crítico durante la copia: {strerror(e.errno)}")