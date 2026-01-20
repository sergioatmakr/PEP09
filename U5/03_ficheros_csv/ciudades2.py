import csv

try:
    with open("ciudades.csv", "r", encoding="utf-8") as fichero:
        
        try:
            lector = csv.DictReader(fichero)
            
            if not lector.fieldnames or lector.fieldnames == [None]:
                fieldnames = ["Ciudad", "País", "Población (millones)"]
                fichero.seek(0)  # Volver al inicio del archivo
                lector = csv.DictReader(fichero, fieldnames=fieldnames)
                
                print("El archivo no tenía cabecera. Se definieron los siguientes campos:")
                print(fieldnames)
            else:
                print("Columnas encontradas en el archivo:")
                print(lector.fieldnames)

            print()

            for fila in lector:
                ciudad = fila["Ciudad"]
                pais = fila["País"]
                poblacion = fila["Población (millones)"]
                print(f"{ciudad} ({pais}) tiene una población aproximada de {poblacion} millones.")
        
        except csv.Error as e:
            print(f"Error leyendo el archivo CSV: {e}")

except FileNotFoundError:
    print("Error: El archivo 'ciudades.csv' no existe.")
except PermissionError:
    print("Error: No tienes permisos para leer este archivo.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")