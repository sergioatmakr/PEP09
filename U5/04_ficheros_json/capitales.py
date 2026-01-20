import json

capitales = [
    {"país": "Francia", "capital": "París"},
    {"país": "Australia", "capital": "Canberra"},
    {"país": "Kenia", "capital": "Nairobi"},
    {"país": "Brasil", "capital": "Brasilia"}
]

nombre_archivo = "capitales.json"

try:
    with open(nombre_archivo, "w", encoding="utf-8") as fichero:
        json.dump(capitales, fichero, ensure_ascii=False, indent=4)

    print("Archivo 'capitales.json' creado correctamente.")

except Exception as e:
    print(f"Ocurrió un error al crear el archivo: {e}")