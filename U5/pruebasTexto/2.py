# Programa02: Lectura línea a línea
# Escribe un programa en Python que lea el mismo archivo datos.txt línea a línea 
# y muestre cada línea numerada en pantalla. Usa la función enumerate().

fichero = open("datos.txt", "r")
for indice, linea in enumerate(fichero, start=1):
    # Usamos strip() para quitar los saltos de línea duplicados al imprimir
    print(f"Línea {indice}: {linea.strip()}")
fichero.close()