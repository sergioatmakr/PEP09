"""Escribe un programa en Python que abra un fichero llamado datos.txt, lea todo su
contenido con read() y lo muestre por pantalla. El fichero debe contener al menos tres líneas de texto."""

# Abre el archivo ej1.txt
fichero=open("../ficherosTexto/datos.txt","rt",encoding="utf-8")

# Lee el contenido del fichero​
contenido = fichero.read()

# Imprime el contenido del fichero​
print(contenido)

# Cierra el fichero​
fichero.close()