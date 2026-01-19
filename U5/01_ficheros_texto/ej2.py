"""Escribe un programa en Python que lea el mismo archivo datos.txt línea a línea y muestre
cada línea numerada en pantalla.
Usa la función enumerate().
El formato debe ser:
◦ Línea 1: <contenido>.
◦ Línea 2: <contenido>
◦ ..."""

with open("../ficherosTexto/datos.txt", "rt", encoding="utf-8") as fichero:
    for linea_no, linea in enumerate(fichero, start=1):
        print(f'Línea:{linea_no}: {linea.strip()}')