# Programa02: Lectura con csv.DictReader()
# Crea un programa que lea el archivo ciudades.csv usando csv.DictReader(). Debe:
# - Mostrar los nombres de las columnas (fieldnames).
# - Recorrer las filas e imprimir información como:
#   {Ciudad} ({País}) tiene una población aproximada de {Población (millones)} millones.
# - Si el archivo no incluye cabecera, define manualmente los campos necesarios.

import csv
from os import strerror

try:
    with open("ciudades.csv", "r", encoding="utf-8") as fichero:
        # DictReader mapea la información de cada fila a un diccionario basado en la cabecera
        lector_dict = csv.DictReader(fichero)
        
        # Mostramos los nombres de las columnas (strip para limpiar espacios sobrantes)
        columnas_limpias = [col.strip() for col in lector_dict.fieldnames]
        print(f"Nombres de las columnas encontrados: {columnas_limpias}\n")
        
        # Recorremos e imprimimos el formato solicitado
        for fila in lector_dict:
            # Limpiamos las claves y valores debido a los espacios del archivo original
            ciudad = fila.get("Ciudad", "").strip()
            pais = fila.get(" País", fila.get("País", "")).strip()
            poblacion = fila.get(" Población (millones)", fila.get("Población (millones)", "")).strip()
            
            print(f"{ciudad} ({pais}) tiene una población aproximada de {poblacion} millones.")

except FileNotFoundError:
    print("Error: No se encontró 'ciudades.csv'.")
except OSError as e:
    print(f"Error de lectura: {strerror(e.errno)}")