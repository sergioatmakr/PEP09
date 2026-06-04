# Programa 05: Escritura desde un bytearray modificado
# [Corrección de enunciado repetido]: Lee datos.bin usando readinto(),
# modifica el contenido del bytearray y vuelve a guardarlo en modo 'wb'.

bufer = bytearray(10)

# 1. Leemos el archivo actual
with open("datos.bin", "rb") as fichero:
    fichero.readinto(bufer)
print(f"Búfer original: {list(bufer)}")

# 2. Modificamos algunas posiciones del bytearray
# Cambiamos, por ejemplo, el primer elemento a 99 y el último a 100
bufer[0] = 99
bufer[-1] = 100
print(f"Búfer modificado: {list(bufer)}")

# 3. Guardamos el bytearray modificado de vuelta en el archivo
with open("datos.bin", "wb") as fichero:
    fichero.write(bufer)
print("Archivo 'datos.bin' actualizado con el bytearray modificado.")