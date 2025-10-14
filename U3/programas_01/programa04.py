"""
Mejora el programa anterior de forma que compruebe si el usuario está introduciendo
valores correctos (por ejemplo, el radio no puede ser un número negativo) y si no es así
que pida muestre un aviso y vuelva a pedir el valor.
"""


def main():
    correcto=False
    while not correcto:
        mostrar_menu()
        opcion=int(input())
        if opcion>=1 and opcion<=4:
            correcto=True
    match opcion:
        case 1:
            opcion1()
        case 2:
            opcion2()
        case 3:
            opcion3()
        case 4:
            return 4


def mostrar_menu():
    print("1. Calcular el área de un círculo")
    print("2. Calcular el área de un triángulo")
    print("3. Calcular el área de un rectángulo")
    print("4. Salir")
    print("Introduce una opción (1-4):")
    
        
def calcular_area_circulo(radio):
    area= 3,14*radio**2
    return print(f"El area del circulo es 3,14*{radio}^2 = {area}")

def opcion1():
    correcto=False
    while not correcto:
        radio=int(input("Introduce el radio de tu circulo"))
        if radio>0:
            correcto=True
    calcular_area_circulo (radio)

def calcular_area_triangulo(base,altura):
    return print(f"El area del triangulo es ({base}*{altura})/2={(base*altura)/2}")

def opcion2():
    correcto=False
    while not correcto:
        base=int(input("Introduce la base de tu triangulo"))
        if base>0:
            correcto=True
        else:
            print("El valor tiene que ser mayor que 0")

    correcto=False
    while not correcto:
        altura=int(input("Introduce la altura de tu triangulo"))
        if altura>0:
            correcto=True
        else:
            print("El valor tiene que ser mayor que 0")
    
    calcular_area_triangulo(base,altura)

def calcular_area_rectangulo(base,altura):
    return print(f"El area del rectangulo es {base}*{altura}={base*altura}")
    
def opcion3():
    correcto=False
    while not correcto:
        base=int(input("Introduce la base de tu rectangulo"))
        if base>0:
            correcto=True
        else:
            print("El valor tiene que ser mayor que 0")

    correcto=False
    while not correcto:
        altura=int(input("Introduce la altura de tu rectangulo"))
        if altura>0:
            correcto=True
        else:
            print("El valor tiene que ser mayor que 0")
    
    calcular_area_rectangulo(base,altura)


opcion=main()

while opcion !=4:
    opcion=main()