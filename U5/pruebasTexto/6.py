# Programa 06: Lectura controlada
# Crea un programa que lea un fichero texto.txt carácter a carácter 
# usando read(1) hasta llegar al final del archivo. 
# Cuenta cuántos caracteres totales contiene y muestra el resultado.

# Nota: Asegúrate de crear un archivo 'texto.txt' para probarlo.
try:
    with open("texto.txt", "r") as fichero:
        total_caracteres = 0
        caracter = fichero.read(1)
        
        while caracter != "":
            total_caracteres += 1
            caracter = fichero.read(1)
            
    print(f"El número total de caracteres es: {total_caracteres}")
except FileNotFoundError:
    print("El archivo 'texto.txt' no existe. Créalo primero para probar.")