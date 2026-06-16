# 1. Leer archivo
personas = []

with open("personas.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        # quitar salto de línea
        linea = linea.strip()
        
        # separar por coma
        nombre, edad, ciudad = linea.split(",")
        
        # convertir edad a número
        persona = {
            "nombre": nombre,
            "edad": int(edad),
            "ciudad": ciudad
        }
        
        personas.append(persona)

# 2. Pedir filtro al usuario
x = int(input("Introduce edad mínima: "))

# 3. Filtrar
resultado = []

for p in personas:
    if p["edad"] > x:
        resultado.append(p)

# 4. Mostrar resultados
print("\nPersonas con edad mayor que", x)

for r in resultado:
    print(r)