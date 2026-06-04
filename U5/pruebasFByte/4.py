# Programa 04: Lectura con readinto()
# Crea un bytearray vacío de 10 posiciones.
# Abre el archivo datos.bin en modo 'rb' y usa readinto() para rellenar el bytearray.
# Muestra los bytes leídos y el número total de bytes cargados.

# Creamos un bytearray vacío de 10 posiciones (inicializadas a 0)
bufer = bytearray(10)

with open("datos.bin", "rb") as fichero:
    # readinto llena el búfer existente y devuelve la cantidad de bytes leídos
    bytes_cargados = fichero.readinto(bufer)

print(f"Número total de bytes cargados: {bytes_cargados}")
print(f"Contenido del bytearray: {list(bufer)}")