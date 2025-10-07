FACTOR = 1.61

millas = float(input("Introduce una distancia en millas: "))
kilometros = float(input("Introduce una distancia en kilómetros: "))

millas_a_km = millas * FACTOR
km_a_millas = kilometros / FACTOR

print(f"{millas} millas equivalen a {millas_a_km:.2f} kilómetros.")
print(f"{kilometros} kilómetros equivalen a {km_a_millas:.2f} millas.")
