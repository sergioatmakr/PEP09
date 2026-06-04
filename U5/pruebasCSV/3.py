# Programa03: Escritura de un CSV con csv.writer()
# Crea un programa que genere un fichero nuevo llamado capitales.csv con los datos:
# París, Francia, Europa / Canberra, Australia, Oceanía / Nairobi, Kenia, África / Ottawa, Canadá, América
# El programa debe:
# - Escribir la cabecera y los datos con writerow() y writerows().
# - Usar un bloque try/except con os.strerror() para capturar errores de E/S.
# - Confirmar con un mensaje final: "Archivo 'capitales.csv' creado correctamente."

import csv
from os import strerror

cabecera = ["Ciudad", "País", "Continente"]

# Fila individual para usar con writerow()
primera_fila = ["París", "Francia", "Europa"]

# Lista de filas restantes para usar con writerows()
filas_restantes = [
    ["Canberra", "Australia", "Oceanía"],
    ["Nairobi", "Kenia", "África"],
    ["Ottawa", "Canadá", "América"]
]

try:
    # newline="" evita líneas en blanco adicionales entre plataformas (Windows/Linux)
    with open("capitales.csv", "w", newline="", encoding="utf-8") as fichero:
        escritor = csv.writer(fichero)
        
        # 1. Escribimos la cabecera
        escritor.writerow(cabecera)
        
        # 2. Escribimos la primera fila usando writerow()
        escritor.writerow(primera_fila)
        
        # 3. Escribimos el resto de datos usando writerows()
        escritor.writerows(filas_restantes)
        
    print("Archivo 'capitales.csv' creado correctamente.")

except OSError as e:
    print(f"Error al escribir el archivo: {strerror(e.errno)}")