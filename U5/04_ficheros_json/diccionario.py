import json

pais = {
    "nombre": "Islandia",
    "capital": "Reikiavik",
    "idiomas": ["Islandés", "Inglés"],
    "superficie_km2": 103000
}

# Convertir el diccionario a una cadena JSON
cadena_json = json.dumps(pais, indent=2, sort_keys=True, ensure_ascii=False)

# Mostrar la cadena generada
print(cadena_json)