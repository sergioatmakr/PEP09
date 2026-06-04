# Programa 10: Lectura y escritura combinadas
# Crea un programa que lea un fichero origen.txt y copie su contenido 
# a otro fichero copia.txt línea por línea. Después, muestra por pantalla:
# Número total de líneas copiadas, número total de palabras y número total de caracteres.

# Nota: Crea un archivo 'origen.txt' con texto antes de ejecutar.
try:
    lineas_totales = 0
    palabras_totales = 0
    caracteres_totales = 0

    with open("origen.txt", "r") as origen, open("copia.txt", "w") as copia:
        for linea in origen:
            copia.write(linea)
            
            lineas_totales += 1
            # Contamos caracteres (incluyendo saltos de línea)
            caracteres_totales += len(linea)
            # split() separa por espacios y saltos de línea para contar palabras
            palabras_totales += len(linea.split())

    print(f"Número total de líneas copiadas: {lineas_totales}")
    print(f"Número total de palabras: {palabras_totales}")
    print(f"Número total de caracteres: {caracteres_totales}")

except FileNotFoundError:
    print("Por favor, asegúrate de que el archivo 'origen.txt' exista.")