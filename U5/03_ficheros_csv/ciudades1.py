import csv

try:
    with open("ciudades.csv", "r", encoding="utf-8") as fichero:
        lector = csv.reader(fichero)
        
        # Saltamos la cabecera
        next(lector)
        
        for fila in lector:
            try:
                ciudad, pais, poblacion = fila
                print(f"La ciudad de {ciudad} está en {pais} y tiene {poblacion} millones de habitantes.")
            except ValueError:
                print("Error: formato inesperado en una línea del archivo.")

except FileNotFoundError:
    print("Error: El archivo 'ciudades.csv' no existe.")
except PermissionError:
    print("Error: No se tienen permisos para leer el archivo.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")