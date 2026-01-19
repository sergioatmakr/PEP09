# ===============================================
# imports de la librería estándar
# ===============================================
# (No se necesitan módulos de la biblioteca estándar en este caso.)

# ===============================================
# imports de librerías de terceros
# ===============================================
# (No se usan librerías externas.)

# ===============================================
# imports de módulos propios
# ===============================================
import operaciones
import figuras

# ===============================================
# Submenú de operaciones matemáticas
# ===============================================
def menu_operaciones():
    """Submenú que gestiona las operaciones matemáticas básicas."""
    while True:
        print("\n=== OPERACIONES MATEMÁTICAS ===")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Volver al menú principal")

        opcion = input("Elige una opción: ")

        if opcion == "5":
            break

        try:
            a = float(input("Introduce el primer número: "))
            b = float(input("Introduce el segundo número: "))
        except ValueError:
            print("Error: debes ingresar solo números.")
            continue

        if opcion == "1":
            print(f"Resultado: {operaciones.suma(a, b)}")
        elif opcion == "2":
            print(f"Resultado: {operaciones.resta(a, b)}")
        elif opcion == "3":
            print(f"Resultado: {operaciones.multiplicacion(a, b)}")
        elif opcion == "4":
            print(f"Resultado: {operaciones.division(a, b)}")
        else:
            print("Opción no válida. Intenta de nuevo.")

# ===============================================
# Submenú de figuras geométricas
# ===============================================
def menu_figuras():
    """Submenú que gestiona el cálculo de áreas geométricas."""
    while True:
        print("\n=== CÁLCULO DE ÁREAS GEOMÉTRICAS ===")
        print("1. Círculo")
        print("2. Triángulo")
        print("3. Rectángulo")
        print("4. Volver al menú principal")

        opcion = input("Elige una opción: ")

        if opcion == "4":
            break

        try:
            if opcion == "1":
                radio = float(input("Introduce el radio del círculo: "))
                area = figuras.calcular_area_circulo(radio)
                print(f"Área del círculo = 3.14 × {radio}² = {area:.2f}")

            elif opcion == "2":
                base = float(input("Introduce la base del triángulo: "))
                altura = float(input("Introduce la altura del triángulo: "))
                area = figuras.calcular_area_triangulo(base, altura)
                print(f"Área del triángulo = ({base} × {altura}) / 2 = {area:.2f}")

            elif opcion == "3":
                base = float(input("Introduce la base del rectángulo: "))
                altura = float(input("Introduce la altura del rectángulo: "))
                area = figuras.calcular_area_rectangulo(base, altura)
                print(f"Área del rectángulo = {base} × {altura} = {area:.2f}")

            else:
                print("Opción no válida.")
        except ValueError:
            print("Error: debes ingresar números válidos.")

# ===============================================
# Función principal
# ===============================================
def main():
    """Función principal del programa."""
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Operaciones matemáticas")
        print("2. Figuras geométricas")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            menu_operaciones()
        elif opcion == "2":
            menu_figuras()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# ===============================================
# Bloque de ejecución principal
# ===============================================
if __name__ == "__main__":
    main()
