# Programa 09: Lectura y escritura combinadas
# Crea un programa que abra un fichero en modo 'r+'. Primero debe leer 
# su contenido y mostrarlo y luego, añadir al final del fichero la línea: 
# "Archivo actualizado correctamente". Asegúrate de que no se borre el contenido existente.

# Nota: 'r+' abre para lectura y escritura, pero no posiciona el puntero al final 
# automáticamente al escribir si ya has leído, así que hay que tener cuidado.

with open("datos.txt", "r+") as fichero:
    print("Contenido actual del archivo:")
    contenido = fichero.read()
    print(contenido)
    
    # Al haber leído todo, el puntero ya está al final del archivo.
    # Escribimos la nueva línea asegurándonos de que empiece bien.
    fichero.write("\nArchivo actualizado correctamente")