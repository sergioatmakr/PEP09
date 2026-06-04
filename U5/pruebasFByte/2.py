# Programa02: Lectura completa
# Escribe un programa que abra el archivo datos.bin en modo 'rb' y lea su contenido con read().
# Convierte los datos leídos en un bytearray.
# Muestra cada byte en formato hexadecimal (hex()).

with open("datos.bin", "rb") as fichero:
    contenido_bytes = fichero.read()
    
# Convertimos los datos leídos en un bytearray
mi_bytearray = bytearray(contenido_bytes)

print("Contenido del archivo en formato hexadecimal:")
for byte in mi_bytearray:
    print(hex(byte), end=" ")
print()  # Salto de línea final