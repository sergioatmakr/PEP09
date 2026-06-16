import json

# 1. Cargar datos del JSON
with open("personas.json", "r", encoding="utf-8") as archivo:
    personas = json.load(archivo)

# 2. Pedir valor al usuario
x = int(input("Introduce edad mínima: "))

# 3. Filtrar datos
resultado = [p for p in personas if p["edad"] > x]

# 4. Mostrar resultados
print("\nPersonas con edad mayor que", x)

for r in resultado:
    print(r)