# Programa 11: Histograma de frecuencia de caracteres
# Pide al usuario el nombre del archivo de entrada.
# Cuenta todas las letras latinas (mayúsculas y minúsculas se tratan como iguales).
# Imprime y guarda en un archivo '.hist' un histograma ordenado de mayor a menor frecuencia.

nombre_archivo = input("Introduce el nombre del archivo de entrada: ")

try:
    frecuencias = {}

    with open(nombre_archivo, "r", encoding="utf-8") as fichero:
        contenido = fichero.read().lower()  # Tratamos mayúsculas y minúsculas igual
        
        for caracter in contenido:
            # Filtramos solo letras latinas convencionales (a la z)
            # Si quieres incluir letras con tilde o 'ñ', puedes modificar esta condición
            if 'a' <= caracter <= 'z':
                if caracter in frecuencias:
                    frecuencias[caracter] += 1
                else:
                    frecuencias[caracter] = 1

    # Ordenamos el diccionario por su valor (frecuencia) de mayor a menor
    # e.x. item[1] es el valor (las veces que aparece)
    frecuencias_ordenadas = sorted(frecuencias.items(), key=lambda item: item[1], reverse=True)

    # Definimos el nombre del archivo de salida (.hist concatenado al original)
    archivo_hist = nombre_archivo + ".hist"

    with open(archivo_hist, "w", encoding="utf-8") as salida:
        print("\n--- Histograma de Frecuencias ---")
        for letra, cuenta in frecuencias_ordenadas:
            linea_salida = f"{letra}: {cuenta}\n"
            
            # Mostrar en pantalla
            print(linea_salida, end="")
            # Escribir en el archivo .hist
            salida.write(linea_salida)
            
    print(f"\nResultados guardados exitosamente en '{archivo_hist}'")

except FileNotFoundError:
    print(f"El archivo '{nombre_archivo}' no se pudo encontrar.")