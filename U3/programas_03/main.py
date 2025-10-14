# ===============================================
# imports de la librería estándar
# ===============================================
# (Aquí podrías importar módulos estándar si los necesitaras, por ejemplo: os, sys, math, etc.)
# En este caso no se necesitan.

# ===============================================
# imports de librerías de terceros
# ===============================================
# (Por ahora no usamos ninguna librería externa, como numpy o pandas.)

# ===============================================
# imports de módulos propios
# ===============================================
import operaciones  # Importamos nuestro módulo personalizado

# ===============================================
# Definición de funciones principales
# ===============================================
def main():
    """Función principal del programa"""
    print("=== Calculadora básica ===")
    
    try:
        a = float(input("Introduce el primer número: "))
        b = float(input("Introduce el segundo número: "))
    except ValueError:
        print("Error: Debes ingresar solo números.")
        return

    # Mostrar resultados usando las funciones del módulo
    print("\nResultados:")
    print(f"Suma: {operaciones.suma(a, b)}")
    print(f"Resta: {operaciones.resta(a, b)}")
    print(f"Multiplicación: {operaciones.multiplicacion(a, b)}")
    print(f"División: {operaciones.division(a, b)}")

# ===============================================
# Bloque para asegurar ejecución sólo si el archivo es el principal
# ===============================================
if __name__ == "__main__":
    # Se pueden procesar argumentos, inicializar variables, etc.
    main()
