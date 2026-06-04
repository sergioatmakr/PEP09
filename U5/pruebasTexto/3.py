# Programa03: Escritura básica
# Escribe un programa que cree un fichero saludo.txt y escriba tres frases dentro.
# Usa el modo 'w'. Comprueba que al ejecutar el programa dos veces, el archivo se sobrescribe.

fichero = open("saludo.txt", "w")
fichero.write("Hola, esta es la primera frase.\n")
fichero.write("Esta es la segunda frase del archivo.\n")
fichero.write("Y aquí termina la tercera frase.\n")
fichero.close()