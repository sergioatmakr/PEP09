# Programa 04: Escritura desde diccionarios con csv.DictWriter()
# Crea un programa que escriba un archivo patrimonios.csv con información sobre
# ciudades con lugares Patrimonio de la Humanidad.
# El programa debe:
# - Usar DictWriter con fieldnames=["Ciudad", "País", "Lugar emblemático"].
# - Escribir la cabecera con writeheader() y las filas con writerows().
# - Cambiar el delimitador a ';'.
# - Mostrar un mensaje final: "Archivo 'patrimonios.csv' generado correctamente."

import csv
from os import strerror

# Definición de la estructura de datos corregida del enunciado
patrimonios = [
    {"Ciudad": "Roma", "País": "Italia", "Lugar emblemático": "Coliseo"},
    {"Ciudad": "El Cairo", "País": "Egipto", "Lugar emblemático": "Pirámides de Guiza"},
    {"Ciudad": "Kioto", "País": "Japón", "Lugar emblemático": "Templos históricos"}
]

columnas = ["Ciudad", "País", "Lugar emblemático"]

try:
    with open("patrimonios.csv", "w", newline="", encoding="utf-8") as fichero:
        # Configuramos DictWriter especificando las columnas y cambiando el delimitador a ';'
        escritor_dict = csv.DictWriter(fichero, fieldnames=columnas, delimiter=";")
        
        # Escribimos la fila de títulos/cabecera
        escritor_dict.writeheader()
        
        # Escribimos todos los diccionarios de la lista de golpe
        escritor_dict.writerows(patrimonios)
        
    print("Archivo 'patrimonios.csv' generado correctamente.")

except OSError as e:
    print(f"Error al generar el archivo: {strerror(e.errno)}")