import json

cadena_json = '''
[
    {"nombre": "Chile", "moneda": "Peso chileno"},
    {"nombre": "Egipto", "moneda": "Libra egipcia"}
]
'''

# Convertir la cadena JSON en un objeto Python
datos = json.loads(cadena_json)

# Mostrar el tipo de dato obtenido
print("Tipo de datos:", type(datos))

# Recorrer e imprimir la información
for pais in datos:
    print(f"{pais['nombre']} utiliza la moneda {pais['moneda']}.")