# Programa 07: Reposicionamiento
# Crea un programa que lea las dos primeras líneas de un fichero 
# y luego use seek(0) para volver al inicio. 
# Después, muestra nuevamente todo el contenido completo.

with open("datos.txt", "r") as fichero:
    print("--- Leyendo las dos primeras líneas ---")
    linea1 = fichero.readline()
    linea2 = fichero.readline()
    print(linea1, end="")
    print(linea2, end="")
    
    # Reposicionamos el puntero al inicio (byte 0)
    fichero.seek(0)
    
    print("\n--- Volviendo al inicio y leyendo todo ---")
    todo_el_contenido = fichero.read()
    print(todo_el_contenido)