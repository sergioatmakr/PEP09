import csv
import os

nombre_archivo = "capitales.csv"

cabecera = ["Ciudad", "País", "Continente"]

filas = [
    ["París", "Francia", "Europa"],
    ["Canberra", "Australia", "Oceanía"],
    ["Nairobi", "Kenia", "África"],
    ["Ottawa", "Canadá", "América"]
]

try:
    with open(nombre_archivo, "w", encoding="utf-8", newline="") as fichero:
        escritor = csv.writer(fichero)

        escritor.writerow(cabecera)

        escritor.writerows(filas)

    print("Archivo 'capitales.csv' creado correctamente.")

except OSError as e:
    print(f"Error de E/S: {os.strerror(e.errno)}")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
