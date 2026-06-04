# Programa 05: Bloque with
# Crea un programa que escriba una lista de nombres (["Ana", "Pedro", "Lucía", "Eva"]) 
# en un fichero alumnos.txt usando el bloque with. Luego, en el mismo programa, 
# vuelve a abrir el archivo con with y muestra todos los nombres en mayúsculas.

nombres = ["Ana", "Pedro", "Lucía", "Eva"]

# Escritura
with open("alumnos.txt", "w") as fichero:
    for nombre in nombres:
        fichero.write(nombre + "\n")

# Lectura y conversión a mayúsculas
with open("alumnos.txt", "r") as fichero:
    for linea in fichero:
        print(linea.strip().upper())