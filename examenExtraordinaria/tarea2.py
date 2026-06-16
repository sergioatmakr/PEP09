import csv

futbolistas = [
    {"Nombre": "Michael Schumacher", "País": "Alemania", "Mundiales": "7"},
    {"Nombre": "Ayrton Senna", "País": "Brasil", "Mundiales": "3"},
    {"Nombre": "Alonso", "País": "España", "Mundiales": "2"}
]

nombre_archivo = "futbolistas.csv"

try:
    with open(nombre_archivo, "w", encoding="utf-8", newline="") as fichero:
        fieldnames = ["Nombre", "País", "Mundiales"]
        escritor = csv.DictWriter(fichero, fieldnames=fieldnames, delimiter=";")

        # Escribir cabecera
        escritor.writeheader()

        # Escribir filas
        escritor.writerows(futbolistas)

    print("Archivo 'futbolistas.csv' generado correctamente.")

except Exception as e:
    print(f"Ocurrió un error al crear el archivo: {e}")


    # 1. Cargar datos del CSV
personas = []
try:
    with open("futbolistas.csv", newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        
        for fila in lector:
            fila["Mundiales"] = int(fila["Mundiales"])  # convertir a número
            personas.append(fila)

    # 3. Filtrar datos
    resultado = []
    menor=100
    for p in personas:
        if p["Mundiales"]<menor:
            menor=int(p["Mundiales"])
            resultado.append(p)

    # 4. Mostrar resultados
    print("\nEl jugador con menos mundiales es")
    for r in resultado:
        print(r)
except Exception as e:
    print(f"Ocurrió un error al calcular el menor el archivo: {e}")        