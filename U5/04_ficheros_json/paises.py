import json

nombre_archivo = "paises.json"

try:
    with open(nombre_archivo, "r", encoding="utf-8") as fichero:
        datos = json.load(fichero)

        for pais in datos:
            nombre = pais["nombre"]
            continente = pais["continente"]
            poblacion = pais["poblacion"]
            print(f"{nombre} está en {continente} y tiene {poblacion} millones de habitantes.")

except FileNotFoundError:
    print(f"Error: El archivo '{nombre_archivo}' no existe.")
except json.JSONDecodeError:
    print("Error: El archivo JSON tiene un formato incorrecto.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")