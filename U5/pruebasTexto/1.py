# Programa01: Lectura completa de un fichero
# Escribe un programa en Python que abra un fichero llamado datos.txt, 
# lea todo su contenido con read() y lo muestre por pantalla. 
# El fichero debe contener al menos tres líneas de texto.

fichero = open("datos.txt", "r")
contenido = fichero.read()
print(contenido)
fichero.close()