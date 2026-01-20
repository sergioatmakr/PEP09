import csv

patrimonios = [
    {"Ciudad": "Roma", "País": "Italia", "Lugar emblemático": "Coliseo"},
    {"Ciudad": "El Cairo", "País": "Egipto", "Lugar emblemático": "Pirámides de Guiza"},
    {"Ciudad": "Kioto", "País": "Japón", "Lugar emblemático": "Templos históricos"}
]

nombre_archivo = "patrimonios.csv"

try:
    with open(nombre_archivo, "w", encoding="utf-8", newline="") as fichero:
        fieldnames = ["Ciudad", "País", "Lugar emblemático"]
        escritor = csv.DictWriter(fichero, fieldnames=fieldnames, delimiter=";")

        # Escribir cabecera
        escritor.writeheader()

        # Escribir filas
        escritor.writerows(patrimonios)

    print("Archivo 'patrimonios.csv' generado correctamente.")

except Exception as e:
    print(f"Ocurrió un error al crear el archivo: {e}")