# Programa 08: Manejo de errores
# Escribe un programa que intente abrir un fichero que no existe (inexistente.txt) 
# y capture la excepción. Usa from os import strerror para mostrar un mensaje 
# de error legible en pantalla.

from os import strerror

try:
    with open("inexistente.txt", "r") as fichero:
        contenido = fichero.read()
except FileNotFoundError as e:
    # e.errno contiene el código numérico del error del sistema operativo
    print(f"Error al abrir el archivo: {strerror(e.errno)}")