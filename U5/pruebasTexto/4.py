# Programa 04: Añadir texto sin borrar el anterior
# Modifica el ejercicio anterior para que, en lugar de sobrescribir, 
# añada nuevas líneas cada vez que se ejecute. Usa el modo 'a'.

fichero = open("saludo.txt", "a")
fichero.write("Nueva línea añadida en una nueva ejecución.\n")
fichero.write("Otra línea más para acumular contenido.\n")
fichero.close()