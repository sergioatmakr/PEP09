# Programa01: Lectura básica con csv.reader()
# Crea un fichero llamado ciudades.csv con el siguiente contenido:
# Ciudad, País, Población (millones)
# Tokio, Japón, 37.4
# Delhi, India, 30.3
# Shanghai, China, 27.1
# São Paulo, Brasil, 22.0
# Escribe un programa que: Lea el fichero usando csv.reader().
# Muestre en pantalla frases como: "La ciudad de Tokio está en Japón y tiene 37.4 millones de habitantes."
# Controle las posibles excepciones.

import csv
from os import strerror

# Primero creamos el archivo ciudades.csv con los datos solicitados
datos_iniciales = """Ciudad, País, Población (millones)
Tokio, Japón, 37.4
Delhi, India, 30.3
Shanghai, China, 27.1
São Paulo, Brasil, 22.0"""

try:
    with open("ciudades.csv", "w", encoding="utf-8") as f:
        f.write(datos_iniciales)
except OSError as e:
    print(f"Error al preparar el archivo de prueba: {strerror(e.errno)}")

# --- Solución del ejercicio ---
try:
    with open("ciudades.csv", "r", encoding="utf-8") as fichero:
        # Usamos csv.reader para leer las filas como listas
        lector = csv.reader(fichero)
        
        # Saltamos la línea de la cabecera
        cabecera = next(lector)
        
        for fila in lector:
            # Comprobamos que la fila tenga los elementos esperados para evitar IndexError
            if len(fila) >= 3:
                ciudad = fila[0].strip()
                pais = fila[1].strip()
                poblacion = fila[2].strip()
                
                print(f"La ciudad de {ciudad} está en {pais} y tiene {poblacion} millones de habitantes.")
                
except FileNotFoundError:
    print("Error: El archivo 'ciudades.csv' no existe.")
except OSError as e:
    print(f"Error de E/S al leer el archivo: {strerror(e.errno)}")
except csv.Error as e:
    print(f"Error en el formato del archivo CSV: {e}")