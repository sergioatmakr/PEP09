import json

archivo_entrada = "paises.json"
archivo_salida = "paises_filtrados.json"

try:
    with open(archivo_entrada, "r", encoding="utf-8") as fichero:
        paises = json.load(fichero)

    continente_usuario = input("Introduce el nombre de un continente: ").strip()

    paises_filtrados = [pais for pais in paises if pais["continente"].lower() == continente_usuario.lower()]

    if paises_filtrados:
        print(f"\nPaíses en {continente_usuario}:")
        for pais in paises_filtrados:
            print(f"{pais['nombre']} tiene {pais['poblacion']} millones de habitantes.")
    else:
        print(f"No se encontraron países en el continente '{continente_usuario}'.")

    with open(archivo_salida, "w", encoding="utf-8") as fichero_salida:
        json.dump(paises_filtrados, fichero_salida, ensure_ascii=False, indent=4)

    print(f"\nArchivo '{archivo_salida}' creado correctamente.")

except FileNotFoundError:
    print(f"Error: El archivo '{archivo_entrada}' no existe.")
except json.JSONDecodeError:
    print("Error: El archivo JSON tiene un formato incorrecto.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")