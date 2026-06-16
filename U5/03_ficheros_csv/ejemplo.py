import csv

# 1. Cargar datos del CSV
personas = []

with open("personas.csv", newline="", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    
    for fila in lector:
        fila["edad"] = int(fila["edad"])  # convertir a número
        personas.append(fila)

# 2. Pedir valor al usuario
x = int(input("Introduce edad mínima: "))

# 3. Filtrar datos
resultado = []

for p in personas:
    if p["edad"] > x:
        resultado.append(p)

# 4. Mostrar resultados
print("\nPersonas con edad mayor que", x)
for r in resultado:
    print(r)