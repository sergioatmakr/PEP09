import csv

equipos = [
    {"Nombre": "Real Madrid", "País": "España", "Champions": 15},
    {"Nombre": "AC Milan", "País": "Italia", "Champions": 7},
    {"Nombre": "Bayer Munich", "País": "Alemania", "Champions": 6},
    {"Nombre": "Barcelona", "País": "España", "Champions": 5}
]

nombre_archivo = "equipos.csv"

try:
    with open(nombre_archivo, "w", encoding="utf-8", newline="") as fichero:
        fieldnames = ["Nombre", "País", "Champions"]
        escritor = csv.DictWriter(fichero, fieldnames=fieldnames, delimiter=";")

        # Escribir cabecera
        escritor.writeheader()

        # Escribir filas
        escritor.writerows(equipos)

    print("Archivo 'equipos.csv' generado correctamente.")

except Exception as e:
    print(f"Ocurrió un error al crear el archivo: {e}")


try:
    with open(nombre_archivo, "r") as fichero:
        lector = csv.reader(fichero)
            
        # Saltamos la cabecera
        next(lector)

        max_valor=0
        actual=0  
        nombre=""  
        pais=""
        for fila in lector:
            try:
                actual = int(fila[2])
                if(max_valor<actual):
                    max_valor=actual
                    nombre=fila[0]     
                    pais=fila[1]
            except ValueError:
                print("Error: formato inesperado en una línea del archivo.")
        print(f"El equipo: {nombre} de ({pais}) tiene el mayor número de champions con un total de: {max_valor}.")
except Exception as e:
    print(f"Ocurrió un error al crear el archivo: {e}")